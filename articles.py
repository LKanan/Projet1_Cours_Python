import json
import os

articles = []
nomArt = ""
prixArt = ""
numArt = 1
qteArt = ""
nom_fichier = "ARTICLES.json"

if os.path.exists(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        try:
            articles = json.load(fichier)
        except json.JSONDecodeError:
            articles = []
else:
    articles = []


def validationNomArticle(nomArticle, listArticle):
    global nomArt
    while (nomArticle.isdigit()):
        print("Erreur, le nom de l'article ne peut pas etre un nombre")
        nomArt = input("Saisir le nom de l'article : ")
        nomArticle = nomArt

    for i in listArticle:
        article = list(map(str.lower, list(i['Nom'])))
        if nomArticle.lower() in article:
            print("\nErreur un article du meme nom existe déjà !\n")
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

    # numArt = input("Saisir le numero de l'article : ")
    nomArt = input("Saisir le nom de l'article : ")
    validationNomArticle(nomArt, articles)
    prixArt = input("Saisir le prix de l'article : ")
    validationPrixArticle(prixArt)
    qteArt = input("Saisir la quantite de l'article : ")
    validationQteArticle(qteArt)
    if validationNomArticle(nomArt, articles):
        return articles
    else:
        if not validationNomArticle(nomArt, articles):
            numArt = articles[-1]['Id'] + 1
            articles.append({'Id': numArt, 'Nom': nomArt, 'Prix unitaire': prixArt, 'Quantite': qteArt})
            with open(nom_fichier, 'w') as fichier:
                json.dump(articles, fichier, indent=4)
            return "Article Ajouté avec succès"
        else:
            return "Article deja existant"
