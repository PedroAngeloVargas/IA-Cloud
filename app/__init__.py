from flask import Flask
from app.controller.controller import chat_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'segredo'
    app.register_blueprint(chat_bp, url_prefix="/chat")
    return app



