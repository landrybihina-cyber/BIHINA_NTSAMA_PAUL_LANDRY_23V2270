import os

class Config:
    # Utilise une base SQLite locale pour le développement
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False