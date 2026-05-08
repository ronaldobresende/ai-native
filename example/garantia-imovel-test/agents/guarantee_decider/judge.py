from .models import AgentOutput


class GuaranteeDeciderJudge:
    async def evaluate(
        self,
        output: AgentOutput,
        *,
        penhoravel: bool,
        valor_estimado: float,
    ) -> bool:
        validated = AgentOutput.model_validate(output)
        expected = penhoravel and valor_estimado >= 500_000
        return validated.aceitar_garantia == expected
