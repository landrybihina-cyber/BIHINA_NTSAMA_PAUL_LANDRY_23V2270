from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config  # CORR : Utilisation d'un import relatif (.) pour le package

db = SQLAlchemy()

def create_app():
    # Définition des dossiers templates et static par rapport à la racine du package
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    app.config.from_object(Config)
    db.init_app(app)

    # CORR : Import relatif du Blueprint pour éviter les erreurs de module
    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        # Crée les tables si elles n'existent pas encore
        db.create_all()

    return app