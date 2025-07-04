# AgronomIA - ChatBot Especializado em Agronegócio

### 🔥 Resumo do Projeto

O AgronomIA é um chatbot inteligente com interface web, voltado exclusivamente para responder dúvidas e fornecer informações relacionadas à agropecuária e ao agronegócio brasileiro. Ele foi desenvolvido com o intuito de facilitar o acesso a informações confiáveis do setor utilizando RAG, um conceito de alimentar uma IA com uma base de dados para que a mesma responda com maior confiabilidade as informações, assim auxiliando produtores rurais, técnicos e estudantes da área. Além de ser um chatbot para os produtores guardarem informações e adequarem o uso da IA ao seu próprio negócio.

### 🛠️ Tecnologias Utilizadas

💬 Módulo Chatbot (Backend Inteligente)
- Linguagem: Python
- Framework: Flask
- Banco de Dados: MongoDB
Arquivos importantes:
- run.py – Executa o servidor Flask
- controller.py – Manipula lógica do chatbot
- api.py – Integrações com API/Modelos

### 📌 Funcionalidades
✅ Interface web simples e responsiva

✅ Integração com modelo de IA (DeepSeek via OpenRouter)

✅ Armazenamento de perguntas e respostas com MongoDB

✅ Estrutura MVC clara para separação de responsabilidades

✅ Registro de histórico de interações

✅ Cadastro de usuários

✅ Login com autenticação

✅ Restrição de acesso ao chatbot para usuários autenticados

### 🧾 Cadastro e Login (Frontend e Backend Web)
- Linguagens: Python, HTML, CSS, Javascript.
- Banco de Dados: Mysql

### 🎨 Protótipo
- Ferramenta: Figma
Telas disponíveis:
- ChatBot
- Tela de Login
- Tela de Cadastro

### 🧱 Parte da Estrutura do Projeto

```
IA-Cloud/
├── app/                            # Diretório principal da aplicação Flask
│   ├── controller/                 # Camada de controle (intermediário entre view e model)
│   │   └── controller.py           # Define a lógica de roteamento e controle do chatbot
│   ├── model/                      # Camada de dados e integração externa
│   │   ├── api.py                  # Funções para chamada à API do OpenRouter (DeepSeek)
│   │   └── db.py                   # Conexão e operações com o MongoDB
│   ├── static/                     # Arquivos estáticos usados pelo HTML
│   │   ├── css/
│   │   │   └── style.css           # Estilos customizados da interface
│   │   └── img/
│   │       └── pastoevaca.jpg      # Imagem de fundo usada na interface
│   ├── templates/                  # Templates HTML renderizados pelo Flask
│   │   └── index.html              # Página principal da aplicação
│   └── __init__.py                 # Inicializa o app Flask com a estrutura de pastas
│
├── Wireframe                       # Pasta com os prototipos da aplicação
├── terraform                       # Pasta contendo exemplo de infraestrura pra utilizar a aplicação
├── requirements.txt                # Lista de dependências do Python
├── docker-compose                  # Arquivos docker-compose para facilitar a implementação
├── Dockerfile                      # Caso queira transformar a aplicação em imagem docker
├── teste_rag.py                    # Testar funcionamento do RAG
├── run.py                          # Arquivo principal para iniciar o servidor Flask
└── README.md                       # Documentação do projeto (você pediu uma nova versão!)

```

### 👤 Fluxo do Usuário
- O usuário acessa a interface web.
- Realiza o cadastro através de um formulário.
- Após o login, o sistema libera acesso ao chatbot.
- O chatbot recebe perguntas relacionadas ao agronegócio e responde com base em uma base de conhecimento treinada ou embutida no sistema Flask/MongoDB.

### 🔒 Autenticação
- É obrigatória para acessar o chat.
- Usuário e senha são verificados via Flask e armazenados no Mysql
- Segurança básica implementada (a confirmar criptografia e validação).

### 💬 ChatBot
- O bot responde perguntas relacionadas ao agronegócio.
- Utiliza uma base de conhecimento específica.
- Pode usar RAG (Retrieval Augmented Generation) — confirmar se test_rag.py faz isso.

### 📝 Requisitos do Sistema
- Python
- Flask
- MongoDB 
- Gunicorn
- Mysql

### ⚙️ Como Executar Localmente
1. Clone o repositório
```
bash
git clone https://github.com/PedroAngeloVargas/IA-Cloud.git
cd IA-Cloud
```
2. Crie e ative um ambiente virtual
```
bash
python3 -m venv venv
source venv/bin/activate
```
3. Instale as dependências
```
bash
pip install -r requirements.txt
```
4. Configure as variaveis do MongoDB e Mysql
```
client = MongoClient("mongodb://USUARIO_ADMIN:SENHA@banco_mongo/admin")

DB_CONFIG = {
    'host': 'banco_mysql',
    'user': 'SEU_USUARIO',
    'password': 'SUA_SENHA',
    'database': 'usuarios_db'
}
```
5. Entre com sua chave openrouter (Gerar em https://openrouter.ai/)
```
API_KEY = "SEU_TOKEN"
```
6. Faça a execução
```
python3 run.py
```
### 🐳 Docker (opcional)
Se desejar executar com Docker, utlize o Dockerfile e os docker-compose.yml para facilitar o provisionamento.

### ☁️ Terraform
Caso queira utilizar em ambiente Cloud, fica aqui um exemplo de provisionamento de infraestrura na DigitalOcean.
