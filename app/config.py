import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'ff9e85f77a11b23e7ac492859e720092f5b6ac966408aaa18063cff3392aaf82'