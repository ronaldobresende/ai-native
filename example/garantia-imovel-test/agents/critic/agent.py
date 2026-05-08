from .models import AgentInput, AgentOutput


class Critic:
    async def run(self, data: AgentInput) -> AgentOutput:
        validated = AgentInput.model_validate(data)
        lienability = validated.analise_penhorabilidade
        price = validated.pesquisa_preco
        decision = validated.decisao_garantia

        contradictions: list[str] = []
        risks: list[str] = []

        expected_acceptance = (
            lienability.penhoravel and price.valor_estimado >= 500_000
        )

        if decision.aceitar_garantia != expected_acceptance:
            contradictions.append(
                "Decisao de garantia diverge da regra de teste."
            )

        if decision.aceitar_garantia and not lienability.penhoravel:
            contradictions.append(
                "Garantia aceita apesar de penhoravel=false."
            )

        if decision.aceitar_garantia and price.valor_estimado < 500_000:
            contradictions.append(
                "Garantia aceita com valor_estimado abaixo de 500000."
            )

        if price.grau_confianca < 0.6:
            risks.append("Preco estimado tem baixo grau de confianca.")

        risks.extend(lienability.riscos)

        consistent = not contradictions

        return AgentOutput(
            consistente=consistent,
            contradicoes=contradictions,
            riscos=risks,
            recomendacao=(
                "prosseguir_com_cautela"
                if consistent
                else "revisar_antes_de_responder"
            ),
        )
