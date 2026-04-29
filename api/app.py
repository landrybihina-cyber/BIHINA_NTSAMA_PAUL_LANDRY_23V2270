from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.config import Config                        # CORR: 'Config' avec majuscule (nom correct de la classe)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)               # CORR: 'config' → 'Config' (variable importée)
    db.init_app(app)

    from routes import main                      # CORR: 'from app.routes' → 'from routes' (pas de package app)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
