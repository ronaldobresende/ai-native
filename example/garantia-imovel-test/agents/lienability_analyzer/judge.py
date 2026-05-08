from .models import AgentOutput


class LienabilityAnalyzerJudge:
    async def evaluate(self, output: AgentOutput) -> bool:
        validated = AgentOutput.model_validate(output)
        forbidden = [
            "parecer juridico definitivo",
            "garantia juridica definitiva",
        ]

        text = " ".join(
            [validated.justificativa, *validated.riscos]
        ).lower()

        if any(term in text for term in forbidden):
            return False

        return bool(validated.justificativa)
