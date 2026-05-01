import sys
import os

# Ajoute le dossier racine au chemin de recherche pour que 'app' soit reconnu comme un module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

app = create_app()
if __name__ == "__main__":
    print("Static path:", app.static_folder)
    app.run(debug=True)
    