from .models import AgentInput, AgentOutput
from .tools import MockMarketPriceClient


class MarketPriceResearcher:
    def __init__(
        self,
        client: MockMarketPriceClient | None = None,
    ) -> None:
        self.client = client or MockMarketPriceClient()

    async def run(self, data: AgentInput) -> AgentOutput:
        validated = AgentInput.model_validate(data)
        return await self.client.research(
            registry=validated.dados_matricula,
            source_name=validated.fonte_configurada,
        )
