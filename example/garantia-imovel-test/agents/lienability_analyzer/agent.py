from .models import AgentInput, AgentOutput


class LienabilityAnalyzer:
    async def run(self, data: AgentInput) -> AgentOutput:
        validated = AgentInput.model_validate(data)
        registry = validated.dados_matricula

        blocking_flags = [
            flag
            for flag in registry.flags_operacionais_mock
            if flag
            in {
                "bloqueio_operacional_mock",
                "pendencia_cadastral_mock",
            }
        ]

        penhoravel = (
            registry.status_registral == "regular"
            and not blocking_flags
        )

        riscos: list[str] = [
            "Analise de teste; nao substitui revisao juridica.",
        ]

        if registry.onus_ativos:
            riscos.append(
                "Matricula mockada contem onus ativo; revisar antes de usar."
            )

        if blocking_flags:
            riscos.append(
                "Flags operacionais mockadas indicam restricao para teste."
            )

        if penhoravel:
            conclusao = "parece_penhoravel"
            justificativa = (
                "No cenario de teste, a matricula esta regular e sem flags "
                "operacionais mockadas impeditivas."
            )
            confidence = 0.74
        elif registry.status_registral == "pending_review":
            conclusao = "indeterminado"
            justificativa = (
                "No cenario de teste, a matricula possui pendencia mockada "
                "e deve ser tratada como indeterminada."
            )
            confidence = 0.52
        else:
            conclusao = "parece_nao_penhoravel"
            justificativa = (
                "No cenario de teste, ha status ou flags mockadas que "
                "impedem a classificacao como penhoravel."
            )
            confidence = 0.68

        return AgentOutput(
            penhoravel=penhoravel,
            conclusao=conclusao,
            justificativa=justificativa,
            riscos=riscos,
            grau_confianca=confidence,
        )
