from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from agents.registry_fetcher.models import RegistryData


class MarketPriceInput(BaseModel):
    dados_matricula: RegistryData
    fonte_configurada: str | None = None


class MarketPriceOutput(BaseModel):
    valor_estimado: float = Field(ge=0)
    moeda: Literal["BRL"] = "BRL"
    fonte: str
    data_consulta: datetime
    grau_confianca: float = Field(ge=0, le=1)
    observacoes: list[str] = Field(default_factory=list)


AgentInput = MarketPriceInput
AgentOutput = MarketPriceOutput
