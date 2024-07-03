import json
import os

articles = []
nomArt = ""
prixArt = ""
# numArt = 1
qteArt = ""

nom_fichier = "ARTICLES.json"
noms_articles_existants = []

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
        articles.append({'Id': numArt, 'Nom': nomArt, 'Prix unitaire': float(prixArt), 'Quantite': int(qteArt)})
        with open(nom_fichier, 'w') as fichier:
            json.dump(articles, fichier, indent=4)
        return "\nArticle Ajouté avec succès\n"
    else:
        return "\nErreur un article du meme nom existe déjà !\n"


def visualisation_produits():
    if len(articles) == 0:
        return "\nAucun article enregistsré jusque là !\n"
    else:
        return articles

def rechercher_article(nom_article):
    for i in range(len(articles)):
        if nom_article.lower() == articles[i]['Nom'].lower():
            return (i, articles[i])
    return f"\nL'article {nom_article} n'a pas été trouvé !\n"


def supprimer_article(nom_article):
    if str(rechercher_article(nom_article)[0]).isdigit():
        articles.pop(rechercher_article(nom_article)[0])
        with open(nom_fichier, 'w') as fichier:
            json.dump(articles, fichier, indent=4)
        print("\nArticle supprimé avec succès\n")
        return articles
    else:
        return rechercher_article(nom_article)