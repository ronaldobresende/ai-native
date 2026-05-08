from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class RegistryFetchInput(BaseModel):
    identificador_imovel: str | None = None
    numero_matricula: str | None = None

    @model_validator(mode="after")
    def require_identifier(self) -> "RegistryFetchInput":
        if not self.identificador_imovel and not self.numero_matricula:
            raise ValueError(
                "Informe identificador_imovel ou numero_matricula."
            )
        return self


class RegistryOwner(BaseModel):
    nome: str
    documento: str


class RegistryLien(BaseModel):
    tipo: str
    descricao: str
    ativo: bool = True


class RegistryData(BaseModel):
    numero_matricula: str
    identificador_imovel: str
    endereco: str
    cidade: str
    uf: str = Field(min_length=2, max_length=2)
    area_m2: float = Field(gt=0)
    proprietario: RegistryOwner
    status_registral: Literal["regular", "pending_review", "blocked"]
    onus_ativos: list[RegistryLien] = Field(default_factory=list)
    flags_operacionais_mock: list[str] = Field(default_factory=list)
    fonte: str = "mock-registry-api"
    consultado_em: datetime


class RegistryFetchOutput(BaseModel):
    dados_matricula: RegistryData
    observacoes: list[str] = Field(default_factory=list)


AgentInput = RegistryFetchInput
AgentOutput = RegistryFetchOutput
