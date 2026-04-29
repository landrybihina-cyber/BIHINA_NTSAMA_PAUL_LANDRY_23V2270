from app import db
from datetime import datetime


class Student(db.Model):
    __tablename__ = 'students'
    id          = db.Column(db.Integer, primary_key=True)
    nom         = db.Column(db.String(100), nullable=False)
    prenom      = db.Column(db.String(100), nullable=False)
    filiere     = db.Column(db.String(100), nullable=False)   # CORR: 'filire' → 'filiere' + 'db.column' → 'db.Column'
    niveau      = db.Column(db.String(20),  nullable=False)   # CORR: 'db.column' → 'db.Column'
    note_math   = db.Column(db.Float,       nullable=True)    # CORR: 'db.column' → 'db.Column', 'db.float' → 'db.Float'
    note_info   = db.Column(db.Float,       nullable=True)    # CORR: idem
    note_anglais= db.Column(db.Float,       nullable=True)    # CORR: idem
    moyenne     = db.Column(db.Float,       nullable=True)    # CORR: idem
    date_ajout  = db.Column(db.DateTime,    default=datetime.utcnow)  # CORR: 'db.column' → 'db.Column', 'db.Datetime' → 'db.DateTime'

    def __repr__(self):                                        # CORR: '_repr__' → '__repr__' (underscore manquant)
        return f'<Student {self.nom} {self.prenom}>'
