import streamlit as st
import asyncio

from agents.orchestrator.state import GuaranteeRequest
from agents.orchestrator.supervisor import Supervisor


st.set_page_config(page_title="Garantia Imovel Debug", layout="wide")
st.title("Garantia Imovel Debug")

with st.form("debug-form"):
    identificador_imovel = st.text_input(
        "Identificador do imovel",
        value="IMOVEL-HIGH-001",
    )
    numero_matricula = st.text_input("Numero da matricula", value="")
    submitted = st.form_submit_button("Executar")

if submitted:
    request = GuaranteeRequest(
        identificador_imovel=identificador_imovel or None,
        numero_matricula=numero_matricula or None,
    )
    result = asyncio.run(Supervisor().run(request))

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Decisao")
        st.json(result.decisao_garantia.model_dump(mode="json"))
    with col2:
        st.subheader("Critica")
        st.json(result.critica.model_dump(mode="json"))

    st.subheader("Resposta completa")
    st.json(result.model_dump(mode="json"))
