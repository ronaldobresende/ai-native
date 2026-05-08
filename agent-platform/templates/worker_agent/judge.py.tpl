from .models import AgentOutput


class {{ agent_class_name }}Judge:
    async def evaluate(self, output: AgentOutput) -> bool:
        """
        Local LLM-as-a-Judge placeholder.

        Replace this logic with semantic validation rules
        or an LLM-based judge call.
        """
        return True