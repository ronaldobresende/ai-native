from __future__ import annotations

from pydantic import BaseModel, Field

from agents.lienability_analyzer.models import LienabilityOutput
from agents.market_price_researcher.models import MarketPriceOutput


class GuaranteeDecisionInput(BaseModel):
    analise_penhorabilidade: LienabilityOutput
    pesquisa_preco: MarketPriceOutput


class GuaranteeDecisionOutput(BaseModel):
    aceitar_garantia: bool
    justificativa: str
    condicoes: list[str] = Field(default_factory=list)
    alertas: list[str] = Field(default_factory=list)


AgentInput = GuaranteeDecisionInput
AgentOutput = GuaranteeDecisionOutput
