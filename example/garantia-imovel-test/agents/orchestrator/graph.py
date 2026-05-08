from langgraph.graph import END, StateGraph

from agents.critic.agent import Critic
from agents.critic.models import CriticInput
from agents.guarantee_decider.agent import GuaranteeDecider
from agents.guarantee_decider.models import GuaranteeDecisionInput
from agents.lienability_analyzer.agent import LienabilityAnalyzer
from agents.lienability_analyzer.models import LienabilityInput
from agents.market_price_researcher.agent import MarketPriceResearcher
from agents.market_price_researcher.models import MarketPriceInput
from agents.registry_fetcher.agent import RegistryFetcher
from agents.registry_fetcher.models import RegistryFetchInput
from .state import GraphState
from .state import GuaranteeRequest


async def registry_fetcher_node(state: GraphState) -> dict:
    request = GuaranteeRequest.model_validate(state["request"])
    output = await RegistryFetcher().run(
        RegistryFetchInput(
            identificador_imovel=request.identificador_imovel,
            numero_matricula=request.numero_matricula,
        )
    )
    return {
        "registry_fetch": output,
        "registry": output.dados_matricula,
        "execution_path": [
            *state.get("execution_path", []),
            "registry_fetcher",
        ],
    }


async def lienability_analyzer_node(state: GraphState) -> dict:
    output = await LienabilityAnalyzer().run(
        LienabilityInput(dados_matricula=state["registry"])
    )
    return {
        "lienability": output,
        "execution_path": [
            *state.get("execution_path", []),
            "lienability_analyzer",
        ],
    }


async def market_price_researcher_node(state: GraphState) -> dict:
    output = await MarketPriceResearcher().run(
        MarketPriceInput(dados_matricula=state["registry"])
    )
    return {
        "market_price": output,
        "execution_path": [
            *state.get("execution_path", []),
            "market_price_researcher",
        ],
    }


async def guarantee_decider_node(state: GraphState) -> dict:
    output = await GuaranteeDecider().run(
        GuaranteeDecisionInput(
            analise_penhorabilidade=state["lienability"],
            pesquisa_preco=state["market_price"],
        )
    )
    return {
        "guarantee_decision": output,
        "execution_path": [
            *state.get("execution_path", []),
            "guarantee_decider",
        ],
    }


async def critic_node(state: GraphState) -> dict:
    output = await Critic().run(
        CriticInput(
            dados_matricula=state["registry"],
            analise_penhorabilidade=state["lienability"],
            pesquisa_preco=state["market_price"],
            decisao_garantia=state["guarantee_decision"],
        )
    )
    return {
        "critic": output,
        "execution_path": [
            *state.get("execution_path", []),
            "critic",
        ],
    }


def build_graph():
    graph = StateGraph(GraphState)

    graph.add_node("registry_fetcher", registry_fetcher_node)
    graph.add_node("lienability_analyzer", lienability_analyzer_node)
    graph.add_node("market_price_researcher", market_price_researcher_node)
    graph.add_node("guarantee_decider", guarantee_decider_node)
    graph.add_node("critic", critic_node)

    graph.add_edge("registry_fetcher", "lienability_analyzer")
    graph.add_edge("lienability_analyzer", "market_price_researcher")
    graph.add_edge("market_price_researcher", "guarantee_decider")
    graph.add_edge("guarantee_decider", "critic")
    graph.add_edge("critic", END)

    graph.set_entry_point("registry_fetcher")

    return graph.compile()
