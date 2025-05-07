# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


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