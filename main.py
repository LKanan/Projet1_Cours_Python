produit = []
num_art = 0
prix_art = ''
qte_art = ''
article_existe = False


def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer rapport de ventes")
    print("8. Charger données")
    print("9. Quitter")
    return input("Choisissez une option: ")


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
        produit.append({'Designation': nom_art, 'Numero': num_art, 'Prix': float(prix_art), 'Quantité': int(qte_art)})
        return produit

def main():
    # charger_donnees()
    while True:
        choix = menu_principal()
        if choix == '1':
            # print("interface_ajout_produit")
            print(ajout_produit())
        elif choix == '2':
            # interface_affichage_produits()
            print("interface_affichage_produits")
        elif choix == '3':
            # interface_recherche_produit()
            print("interface_recherche_produit")
        elif choix == '4':
            # interface_enregistrement_vente()
            print("interface_enregistrement_vente")
        elif choix == '5':
            # interface_affichage_ventes()
            print("interface_affichage_ventes")
        elif choix == '6':
            # interface_ventes_par_client()
            print("interface_ventes_par_client")
        elif choix == '7':
            # generer_rapport_ventes()
            print("generer_rapport_ventes")
        elif choix == '8':
            # charger_donnees()
            print("charger_donnees")
        elif choix == '9':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

        print("")


if __name__ == "__main__":
    main()
