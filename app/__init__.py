import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    # FORCE le chemin d'instance vers /tmp pour éviter l'erreur Read-only
    app = Flask(__name__, instance_path='/tmp')
    
    if os.environ.get('VERCEL'):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev_key_123'

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app