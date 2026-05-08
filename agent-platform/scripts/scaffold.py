from pathlib import Path
import argparse
import shutil

import yaml


ROOT_FILES = [
    ".env.example",
    ".gitignore",
    "Makefile",
]

SHARED_FILES = [
    "llm.py",
    "tracing.py",
    "settings.py",
    "cache.py",
    "checkpointer.py",
]

INTERFACE_FILES = [
    "api.py",
    "streamlit.py",
]

EVAL_FILES = [
    "ragas.py",
    "metrics.py",
]

WORKER_AGENT_FILES = [
    "agent.py",
    "prompt.md",
    "models.py",
    "judge.py",
    "AGENT_SPEC.md",
]

ORCHESTRATOR_FILES = [
    "graph.py",
    "state.py",
    "routing.py",
    "supervisor.py",
    "AGENT_SPEC.md",
]


def read_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file) or {}


def mkdir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def create_init(path: Path) -> None:
    mkdir(path)

    init_file = path / "__init__.py"

    if not init_file.exists():
        init_file.write_text("", encoding="utf-8")


def read_template(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_template(content: str, variables: dict) -> str:
    for key, value in variables.items():
        placeholder = "{{ " + key + " }}"
        content = content.replace(placeholder, str(value))

    return content


def write_template(
    template_path: Path,
    output_path: Path,
    variables: dict,
) -> None:
    content = read_template(template_path)
    rendered = render_template(content, variables)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not output_path.exists():
        output_path.write_text(rendered, encoding="utf-8")


def copy_root_files(
    platform_root: Path,
    project_path: Path,
) -> None:
    for file_name in ROOT_FILES:
        source = platform_root / file_name
        destination = project_path / file_name

        if source.exists() and not destination.exists():
            shutil.copyfile(source, destination)


def create_root_files(
    project_path: Path,
    project_name: str,
) -> None:
    readme = f"# {project_name}\n\nAI-native multi-agent project.\n"

    pyproject = f"""[project]
name = "{project_name}"
version = "0.1.0"
requires-python = ">=3.11"

dependencies = [
    "langchain",
    "langgraph",
    "pydantic",
    "pydantic-settings",
    "langfuse",
    "ragas",
    "dspy-ai",
    "fastapi",
    "uvicorn",
    "streamlit",
    "pyyaml",
]
"""

    write_if_missing(project_path / "README.md", readme)
    write_if_missing(project_path / "pyproject.toml", pyproject)


def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text(content, encoding="utf-8")


def create_shared(
    platform_root: Path,
    project_path: Path,
    variables: dict,
) -> None:
    shared_path = project_path / "shared"
    create_init(shared_path)

    for file_name in SHARED_FILES:
        template = (
            platform_root
            / "templates"
            / "shared"
            / f"{file_name}.tpl"
        )

        output = shared_path / file_name

        write_template(template, output, variables)


def create_interfaces(
    platform_root: Path,
    project_path: Path,
    interfaces: dict,
    variables: dict,
) -> None:
    interfaces_path = project_path / "interfaces"
    create_init(interfaces_path)

    if interfaces.get("api", True):
        write_template(
            platform_root
            / "templates"
            / "interfaces"
            / "api.py.tpl",
            interfaces_path / "api.py",
            variables,
        )

    if interfaces.get("streamlit", True):
        write_template(
            platform_root
            / "templates"
            / "interfaces"
            / "streamlit.py.tpl",
            interfaces_path / "streamlit.py",
            variables,
        )


def create_eval(
    platform_root: Path,
    project_path: Path,
    variables: dict,
) -> None:
    eval_path = project_path / "eval"
    create_init(eval_path)

    golden_set_path = eval_path / "golden_set"
    mkdir(golden_set_path)

    for file_name in EVAL_FILES:
        template = (
            platform_root
            / "templates"
            / "eval"
            / f"{file_name}.tpl"
        )

        output = eval_path / file_name

        write_template(template, output, variables)


def create_worker_agent(
    platform_root: Path,
    project_path: Path,
    agent: dict,
    variables: dict,
) -> None:
    agent_name = agent["name"]

    agent_variables = {
        **variables,
        "agent_name": agent_name,
        "agent_description": agent.get(
            "description",
            "Describe this agent.",
        ),
        "agent_class_name": agent_name.title().replace("_", ""),
    }

    agent_path = project_path / "agents" / agent_name
    create_init(agent_path)

    for file_name in WORKER_AGENT_FILES:
        if (
            file_name == "judge.py"
            and not agent.get("has_judge", False)
        ):
            continue

        template = (
            platform_root
            / "templates"
            / "worker_agent"
            / f"{file_name}.tpl"
        )

        output = agent_path / file_name

        write_template(template, output, agent_variables)

    if agent.get("has_tools", False):
        tools_path = agent_path / "tools"
        create_init(tools_path)


def create_orchestrator(
    platform_root: Path,
    project_path: Path,
    variables: dict,
) -> None:
    orchestrator_path = (
        project_path
        / "agents"
        / "orchestrator"
    )

    create_init(orchestrator_path)

    nodes_path = orchestrator_path / "nodes"
    create_init(nodes_path)

    for file_name in ORCHESTRATOR_FILES:
        template = (
            platform_root
            / "templates"
            / "orchestrator"
            / f"{file_name}.tpl"
        )

        output = orchestrator_path / file_name

        write_template(template, output, variables)


def create_agents(
    platform_root: Path,
    project_path: Path,
    agents: list[dict],
    variables: dict,
) -> None:
    agents_path = project_path / "agents"
    create_init(agents_path)

    for agent in agents:
        agent_name = agent["name"]
        agent_type = agent.get("type", "worker")

        if (
            agent_name == "orchestrator"
            or agent_type == "supervisor"
        ):
            create_orchestrator(
                platform_root,
                project_path,
                variables,
            )
        else:
            create_worker_agent(
                platform_root,
                project_path,
                agent,
                variables,
            )


def copy_project_yaml(
    project_config_path: Path,
    project_path: Path,
) -> None:
    destination = project_path / "agents.yaml"

    if not destination.exists():
        shutil.copyfile(project_config_path, destination)


def scaffold(
    project_config_path: Path,
    output_dir: Path,
) -> None:
    platform_root = Path(__file__).resolve().parent.parent

    config = read_yaml(project_config_path)

    project = config.get("project", {})

    project_name = project.get(
        "name",
        "generated-agent-project",
    )

    project_description = project.get(
        "description",
        "",
    )

    interfaces = config.get("interfaces", {})

    agents = config.get("agents", [])

    variables = {
        "project_name": project_name,
        "project_description": project_description,
    }

    project_path = output_dir / project_name

    mkdir(project_path)

    copy_root_files(
        platform_root,
        project_path,
    )

    create_root_files(
        project_path,
        project_name,
    )

    copy_project_yaml(
        project_config_path,
        project_path,
    )

    create_shared(
        platform_root,
        project_path,
        variables,
    )

    create_interfaces(
        platform_root,
        project_path,
        interfaces,
        variables,
    )

    create_eval(
        platform_root,
        project_path,
        variables,
    )

    create_agents(
        platform_root,
        project_path,
        agents,
        variables,
    )

    print(
        f"Project scaffolded successfully: "
        f"{project_path}"
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Scaffold an AI-native multi-agent project."
        )
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to agents.yaml",
    )

    parser.add_argument(
        "--output",
        default=".",
        help="Output directory",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    scaffold(
        project_config_path=Path(args.config),
        output_dir=Path(args.output),
    )