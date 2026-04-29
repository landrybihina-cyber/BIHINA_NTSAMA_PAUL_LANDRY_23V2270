import os


class Config:
    SECRET_KEY = 'ma_cle_secrete_2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'      # CORR: espace supprimé après 'sqlite:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False                  # CORR: 'MODIFATIONS' → 'MODIFICATIONS'
