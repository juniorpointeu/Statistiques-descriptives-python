from function import *

def afficher_message_bienvenue():
    print("******************************************************** \n")
    print("* Bienvenue dans le programme d'analyse statistique!   * \n")
    print("* Veuillez choisir une option dans le menu ci-dessous. * \n")
    print("******************************************************** \n")

def main():
    afficher_message_bienvenue()
    
    while True:
        print("Menu:")
        print("1 - Variables discrètes univariées")
        print("2 - Variables continues univariées")
        print("3 - Variables discrètes bivariées") 
        print("4 - Variables continues bivariées")
        print("5 - Sortir")
        
        try:
            choix = int(input("Entrez votre choix: "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.\n")
            continue

        if choix == 1:
            while True:
                try:
                    n = int(input("Entrez le nombre de modalités: "))
                    if n <= 0:
                        print("Le nombre de modalités doit être supérieur à 0.\n")
                        continue
                    break
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entier.\n")

            modalites = []
            effectifs = []

            for i in range(n):
                while True:
                    try:
                        modalite = int(input(f"Entrez la modalité {i + 1}: "))
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un nombre entier.\n")

                while True:
                    try:
                        effectif = int(input(f"Entrez l'effectif pour la modalité {modalite}: "))
                        if effectif < 0:
                            print("L'effectif doit être non négatif. Veuillez entrer un effectif valide.\n")
                            continue
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un nombre entier.\n")

                modalites.append(modalite)
                effectifs.append(effectif)

            while True:
                print("Sous-menu:")
                print("1 - Afficher le tableau statistique")
                print("2 - Afficher les valeurs centrales")
                print("3 - Afficher les valeurs de dispersion")
                print("4 - Retour au menu principal")
                
                try:
                    sous_choix = int(input("Entrez votre choix: "))
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entier.\n")
                    continue

                if sous_choix == 1:
                    afficher_tableau_statistique1(modalites, effectifs)
                elif sous_choix == 2:
                    afficher_valeurs_centrales1(modalites, effectifs)
                elif sous_choix == 3:
                    afficher_valeurs_dispersion1(modalites, effectifs)
                elif sous_choix == 4:
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.\n")

        elif choix == 2:
            try:
                n = int(input("Entrez le nombre de classes: "))
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.\n")
                continue
        
            bornes_inf = []
            bornes_sup = []
            effectifs = []

            for i in range(n):
                while True:
                    try:
                        borne_inf = float(input(f"Entrez la borne inférieure de la classe {i + 1}: "))
                        borne_sup = float(input(f"Entrez la borne supérieure de la classe {i + 1}: "))
                        effectif = int(input(f"Entrez l'effectif pour la classe [{borne_inf}, {borne_sup}[: "))
                
                # Vérification des conditions
                        if borne_inf < borne_sup and (len(bornes_inf) == 0 or borne_inf == bornes_sup[-1]):
                            if effectif >= 0:
                                bornes_inf.append(borne_inf)
                                bornes_sup.append(borne_sup)
                                effectifs.append(effectif)
                                break  # Sortir de la boucle si tout est correct
                            else:
                                print("Erreur: L'effectif doit être positif (>= 0).\n")
                        else:
                            print("Erreur: Les bornes doivent être dans l'ordre croissant et la borne inférieure doit être égale à la borne supérieure de la classe précédente.\n")
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer des nombres valides.\n")

            centres = calculer_centres2(bornes_inf, bornes_sup)

            while True:
                print("Sous-menu:")
                print("1 - Afficher le tableau statistique")
                print("2 - Afficher les valeurs centrales")
                print("3 - Afficher les valeurs de dispersion")
                print("4 - Retour au menu principal")
        
                try:
                    sous_choix = int(input("Entrez votre choix: "))
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entier.\n")
                    continue

                if sous_choix == 1:
                    afficher_tableau_statistique2(bornes_inf, bornes_sup, effectifs)
                elif sous_choix == 2:
                    afficher_valeurs_centrales2(bornes_inf, bornes_sup, effectifs)
                elif sous_choix == 3:
                    afficher_valeurs_dispersion2(bornes_inf, bornes_sup, centres, effectifs)
                elif sous_choix == 4:
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.\n")


        elif choix == 3:
            while True:
                try:
                    n = int(input("Entrez le nombre de modalités: "))
                    if n <= 0:
                        print("Le nombre de modalités doit être supérieur à 0.\n")
                        continue
                    break
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entier.\n")

            modalites1 = []
            modalites2 = []
            effectifs1 = []
            effectifs2 = []

            for i in range(n):
                while True:
                    try:
                        modalite1 = int(input(f"Entrez la modalité {i + 1} pour la première variable: "))
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un nombre entier.\n")

                while True:
                    try:
                        effectif1 = int(input(f"Entrez l'effectif pour la modalité {modalite1}: "))
                        if effectif1 < 0:
                            print("L'effectif doit être non négatif. Veuillez entrer un effectif valide.\n")
                            continue
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un nombre entier.\n")

                while True:
                    try:
                        modalite2 = int(input(f"Entrez la modalité {i + 1} pour la deuxième variable: "))
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un nombre entier.\n")

                while True:
                    try:
                        effectif2 = int(input(f"Entrez l'effectif pour la modalité {modalite2}: "))
                        if effectif2 < 0:
                            print("L'effectif doit être non négatif. Veuillez entrer un effectif valide.\n")
                            continue
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer un nombre entier.\n")

                modalites1.append(modalite1)
                effectifs1.append(effectif1)
                modalites2.append(modalite2)
                effectifs2.append(effectif2)

            while True:
                print("Sous-menu:")
                print("1 - Afficher la moyenne des variables")
                print("2 - Afficher la variance et l'écart-type")
                print("3 - Afficher la covariance")
                print("4 - Afficher la droite de corrélation")
                print("5 - Afficher le coefficient de corrélation et conclure")
                print("6 - Retour au menu principal")
                
                try:
                    sous_choix = int(input("Entrez votre choix: "))
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entier.\n")
                    continue

                if sous_choix == 1:
                    afficher_moyennes3(modalites1, effectifs1, modalites2, effectifs2)
                elif sous_choix == 2:
                    afficher_variance_ecart_type3(modalites1, effectifs1, modalites2, effectifs2)
                elif sous_choix == 3:
                    afficher_covariance3(modalites1, modalites2, effectifs1, effectifs2)
                elif sous_choix == 4:
                    afficher_droite_regression3(modalites1, modalites2, effectifs1, effectifs2)
                elif sous_choix == 5:
                    afficher_coefficient_correlation3(modalites1, modalites2, effectifs1, effectifs2)
                elif sous_choix == 6:
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.\n")

        elif choix == 4:
            print("\n LORS DE VOS ENTRÉES,VOUS FIXEREZ TOUJOURS UNE CLASSE DE Y ET VOUS FAITES VARIER LES CLASSES DE X (POUR CHAQUE COMBINAISON)")
            print(" DES QUE LE NOMBRE DE COMBINAISONS AVEC CET CLASSE DE Y FIXÉ EST ENTRÉ,\nVOUS FIXEZ LA CLASSE SUIVANTE DE Y ET VOUS RECOMMENCEZ LE PROCESSUS \n ")
            while True:
                try:
                    n = int(input("Entrez le nombre de classes de X: "))
                    m = int(input("Entrez le nombre de classes de Y: "))
                    if n <= 0 or m <= 0:
                        print("Le nombre de classes doit être supérieur à 0.\n")
                        continue
                    break
                except ValueError:
                    print("Entrée invalide. Veuillez entrer des nombres entiers.\n")

            bornes_inf_X = []
            bornes_sup_X = []
            bornes_inf_Y = []
            bornes_sup_Y = []
            effectifs = []
            combinaisons_XY = set()
            occurences_X = {}
            occurences_Y = {}

            for i in range(n * m):
                while True:
                    try:
                        borne_inf_X = float(input(f"Entrez la borne inférieure de X pour la combinaison {i + 1}: "))
                        borne_sup_X = float(input(f"Entrez la borne supérieure de X pour la combinaison {i + 1}: "))
                        borne_inf_Y = float(input(f"Entrez la borne inférieure de Y pour la combinaison {i + 1}: "))
                        borne_sup_Y = float(input(f"Entrez la borne supérieure de Y pour la combinaison {i + 1}: "))
                        effectif = int(input(f"Entrez l'effectif pour la combinaison {i + 1}: "))

                        # Vérification des conditions pour X et Y
                        if borne_inf_X >= borne_sup_X or borne_inf_Y >= borne_sup_Y:
                            print("Erreur: Les bornes inférieures doivent être inférieures aux bornes supérieures.\n")
                            continue

                        # Vérifier les conditions de continuité et d'occurrences
                        x_class = (borne_inf_X, borne_sup_X)
                        y_class = (borne_inf_Y, borne_sup_Y)

                        if (borne_inf_X, borne_sup_X, borne_inf_Y, borne_sup_Y) in combinaisons_XY:
                            print("Erreur: Cette combinaison de bornes X et Y a déjà été entrée.\n")
                            continue

                        if x_class in occurences_X and occurences_X[x_class] >= m:
                            print(f"Erreur: La classe X {x_class} a déjà été entrée {m} fois.\n")
                            continue

                        if y_class in occurences_Y and occurences_Y[y_class] >= n:
                            print(f"Erreur: La classe Y {y_class} a déjà été entrée {n} fois.\n")
                            continue

                        # Validation des continuités pour X
                        if (i % n > 0) and (i // n == (i - 1) // n) and (borne_inf_X != bornes_sup_X[-1]):
                            print("Erreur: La borne inférieure de X doit être égale à la borne supérieure de la classe X précédente.\n")
                            continue

                        # Validation des continuités pour Y
                        if (i >= n) and (i % n == 0) and (borne_inf_Y != bornes_sup_Y[i - n]):
                            print("Erreur: La borne inférieure de Y doit être égale à la borne supérieure de la classe Y précédente.\n")
                            continue

                        if effectif < 0:
                            print("Erreur: L'effectif doit être positif (>= 0).\n")
                            continue

                        # Enregistrer la combinaison valide
                        combinaisons_XY.add((borne_inf_X, borne_sup_X, borne_inf_Y, borne_sup_Y))
                        bornes_inf_X.append(borne_inf_X)
                        bornes_sup_X.append(borne_sup_X)
                        bornes_inf_Y.append(borne_inf_Y)
                        bornes_sup_Y.append(borne_sup_Y)
                        effectifs.append(effectif)

                        occurences_X[x_class] = occurences_X.get(x_class, 0) + 1
                        occurences_Y[y_class] = occurences_Y.get(y_class, 0) + 1
                        break
                    except ValueError:
                        print("Entrée invalide. Veuillez entrer des nombres valides.\n")

            while True:
                print("Sous-menu:")
                print("1 - Afficher la distribution marginale")
                print("2 - Afficher les moyennes marginales")
                print("3 - Afficher la covariance")
                print("4 - Afficher la droite de régression")
                print("5 - Retour au menu principal")

                try:
                    sous_choix = int(input("Entrez votre choix: "))
                except ValueError:
                    print("Entrée invalide. Veuillez entrer un nombre entier.\n")
                    continue

                if sous_choix == 1:
                    afficher_distribution_marginale4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
                elif sous_choix == 2:
                    afficher_moyennes_marginales4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
                elif sous_choix == 3:
                    afficher_covariance4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
                elif sous_choix == 4:
                    afficher_droite_regression4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
                elif sous_choix == 5:
                    break
                else:
                    print("Choix invalide. Veuillez réessayer.\n")

        elif choix == 5:
            print("Merci d'avoir utilisé le programme d'analyse statistique. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.\n")

                
if __name__ == "__main__":
    main()