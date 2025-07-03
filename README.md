# AgronomIA - ChatBot Especializado em Agronegócio

### 📌 Resumo do Projeto

O AgroIA é um chatbot inteligente com interface web, voltado exclusivamente para responder dúvidas e fornecer informações relacionadas à agropecuária e ao agronegócio brasileiro. Ele foi desenvolvido com o intuito de facilitar o acesso a informações confiáveis do setor, auxiliando produtores rurais, técnicos e estudantes da área. Além de ser um chatbot para os produtores guardarem informações.

### 🛠️ Tecnologias Utilizadas

💬 Módulo Chatbot (Backend Inteligente)
- Linguagem: Python
- Framework: Flask
- Banco de Dados: MongoDB
Outros arquivos importantes:
- run.py – Executa o servidor Flask
- controller.py – Manipula lógica do chatbot
- api.py – Integrações com API/Modelos

🧾 Cadastro e Login (Frontend e Backend Web)
- Linguagens: Python, HTML, CSS, Javascript.
- Banco de Dados: Mysql
Funcionalidades:
- Cadastro de usuários
- Login com autenticação
- Restrição de acesso ao chatbot para usuários autenticados

🎨 Protótipo
- Ferramenta: Figma
Telas disponíveis:
- ChatBot
- Tela de Login
- Tela de Cadastro

### 🧱 Parte da Estrutura do Projeto

```
IA-Cloud-main/
│
├── app/                        # Módulo Python (Flask)
│   ├── controller/
│   │   └── controller.py       # Lógica de controle do chat
│   └── models/
│       └── api.py              # Modelos e integração do chat
│
├── run.py                      # Inicializador da aplicação Flask
├── test_rag.py                 # Script de testes (RAG?)
├── README.md                   # Descrição do projeto
├── requirements.txt            # Dependências Python
├── Login.png                   # Protótipo da tela de login
├── Tela de Cadastro.png        # Protótipo da tela de cadastro
├── Chatbot.png                 # Protótipo da tela do chatbot
└── ...                         # Demais arquivos do sistema (PHP)
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
