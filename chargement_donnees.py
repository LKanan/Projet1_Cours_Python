import os
import json

def charger_donnees(nom_fichier):
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            try:
                contenu_fichier = json.load(fichier)
                return contenu_fichier
            except json.JSONDecodeError:
                return []
    else:
        return []