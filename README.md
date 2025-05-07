# Jornada de Saúde

Quer entender melhor como utilizar IA generativa na área de saúde? Confira essa aplicação Streamlit de uma Jornada de Saúde.

## Funcionalidades

- **Resumo anamnese**: Após a consulta médica, é importante resumir as principais informações para serem armazenadas no prontuário.
- **Auditoria de exames**: Com o pedido de exames, entra em ação a auditoria do plano de saúde.

## Pré-requisitos

- Python 3.8 ou acima
- Pacotes Python requisitados (cheque os arquivos `requirements.txt`)

### Caso vá integrar o modelo em Google Cloud
- Projeto do Google Cloud: certifique-se de ter um Projeto do Google Cloud ativo. Se não tiver, você pode criar um no Google Cloud Console.
- Habilite a API do Artifact Registry: no seu projeto, habilite a API do Artifact Registry. Você pode fazer isso por meio do Cloud Console ou da ferramenta de linha de comando gcloud.
- Autenticação: certifique-se de que sua conta de usuário tenha as permissões necessárias para criar recursos no Artifact Registry. A função Artifact Registry Writer deve ser suficiente.

## Instalação

1. Clone o repositório:
```bash
git clone [repository-url]
cd hcls-demo
```

2. Crie um ambiente virtual:
```bash
python3 -m venv .env
source .env/bin/activate
```

3. Instale as dependências Python:
```bash
pip install -r requirements.txt
```

## Uso

### Para uso local do app Streamlit:

1. Rode no terminal:
```bash
[OPCIONAL: python3 -m] streamlit run Home.py --server.port=8080
```

### Usando o app Streamlit no Cloud Run:

```bash
gcloud builds submit --tag gcr.io/[PROJECT_ID]/hcls-demo
```

```bash
gcloud run deploy --image gcr.io/[PROJECT_ID]/hcls-demo --platform managed --region us-central1 --allow-unauthenticated
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

## Licença

Este projeto está licenciado sob a Licença Apache - veja o arquivo LICENSE para mais detalhes.
