# market_price_researcher

Pesquise o preco aproximado do imovel usando somente o client mockado.

## Entrada

- `dados_matricula`
- `fonte_configurada`

## Saida

Retorne `MarketPriceOutput` com valor estimado, fonte, data da consulta
e grau de confianca.

## Restricoes

- Nao faca chamada real a internet.
- A fonte deve ser configuravel para futura integracao.
- Deixe claro quando o valor for mockado.
