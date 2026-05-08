from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

from agents.guarantee_decider.models import GuaranteeDecisionOutput
from agents.lienability_analyzer.models import LienabilityOutput
from agents.market_price_researcher.models import MarketPriceOutput
from agents.registry_fetcher.models import RegistryData


class CriticInput(BaseModel):
    dados_matricula: RegistryData
    analise_penhorabilidade: LienabilityOutput
    pesquisa_preco: MarketPriceOutput
    decisao_garantia: GuaranteeDecisionOutput


class CriticOutput(BaseModel):
    consistente: bool
    contradicoes: list[str] = Field(default_factory=list)
    riscos: list[str] = Field(default_factory=list)
    recomendacao: Literal[
        "prosseguir_com_cautela",
        "revisar_antes_de_responder",
    ]


AgentInput = CriticInput
AgentOutput = CriticOutput
