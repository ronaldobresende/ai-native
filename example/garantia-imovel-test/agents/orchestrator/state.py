from __future__ import annotations

from typing import TypedDict

from pydantic import BaseModel, model_validator

from agents.critic.models import CriticOutput
from agents.guarantee_decider.models import GuaranteeDecisionOutput
from agents.lienability_analyzer.models import LienabilityOutput
from agents.market_price_researcher.models import MarketPriceOutput
from agents.registry_fetcher.models import RegistryData, RegistryFetchOutput


class GuaranteeRequest(BaseModel):
    identificador_imovel: str | None = None
    numero_matricula: str | None = None

    @model_validator(mode="after")
    def require_identifier(self) -> "GuaranteeRequest":
        if not self.identificador_imovel and not self.numero_matricula:
            raise ValueError(
                "Informe identificador_imovel ou numero_matricula."
            )
        return self


class FinalResponse(BaseModel):
    requisicao: GuaranteeRequest
    matricula: RegistryData
    analise_penhorabilidade: LienabilityOutput
    pesquisa_preco: MarketPriceOutput
    decisao_garantia: GuaranteeDecisionOutput
    critica: CriticOutput


class GraphState(TypedDict, total=False):
    request: GuaranteeRequest | dict
    registry_fetch: RegistryFetchOutput | dict
    registry: RegistryData | dict
    lienability: LienabilityOutput | dict
    market_price: MarketPriceOutput | dict
    guarantee_decision: GuaranteeDecisionOutput | dict
    critic: CriticOutput | dict
    execution_path: list[str]
