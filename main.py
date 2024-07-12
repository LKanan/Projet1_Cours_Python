from articles import *


def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Enregistrer vente")
    print("5. Afficher ventes")
    print("6. Ventes par client")
    print("7. Générer rapport de ventes")
    print("8. Charger données")
    print("9. Supprimer produit")
    print("10. Quitter")
    return input("Choisissez une option: ")


def main():
    while True:
        choix = menu_principal()
        if choix == '1':
            print("\nAJOUT DES NOUVEAUX ARTICLES")
            print("=============================\n")
            # print(ajoutArticle())
            creer_fichier()
            input("Cliquez sur Entree pour continuer")
        elif choix == '2':
            print("\nPRODUITS EN STOCK")
            print("=================\n")
            afficher_produit()
            # for article in visualisation_produits():
            #     print(article)
            # input("Cliquez sur Entree pour continuer")
        elif choix == '3':
            print("\nRECHERCHER UN PRODUIT")
            print("=======================\n")
            nom_article = input("""Saisissez le nom de l'article à supprimer
==> """)
            # print(rechercher_article(nom_article)[0])
            # input("Cliquez sur Entree pour continuer")
        elif choix == '4':
            # interface_enregistrement_vente()
            print("interface_enregistrement_vente")
            enregistrer_vente()
        elif choix == '5':
            # interface_affichage_ventes()
            print("interface_ajout_produit")
        elif choix == '6':
            # interface_ventes_par_client()
            print("interface_ajout_produit")
            vente_par_client()
        elif choix == '7':
            # generer_rapport_ventes()
            print("interface_ajout_produit")
        elif choix == '8':
            # charger_donnees()
            print("interface_ajout_produit")
        elif choix == '9':
            print("\nSUPPRESSION D'ARTICLES")
            print("========================\n")
            nom_article = input("""Saisissez le nom de l'article à supprimer
==> """)
            # print(supprimer_article(nom_article))
            input("Cliquez sur Entree pour continuer")
        elif choix == '10':
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
