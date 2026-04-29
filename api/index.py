import sys
import os

# Ajoute le dossier racine au chemin de recherche de Python
# pour que le module 'app' puisse être importé correctement
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

# Vercel a besoin d'un objet nommé 'app' (ou configuré via vercel.json)
app = create_app()

# Optionnel : pour les tests locaux directs
if __name__ == '__main__':
    app.run(debug=True)