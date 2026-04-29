from . import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    id           = db.Column(db.Integer, primary_key=True)
    nom          = db.Column(db.String(100), nullable=False)
    prenom       = db.Column(db.String(100), nullable=False)
    filiere      = db.Column(db.String(100), nullable=False)
    niveau       = db.Column(db.String(20),  nullable=False)
    note_math    = db.Column(db.Float,       nullable=True)
    note_info    = db.Column(db.Float,       nullable=True)
    note_anglais = db.Column(db.Float,       nullable=True)
    moyenne      = db.Column(db.Float,       nullable=True)
    date_ajout   = db.Column(db.DateTime,    default=datetime.utcnow)

    def __repr__(self):
        return f'<Student {self.nom} {self.prenom}>'