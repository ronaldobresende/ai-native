# garantia-imovel-test

Projeto multi-agente de teste para avaliar garantia de imovel.

## Stack

- Arquitetura supervisor
- LangGraph + LangChain
- Pydantic para contratos
- GPT-4 via Azure usando adaptador para SDK IARA
- Langfuse-ready
- RAGAS-ready
- Streamlit para debug

## Fluxo

`orchestrator` chama:

1. `registry_fetcher`
2. `lienability_analyzer`
3. `market_price_researcher`
4. `guarantee_decider`
5. `critic`

As integracoes externas sao mockadas. Nao ha chamada real para APIs, web ou
LLM no fluxo de teste.

## Teste local

```powershell
cd projects/garantia-imovel-test
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
python scripts/run_sample.py
```

Interface Streamlit:

```powershell
streamlit run interfaces/streamlit.py
```

API:

```powershell
uvicorn interfaces.api:app --reload
```

Exemplos de entrada:

- `IMOVEL-HIGH-001`: deve aceitar pela regra de teste.
- `IMOVEL-LOW-001`: deve rejeitar por valor abaixo de 500000.
- `IMOVEL-BLOQ-HIGH-001`: deve rejeitar por `penhoravel=false`.

## Regra de teste

Aceitar garantia somente se:

- `penhoravel = true`
- `valor_estimado >= 500000`

Nenhuma regra juridica real foi implementada.
