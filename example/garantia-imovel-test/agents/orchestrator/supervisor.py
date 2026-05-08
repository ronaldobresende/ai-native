from __future__ import annotations

from .graph import build_graph
from .state import FinalResponse, GuaranteeRequest


class Supervisor:
    async def run(self, request: GuaranteeRequest | dict) -> FinalResponse:
        validated_request = GuaranteeRequest.model_validate(request)
        graph = build_graph()
        state = await graph.ainvoke(
            {
                "request": validated_request,
                "execution_path": [],
            }
        )

        return FinalResponse(
            requisicao=validated_request,
            matricula=state["registry"],
            analise_penhorabilidade=state["lienability"],
            pesquisa_preco=state["market_price"],
            decisao_garantia=state["guarantee_decision"],
            critica=state["critic"],
        )

    async def decide(self, state):
        return state
