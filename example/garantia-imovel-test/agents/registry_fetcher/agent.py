from .models import AgentInput, AgentOutput
from .tools import MockRegistryClient


class RegistryFetcher:
    def __init__(self, client: MockRegistryClient | None = None) -> None:
        self.client = client or MockRegistryClient()

    async def run(self, data: AgentInput) -> AgentOutput:
        validated = AgentInput.model_validate(data)
        registry_data = await self.client.fetch(validated)

        return AgentOutput(
            dados_matricula=registry_data,
            observacoes=[
                "Dados retornados por tool mockada; sem chamada externa real."
            ],
        )
