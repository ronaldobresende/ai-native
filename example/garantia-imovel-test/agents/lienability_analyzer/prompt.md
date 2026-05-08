# lienability_analyzer

Analise os dados estruturados da matricula e indique, somente para teste,
se o imovel parece penhoravel.

## Entrada

- `dados_matricula`

## Saida

Retorne `LienabilityOutput` com:

- `penhoravel`
- `conclusao`
- `justificativa`
- `riscos`
- `grau_confianca`

## Restricoes

- Nao emita parecer juridico definitivo.
- Nao acrescente regras juridicas reais.
- Baseie a conclusao apenas nos sinais mockados da matricula.
