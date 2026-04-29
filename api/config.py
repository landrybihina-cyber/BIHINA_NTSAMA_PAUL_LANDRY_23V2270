import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'      # CORR: espace supprimé après 'sqlite:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False                  # CORR: 'MODIFATIONS' → 'MODIFICATIONS'
