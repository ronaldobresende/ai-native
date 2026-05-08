from __future__ import annotations

from datetime import UTC, datetime

from ..models import (
    RegistryData,
    RegistryFetchInput,
    RegistryLien,
    RegistryOwner,
)


class MockRegistryClient:
    """Mock interface for a future real estate registry API integration."""

    async def fetch(self, query: RegistryFetchInput) -> RegistryData:
        token = (
            query.numero_matricula
            or query.identificador_imovel
            or "IMOVEL-DEMO"
        ).upper()

        status = "regular"
        flags: list[str] = []
        liens: list[RegistryLien] = []

        if "BLOQ" in token:
            status = "blocked"
            flags.append("bloqueio_operacional_mock")

        if "PEND" in token:
            status = "pending_review"
            flags.append("pendencia_cadastral_mock")

        if "ONUS" in token:
            liens.append(
                RegistryLien(
                    tipo="onus_mock",
                    descricao="Registro mockado de onus ativo para teste.",
                )
            )

        area_m2 = 90.0
        if "LOW" in token:
            area_m2 = 45.0
        if "HIGH" in token:
            area_m2 = 130.0

        return RegistryData(
            numero_matricula=query.numero_matricula or f"MAT-{token}",
            identificador_imovel=query.identificador_imovel or f"ID-{token}",
            endereco="Rua de Teste, 100",
            cidade="Sao Paulo",
            uf="SP",
            area_m2=area_m2,
            proprietario=RegistryOwner(
                nome="Pessoa de Teste",
                documento="000.000.000-00",
            ),
            status_registral=status,
            onus_ativos=liens,
            flags_operacionais_mock=flags,
            consultado_em=datetime.now(UTC),
        )
