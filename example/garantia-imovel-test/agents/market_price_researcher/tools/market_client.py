from __future__ import annotations

from datetime import UTC, datetime

from agents.registry_fetcher.models import RegistryData
from shared.settings import settings

from ..models import MarketPriceOutput


class MockMarketPriceClient:
    """Mock interface for a future configurable web price source."""

    async def research(
        self,
        registry: RegistryData,
        source_name: str | None = None,
    ) -> MarketPriceOutput:
        token = registry.identificador_imovel.upper()

        if "LOW" in token:
            estimated_value = 320_000.0
        elif "HIGH" in token:
            estimated_value = 850_000.0
        else:
            estimated_value = max(registry.area_m2 * 6_500.0, 250_000.0)

        confidence = 0.70
        if registry.status_registral != "regular":
            confidence = 0.55

        return MarketPriceOutput(
            valor_estimado=round(estimated_value, 2),
            fonte=source_name
            or settings.market_price_source_name
            or settings.market_price_source_url,
            data_consulta=datetime.now(UTC),
            grau_confianca=confidence,
            observacoes=[
                "Preco estimado por client mockado; sem acesso real a web."
            ],
        )
