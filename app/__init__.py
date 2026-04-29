import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    if os.environ.get('VERCEL'):
        # On force l'écriture dans /tmp car c'est le seul endroit autorisé
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    else:
        # En local, on garde ton réglage habituel
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'ta_cle_secrete'

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app