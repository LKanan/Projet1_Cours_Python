import json
import os

articles = []
nomArt = ""
prixArt = ""
numArt = 1
qteArt = ""

nom_fichier = "ARTICLES.json"
noms_articles_existants=[]

if os.path.exists(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        try:
            articles = json.load(fichier)
        except json.JSONDecodeError:
            articles = []
# else:
#     with open(nom_fichier, 'w') as fichier:
#         articles = fichier


def validationNomArticle(nomArticle):
    global nomArt
    global articles
    while (nomArticle.isdigit()):
        print("Erreur, le nom de l'article ne peut pas etre un nombre")
        nomArt = input("Saisir le nom de l'article : ")
        nomArticle = nomArt

    noms_articles_existants = [noms['Nom'].lower() for noms in articles]
    if nomArticle.lower() in noms_articles_existants:
        return True
    return False


def validationPrixArticle(prixArticle):
    global prixArt
    prix_ok = True
    while (prix_ok):
        try:
            float(prixArticle)
            prix_ok = False
            prixArt = prixArticle
        except:
            prix_ok = True
            print("\nErreur, le prix de l'article doit etre un chiffre\n")
            prixArt = input("Saisir le prix de l'article : ")
            prixArticle = prixArt


def validationQteArticle(qteArticle):
    global qteArt
    while not qteArticle.isdigit():
        print("\nErreur, saisissez une valeur entière pour la quantité de l'article\n")
        qteArt = input("Saisir la quantite de l'article : ")
        qteArticle = qteArt


def ajoutArticle():
    global nomArt
    global prixArt
    global qteArt
    global articles
    global numArt

    nomArt = input("Saisir le nom de l'article : ")
    validationNomArticle(nomArt)
    prixArt = input("Saisir le prix de l'article : ")
    validationPrixArticle(prixArt)
    qteArt = input("Saisir la quantite de l'article : ")
    validationQteArticle(qteArt)
    if not validationNomArticle(nomArt):
        try:
            numArt = articles[-1]['Id'] + 1
        except:
            numArt = 1
        articles.append({'Id': numArt, 'Nom': nomArt, 'Prix unitaire': prixArt, 'Quantite': qteArt})
        with open(nom_fichier, 'w') as fichier:
            json.dump(articles, fichier, indent=4)
        return "\nArticle Ajouté avec succès\n"
    else:
        return "\nErreur un article du meme nom existe déjà !\n"
def visualisation():
    for i in articles:
        noms_articles_existants = [noms['Nom'].lower() for noms in articles]
    print(noms_articles_existants)
