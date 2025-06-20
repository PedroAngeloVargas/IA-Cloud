from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.controller.controller import chat_bp
    app.register_blueprint(chat_bp)

    return app
