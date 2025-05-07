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
import base64
import os

from utils_streamlit import reset_st_state
from utils_vertex import call_gemini
from configs import MODEL_ID

# Set base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSTEM_INSTRUCTIONS = {
    "Resumo da Anamnese": """
Você é uma especialista médica e faz os melhores resumos para serem armazenados no prontuário eletrônico do paciente.

Sua tarefa é resumir o áudio da anamnese médica.

<Instruções> 
Seu resumo deve conter os seguintes tópicos, formatados em uma tabela:
1) Sintomas: para cada sintoma, informe se é uma melhoria ou piora do paciente, se é possível efeito colateral do medicamento, qual a duração ou desde quando possui os sintomas mencionados, etc.
2) Medicamentos: informe se é um medicamento que paciente já iniciou, quando deve iniciar ou se é uma nova prescrição
3) Resultados dos exames: somente para exames já realizados; para cada exame, informe a conclusão mencionada
4) Recomendações: resuma todos os pedidos de exames, encaminhamentos, procedimentos e consultas que precisarão ser realizados e foram mencionadas na consulta
</Instruções>

<Saída>
Resumo:
</Saída>
"""
}

def load_audio(audio_file):
    """Encode an audio file to base64."""
    return base64.b64encode(audio_file.getvalue()).decode('utf-8')

# Set page configuration
st.set_page_config(
    page_title="Resumo da Anamnese", page_icon="./images/logo.png"
)

if reset := st.button("Reset"):
    reset_st_state()

cols = st.columns([13, 150])
with cols[0]:
    st.image("./images/logo.png")
with cols[1]:
    st.title("Resumo da Anamnese")

st.write(
    """
    A doutora acabou de finalizar a consulta com a paciente e agora precisa escrever sua anamnese. Para facilitar, ela irá gravar um áudio que será processado e armazenado diretamente no prontuário eletrônico. Poderíamos também pensar em gravar a própria consulta. \n
    """
)

st.header("Selecione ou carregue um áudio")
audio_option = st.radio("Selecione ou carregue um áudio:", ('Upload', 'Anamnese.m4a'))

uploaded_audio = None
if audio_option == 'Upload':
    uploaded_audio = st.file_uploader("Audio file", type=['MP3', 'MPGA', 'WAV', 'WEBM', 'M4A', 'OPUS', 'AAC', 'FLAC', 'PCM'])

# Determining the audio source
if uploaded_audio is not None:
    audio_data = uploaded_audio.getvalue()
    st.audio(uploaded_audio)
elif audio_option != 'Upload':
    audio_path = os.path.join(BASE_DIR, "sample_data", audio_option)
    print(audio_path)
    with open(audio_path, "rb") as file:
        audio_data = file.read()
    st.audio(audio_data)
else:
    audio_data = None

# Editable text prompts
st.header("Selecione e edite suas instruções")
system_instructions_option = st.selectbox("Escolha suas instruções:", (SYSTEM_INSTRUCTIONS.keys()))
system_instruction = st.text_area("Edite suas instruções:", value=SYSTEM_INSTRUCTIONS[system_instructions_option], height=200)

# Button to call API
if st.button("Submeter") and audio_data and system_instruction:
    #audio_base64 = load_audio(audio_data)
    with st.spinner("Analisando o áudio, o que pode levar até 90 segundos..."):
        response_markdown = call_gemini(
            model=MODEL_ID,
            system_instructions=system_instruction, 
            audios=[audio_data]
        )
        st.markdown(response_markdown)
    pass
else:
    if audio_data is None or system_instruction is None:
        st.warning("Faça upload de um arquivo de áudio e insira as instruções antes de enviar.")