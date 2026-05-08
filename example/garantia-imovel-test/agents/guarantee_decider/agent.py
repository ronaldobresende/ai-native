from .models import AgentInput, AgentOutput


class GuaranteeDecider:
    async def run(self, data: AgentInput) -> AgentOutput:
        validated = AgentInput.model_validate(data)
        penhoravel = validated.analise_penhorabilidade.penhoravel
        valor = validated.pesquisa_preco.valor_estimado
        aceitar = penhoravel and valor >= 500_000

        alertas: list[str] = []
        condicoes: list[str] = [
            "Confirmar dados reais antes de qualquer uso operacional.",
            "Substituir tools mockadas por integracoes reais homologadas.",
        ]

        if not penhoravel:
            alertas.append(
                "Regra de teste reprovou a garantia porque penhoravel=false."
            )

        if valor < 500_000:
            alertas.append(
                "Regra de teste reprovou a garantia porque valor_estimado < 500000."
            )

        if aceitar:
            justificativa = (
                "Regra de teste atendida: penhoravel=true e valor_estimado "
                "maior ou igual a 500000."
            )
        else:
            justificativa = (
                "Regra de teste nao atendida: aceitar somente se "
                "penhoravel=true e valor_estimado >= 500000."
            )

        return AgentOutput(
            aceitar_garantia=aceitar,
            justificativa=justificativa,
            condicoes=condicoes,
            alertas=alertas,
        )
