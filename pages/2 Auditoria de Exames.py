import streamlit as st
import base64
import os
from io import BytesIO
from PIL import Image

from utils_streamlit import reset_st_state
from utils_vertex import call_gemini
from configs import MODEL_ID


# Set base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSTEM_INSTRUCTIONS = {
    "Exames solicitados": """
Você é uma especialista médica brasileira. Transcreva em formato de lista o nome dos exames solicitados no documento.
""",
"Auditoria": """
Você é um auditor de documentos médicos. Confirme os seguintes pontos:
1) Esse documento está assinado?
2) Esse documento está carimbado por uma médica?
3) Qual o nome da médica?
4) Qual o CRM? Ele está completo (precisa ter 6 dígitos numéricos)?
"""
}


def load_image(image_file):
    """Encode an image file to base64."""
    with open(image_file, "rb") as img:
        data = base64.b64encode(img.read()).decode('utf-8')
    return data

# Set page configuration
st.set_page_config(
    page_title="Auditoria de Exames", page_icon="./images/logo.png"
)

if reset := st.button("Reset"):
    reset_st_state()

cols = st.columns([13, 150])
with cols[0]:
    st.image("./images/logo.png")
with cols[1]:
    st.title("Auditoria de Exames")

st.write(
    """
    Agora que a paciente já fez sua consulta, ela precisa realizar seus exames. Com o pedido da doutora, o sistema automaticamente captura tudo o que foi solicitado. \n
    Além disso, o provedor de saúde precisa checar a validade desse documento, algo que é tarefa do time de auditoria. Por exemplo, checar a assinatura e carimbo. \n
    """
)

st.header("Selecione ou carregue uma imagem")
image_option = st.radio("Selecione ou carregue uma imagem:", ('Upload', 'pedido_exame.jpeg'))

uploaded_image = None
if image_option == 'Upload':
    uploaded_image = st.file_uploader("Image file", type=['JPEG', 'PNG'])

# Determining the image source
if uploaded_image is not None:
    image_data = uploaded_image.getvalue()
    st.image(uploaded_image)
elif image_option != 'Upload':
    image_path = os.path.join(BASE_DIR, "sample_data", image_option)
    print(image_path)
    with open(image_path, "rb") as file:
        image_data = file.read()
    st.image(image_data)
else:
    image_data = None

# Editable text prompts
st.header("Selecione e edite suas instruções")
system_instructions_option = st.selectbox("Escolha suas instruções:", (SYSTEM_INSTRUCTIONS.keys()))
system_instruction = st.text_area("Edite suas instruções:", value=SYSTEM_INSTRUCTIONS[system_instructions_option], height=200)

# Button to call API
if st.button("Submeter") and image_data and system_instruction:
    with st.spinner("Analisando a imagem, o que pode levar até 90 segundos..."):
        response_markdown = call_gemini(
            model=MODEL_ID,
            system_instructions=system_instruction, 
            images=[image_data]
        )
        st.markdown(response_markdown)
    pass
else:
    if image_data is None or system_instruction is None:
        st.warning("Faça upload de um arquivo de imagem e insira suas instruções antes de enviar.")
