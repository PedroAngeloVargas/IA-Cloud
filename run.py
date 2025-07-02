from flask import Flask, request, redirect, url_for, render_template, session, jsonify
import mysql.connector
import requests
from app.models.api import send_message_to_openrouter
from app.utils.auth import login_required  # ✅ correto
import os



# Diretório base (onde está este arquivo run.py)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Caminhos para templates e static
template_dir = os.path.join(base_dir, 'app', 'templates')
static_dir = os.path.join(base_dir, 'app', 'static')

# Criação do app com ambos os diretórios configurados
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = 'segredo'

# --------------------------- CONFIGURAÇÃO BANCO ---------------------------
DB_CONFIG = {
    'host': '172.17.0.2',
    'user': 'root',
    'password': '12345',
    'database': 'usuarios_db'
}

# --------------------------- CONEXÃO E CRIAÇÃO ---------------------------
def inicializar_banco():
    conn = mysql.connector.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS usuarios_db")
    cursor.execute("USE usuarios_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255),
            cpf VARCHAR(14),
            data_nascimento VARCHAR(20),
            email VARCHAR(255) UNIQUE,
            senha VARCHAR(255)
        );
    """)
    conn.commit()
    conn.close()

inicializar_banco()

# --------------------------- CHAT API ---------------------------
API_KEY = "SUA_CHAVE_DA_OPENROUTER"
MODEL = "deepseek-ai/deepseek-chat"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def enviar_para_deepseek(pergunta):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": pergunta}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erro: {str(e)}"

# --------------------------- ROTAS ---------------------------

@app.route("/", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pessoas WHERE email = %s AND senha = %s", (email, senha))
        usuario = cursor.fetchone()
        conn.close()

        if usuario:
            session["usuario"] = usuario["nome"]
            return redirect(url_for("chat"))
        else:
            msg = "E-mail ou senha inválidos."

    return render_template("login.html", mensagem=msg)

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    msg = ""
    if request.method == "POST":
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        data = request.form["data"]
        email = request.form["email"]
        senha = request.form["senha"]

        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pessoas (nome, cpf, data_nascimento, email, senha)
                VALUES (%s, %s, %s, %s, %s)
            """, (nome, cpf, data, email, senha))
            conn.commit()
            conn.close()
            msg = "Cadastro realizado com sucesso!"
        except mysql.connector.Error as e:
            msg = f"Erro ao cadastrar: {e}"

    return render_template("cadastro.html", mensagem=msg)

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "usuario" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        pergunta = request.json.get("mensagem")
        resposta = send_message_to_openrouter(pergunta)  # Mongo registra tudo
        return jsonify({"mensagem": resposta})

    return render_template("chat.html", usuario=session["usuario"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# --------------------------- EXECUÇÃO ---------------------------
if __name__ == "__main__":
    app.run(debug=True)
