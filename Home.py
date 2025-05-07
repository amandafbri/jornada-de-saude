import streamlit as st
import utils_streamlit

st.set_page_config(page_title="Jornada de saúde", page_icon="./images/logo.png")

cols = st.columns([12, 85])
with cols[0]:
    st.image("./images/logo.png")
with cols[1]:
    st.title("Jornada de saúde")

st.subheader("Demonstrações")
st.write("Selecione uma página no menu do lado esquerdo para iniciar uma das demonstrações.")
st.write(
    """**1. Resumo anamnese**: Após a consulta médica, é importante resumir as principais informações para serem armazenadas no prontuário.\n
**2. Auditoria de exames**: Com o pedido de exames, entra em ação a auditoria do plano de saúde.
"""
)
