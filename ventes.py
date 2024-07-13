import json
import os
import time

ventes = []
nomClient = ""
nomArticle=""
qteArticles=0

nom_fichier = "VENTES.json"

if os.path.exists(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        try:
            ventes = json.load(fichier)
        except json.JSONDecodeError:
            ventes = []

def validationNomClient(nomCl):
    global nomClient
    nomClient = nomCl
    while (nomCl.isdigit()):
        print("\nErreur, le nom du client ne peut pas etre un nombre\n")
        nomClient = input("Saisir le nom du client : ")
        nomCl=nomClient

    noms_clients_existants_lower = [noms['Nom Client'].lower() for noms in ventes]
    if nomCl.lower() in noms_clients_existants_lower:
        noms_clients_existants = [noms['Nom Client'] for noms in ventes]
        for i in range(len(noms_clients_existants_lower)):
            if nomCl.lower() == noms_clients_existants_lower[i]:
                nomClient = noms_clients_existants[i]

def validationArticle(nomArt):
    global nomArticle
    nomArticle = nomArt
    while (nomArt.isdigit()):
        print("Erreur, le nom de l'article ne peut pas etre un nombre")
        nomArticle = input("Saisir le nom de l'article : ")
        nomArt=nomArticle

    noms_articles_existants_lower = [noms['Nom Article'].lower() for noms in ventes]
    if nomArt.lower() in noms_articles_existants_lower:
        noms_articles_existants = [noms['Nom Article'] for noms in ventes]
        for i in range(len(noms_articles_existants_lower)):
            if nomArt.lower() == noms_articles_existants_lower[i]:
                nomArticle = noms_articles_existants[i]

def validationQteArticle(qteArt):
    global qteArticles
    qteArticles = qteArt
    while not qteArt.isdigit():
        print("\nErreur, saisissez une valeur entière pour la quantité de l'article\n")
        qteArticles = input("Saisir la quantite de l'article : ")
        qteArt = qteArticles

def enregistrer_vente():
    global nomClient
    global nomArticle
    global qteArticles
    nomClient = input("Saisir le nom du client: ")
    validationNomClient(nomClient)
    nomArticle = input("Saisir le nom de l'article: ")
    validationArticle(nomArticle)
    qteArticles = input("Saisir la quantité: ")
    validationQteArticle(qteArticles)
    datetemps = time.strftime("%Y-%m-%d | %H:%M:%S")
    vente = {"Nom Client": nomClient, "Nom Article": nomArticle, "Quantite": int(qteArticles), "Date": datetemps}
    ventes.append(vente)
    with open(nom_fichier, 'w') as fichier:
        json.dump(ventes, fichier, indent=4)
    print("\nVente enregistrée avec succès\n")

def afficher_ventes():
    for vente in ventes:
        print(vente)

def ventes_par_client():
    global nomClient
    nomClient = input("Saisissez le nom du client : ")
    validationNomClient(nomClient)
    for vente in ventes:
        if nomClient == vente['Nom Client']:
            print(vente)

ventes_par_client()
# afficher_ventes()
# enregistrer_vente()
# print(validationNomClient("GlOdie"))
# print(nomClient)