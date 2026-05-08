from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

from agents.registry_fetcher.models import RegistryData


class LienabilityInput(BaseModel):
    dados_matricula: RegistryData


class LienabilityOutput(BaseModel):
    penhoravel: bool
    conclusao: Literal[
        "parece_penhoravel",
        "parece_nao_penhoravel",
        "indeterminado",
    ]
    justificativa: str
    riscos: list[str] = Field(default_factory=list)
    grau_confianca: float = Field(ge=0, le=1)


AgentInput = LienabilityInput
AgentOutput = LienabilityOutput
