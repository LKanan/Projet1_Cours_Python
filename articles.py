import json
import os

nomArt = ""
prixArt = ""
# numArt = 1
qteArt = ""


nom_fichier = "ARTICLES.json"
nom_fichier_ventes = 'ventes.json'
article_vendus = []
noms_articles_existants = []

# fonction de chargement de donnée
def chargement_donnee():
    if os.path.exists(nom_fichier):
        with open(nom_fichier, 'r') as fichier:
            try:
                articles = json.load(fichier)
            except json.JSONDecodeError:
                articles = []

    if os.path.exists(nom_fichier_ventes):
        with open(nom_fichier_ventes, 'r') as fichier:
            try:
                ventes = json.load(fichier)
            except json.JSONDecodeError:
                ventes = []
    
    return { 'articles' :articles, 'ventes' :ventes }

# fonction de creation du fichier contenant les ventes
def creer_fichier_vente():
    with open(nom_fichier_ventes, 'w') as fichier :
        pass


# fonction d'enregistrement de vente
def enregistrer_vente():
    donnee = chargement_donnee()
    
    if not(os.path.exists(nom_fichier_ventes)):
        creer_fichier_vente()
    
    nomClient = input('veiller saisir le nom du client : ')
    idProduit = int(input("Veiller entrer l'id du produit : "))
    quantite = int(input('Entrer la quantité : '))

    for article in donnee['articles']:
        if article['Id'] == idProduit :
            article_vendus.append({'Id-Vente': 1,'Nom-Client': nomClient,'Nom': article['Nom'], 'Prix Unitaire': article['Prix unitaire'], 'Quantite': article['Quantite'], "Prix D'achat" : article['Prix unitaire'] * quantite})

    with open(nom_fichier_ventes, 'w') as fichier:
        json.dump(article_vendus, fichier, indent=4)

# fonctionnalite pour afficher toute les ventes
def afficher_ventes():
    donnee = chargement_donnee()
    print(donnee['ventes'])


# fonctionnalite pour afficher les ventes d'un client
def vente_par_client():
    donnee = chargement_donnee()
    nomClient = input('veiller entrer le nom du client : ')

    for article in donnee['ventes']:
        if article['Nom-Client'] == nomClient :
            print(article)




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


# fonction pour ajouter des produits
def ajoutArticle():
    global nomArt
    global prixArt
    global qteArt
    global articles
    global numArt

    donnee = chargement_donnee()
    articles = donnee['articles']    

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
    
def afficher_produits():
    donnee = chargement_donnee()
    articles = donnee['articles']

    print(articles)