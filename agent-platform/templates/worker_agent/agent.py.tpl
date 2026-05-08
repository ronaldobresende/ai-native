from .models import AgentInput, AgentOutput


class {{ agent_class_name }}:
    async def run(self, data: AgentInput) -> AgentOutput:
        raise NotImplementedError(
            "Implement agent logic."
        )