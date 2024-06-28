import json
produit = []
num_art = 0
prix_art = ''
qte_art = ''
article_existe = False

def testdecimal(valeur):
    try:
        float(valeur)
        return True
    except:
        return False

def validation_prix_qte(prix, qte):
    global prix_art
    global qte_art
    while not testdecimal(prix):
        print("\nErreur de saisie, la valeur du prix doit etre un chiffre svp !")
        prix = input(f"""Prix unitaire
==> """)
        prix_art = prix

    while not qte.isdigit():
        print("\nErreur de saisie, la valeur de la quantité doit etre un entier svp !")
        qte = input(f"""Quantité
==> """)
        qte_art = qte

def ajout_produit():
    global article_existe
    global prix_art
    global qte_art
    global num_art
    num_art += 1
    print("AJOUT DE ARTICLES")
    print("==================")
    nom_art = input(f"""Nom
==> """)
    prix_art = input(f"""Prix unitaire
==> """)
    qte_art = input(f"""Quantité
==> """)
    validation_prix_qte(prix_art, qte_art)

    for i in produit:
        if nom_art in list(i.values()):
            print("Ce produit existe déjà")
            article_existe = 1
            break
    if not article_existe:
        produit.append({'Designation': nom_art, 'Numero': num_art, 'Prix': float(prix_art), 'Quantite': int(qte_art)})
        
        nom_fichier = 'produits.json'
        with open(nom_fichier, 'w') as fichier:
            json.dump(produit, fichier, indent=4)
        return produit
