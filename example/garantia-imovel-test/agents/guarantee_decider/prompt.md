# guarantee_decider

Decida se o imovel pode ser aceito como garantia usando somente a regra
de teste definida para este projeto.

## Entrada

- `analise_penhorabilidade`
- `pesquisa_preco`

## Regra de teste

Aceitar somente se:

- `penhoravel = true`
- `valor_estimado >= 500000`

## Saida

Retorne `GuaranteeDecisionOutput`.

## Restricoes

- Nao adicione outras regras juridicas, comerciais ou de credito.
- Explique a decisao como regra de teste.
