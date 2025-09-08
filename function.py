

#cas1: variables discretes univariees
# Calculer les Effectifs Cumulés Croissants (ECC)
def calculer_ecc1(effectifs):
    ecc = []
    cumul = 0
    for eff in effectifs:
        cumul += eff
        ecc.append(cumul)
    return ecc

# Calculer les Fréquences Cumulées Croissantes (FCC)
def calculer_fcc1(effectifs):
    total = 0
    for eff in effectifs:
        total += eff
    
    ecc = calculer_ecc1(effectifs)
    fcc = [eff / total for eff in ecc]
    return fcc


# Afficher le tableau statistique
def afficher_tableau_statistique1(modalites, effectifs):
    ecc = calculer_ecc1(effectifs)
    fcc = calculer_fcc1(effectifs)
    # Calculer le total des effectifs
    total_effectifs = 0
    for eff in effectifs:
        total_effectifs += eff

    print("Modalités: ", end="")
    for mod in modalites:
        print(f"{mod}\t\t", end="")
    print("Total")

    print("Effectifs: ", end="")
    for eff in effectifs:
       
        print(f"{eff}\t\t", end="")
       
    print(total_effectifs)

    print("ECC:       ", end="")
    for e in ecc:
        print(f"{e}\t\t", end="")
    print("-")

    print("FCC:       ", end="")
    for f in fcc:
        print(f"{f:.2f}\t\t", end="")
    print("-")


# Calculer la moyenne
def calculer_moyenne1(modalites, effectifs):
    total = 0
    somme_effectifs = 0
    for i in range(len(modalites)):
        total += modalites[i] * effectifs[i]
        somme_effectifs += effectifs[i]
    return total / somme_effectifs


# Calculer la médiane
def calculer_mediane1(modalites, effectifs):
    fcc = calculer_fcc1(effectifs)
    
    for i in range(len(fcc)):
        if fcc[i] > 0.5:
            return modalites[i]
        elif fcc[i] == 0.5:
            if i + 1 <= len(modalites):
                return (modalites[i] + modalites[i + 1]) / 2
            else:
                return modalites[i]


 # Calculer le premier quartile Q1
def calculer_q11(modalites, effectifs):
    fcc = calculer_fcc1(effectifs)
    
    for i in range(len(fcc)):
        if fcc[i] > 0.25:
            return modalites[i]
        elif fcc[i] == 0.25:
            if i + 1 < len(modalites):
                return (modalites[i] + modalites[i + 1]) / 2
            else:
                return modalites[i]

# Calculer le troisième quartile Q3
def calculer_q31(modalites, effectifs):
    fcc = calculer_fcc1(effectifs)
    
    for i in range(len(fcc)):
        if fcc[i] > 0.75:
            return modalites[i]
        elif fcc[i] == 0.75:
            if i + 1 <= len(modalites):
                return (modalites[i] + modalites[i + 1]) / 2
            else:
                return modalites[i]
               

# Calculer le mode
def calculer_mode1(modalites, effectifs):
    max_effectif = max(effectifs)
    modes = []
    for i in range(len(effectifs)):
        if effectifs[i] == max_effectif:
            modes.append(modalites[i])
    return modes

# Afficher les valeurs centrales
def afficher_valeurs_centrales1(modalites, effectifs):
    moyenne = calculer_moyenne1(modalites, effectifs)
    mediane = calculer_mediane1(modalites, effectifs)
    mode = calculer_mode1(modalites, effectifs)
    print(f"Moyenne: x̄ = {moyenne}")
    print(f"Médiane: Me = {mediane}")
    print(f"Mode: {mode}")

# Calculer la variance
def calculer_variance1(modalites, effectifs):
    moyenne = calculer_moyenne1(modalites, effectifs)
    total = 0
    somme_effectifs = 0
    for i in range(len(modalites)):
        total += effectifs[i] * (modalites[i] - moyenne) ** 2
        somme_effectifs += effectifs[i]
    return total / somme_effectifs


# Calculer l'étendue
def calculer_etendue1(modalites):
    min_val = modalites[0]
    max_val = modalites[0]
    
    for i in range(1, len(modalites)):
        if modalites[i] < min_val:
            min_val = modalites[i]
        if modalites[i] > max_val:
            max_val = modalites[i]
    
    return max_val - min_val

# Afficher les valeurs de dispersion
def afficher_valeurs_dispersion1(modalites, effectifs):
    variance = calculer_variance1(modalites, effectifs)
    ecart_type = variance ** 0.5
    etendue = calculer_etendue1(modalites)
    q1 = calculer_q11(modalites, effectifs)
    q3 = calculer_q31(modalites, effectifs)
    iq = q3 - q1
    
    print(f"Variance: V = {variance}")
    print(f"Écart-type:  σ = {ecart_type}")
    print(f"Étendue: E = {etendue}")
    print(f"Q1 = {q1}")
    print(f"Q3 = {q3}")
    print(f"Distance interquartile (IQ): {iq}")    


#cas2:Variables continues univariees
# Calculer les centres des classes
def calculer_centres2(bornes_inf, bornes_sup):
    centres = []
    for i in range(len(bornes_inf)):
        centre = (bornes_inf[i] + bornes_sup[i]) / 2
        centres.append(centre)
    return centres

# Calculer les densités des classes
def calculer_densites2(bornes_inf, bornes_sup, effectifs):
    densites = []
    for i in range(len(bornes_inf)):
        amplitude = bornes_sup[i] - bornes_inf[i]
        if amplitude== 0:
            densite=0
        else:    
            densite = effectifs[i] / amplitude
        densites.append(densite)
    return densites

# Calculer les Effectifs Cumulés Croissants (ECC)
def calculer_ecc2(effectifs):
    ecc = []
    cumul = 0
    for eff in effectifs:
        cumul += eff
        ecc.append(cumul)
    return ecc

# Calculer les Fréquences Cumulées Croissantes (FCC)
def calculer_fcc2(effectifs):
    total = 0
    for eff in effectifs:
        total += eff
    
    ecc = calculer_ecc2(effectifs)
    fcc = [eff / total for eff in ecc]
    return fcc

# Formater les valeurs pour un affichage centré
def format_value(value, width):
    value_str = str(value)
    total_padding = width - len(value_str)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    return ' ' * left_padding + value_str + ' ' * right_padding

# Afficher le tableau statistique pour les variables continues univariées
def afficher_tableau_statistique2(bornes_inf, bornes_sup, effectifs):
    centres = calculer_centres2(bornes_inf, bornes_sup)
    densites = calculer_densites2(bornes_inf, bornes_sup, effectifs)
    ecc = calculer_ecc2(effectifs)
    fcc = calculer_fcc2(effectifs)
    
    # Calculer le total des effectifs
    total_effectifs = 0
    for eff in effectifs:
        total_effectifs += eff

   # Déterminer la largeur de la colonne la plus large (bornes inférieures + bornes supérieures + 2 espaces)
    max_len = 0
    for i in range(len(bornes_inf)):
        class_str_len = len(f"[{bornes_inf[i]}, {bornes_sup[i]}[")
        if class_str_len > max_len:
            max_len = class_str_len

    # Ajouter deux espaces entre les classes
    max_len += 2

    # Afficher les classes
    print("Classes:  ", end="")
    for i in range(len(bornes_inf)):
        class_str = f"[{bornes_inf[i]}, {bornes_sup[i]}["
        print(format_value(class_str, max_len), end="")
    print("Total")

    # Afficher les effectifs
    print("Effectifs:", end="")
    for eff in effectifs:
        print(format_value(eff, max_len), end="")
    print(f" {total_effectifs}")

    # Afficher les ECC
    print("ECC:      ", end="")
    for e in ecc:
        print(format_value(e, max_len), end="")
    print("-")

    # Afficher les FCC
    print("FCC:      ", end="")
    for f in fcc:
        print(format_value(f"{f:.2f}", max_len), end="")
    print("-")

    # Afficher les centres
    print("Centres:  ", end="")
    for centre in centres:
        print(format_value(centre, max_len), end="")
    print("-")

    # Afficher les densités
    print("Densités: ", end="")
    for densite in densites:
        print(format_value(f"{densite:.2f}", max_len), end="")
    print("-")

# Calculer la moyenne
def calculer_moyenne2(bornes_inf, bornes_sup, effectifs):
    centres = calculer_centres2(bornes_inf, bornes_sup)
    total = 0
    somme_effectifs = 0
    for i in range(len(centres)):
        total += centres[i] * effectifs[i]
        somme_effectifs += effectifs[i]
    return total / somme_effectifs

# Calculer la médiane
def calculer_mediane2(bornes_inf, bornes_sup, effectifs):
    fcc = calculer_fcc2(effectifs)
    
    for i in range(1, len(fcc)):
        if fcc[i - 1] < 0.5 < fcc[i]:
            return bornes_sup[i - 1] + (0.5 - fcc[i - 1]) / (fcc[i] - fcc[i - 1]) * (bornes_sup[i] - bornes_sup[i - 1])

# Calculer le premier quartile Q1
def calculer_q12(bornes_inf, bornes_sup, effectifs):
    fcc = calculer_fcc2(effectifs)
    
    for i in range(1, len(fcc)):
        if fcc[i - 1] < 0.25 < fcc[i]:
            q1 = bornes_sup[i - 1] + (0.25 - fcc[i - 1]) / (fcc[i] - fcc[i - 1]) * (bornes_sup[i] - bornes_sup[i - 1])
            return q1
# Calculer le troisième quartile Q3
def calculer_q32(bornes_inf, bornes_sup, effectifs):
    fcc = calculer_fcc2(effectifs)
    
    for i in range(1, len(fcc)):
        if fcc[i - 1] < 0.75 < fcc[i]:
            q3 = bornes_sup[i - 1] + (0.75 - fcc[i - 1]) / (fcc[i] - fcc[i - 1]) * (bornes_sup[i] - bornes_sup[i - 1])
            return q3

def trouver_classe_modale2(bornes_inf, bornes_sup, effectifs):
    densites = []
    for i in range(len(effectifs)):
        intervalle = bornes_sup[i] - bornes_inf[i]
        if intervalle > 0:  # Eviter division par zéro
            densites.append(effectifs[i] / intervalle)

    if not densites:  # Vérifier si la liste des densités est vide
        raise ValueError("La liste des densités est vide. Vérifiez les bornes et les effectifs fournis.")

    max_densite = densites[0]
    index_classe_modale = 0
    for i in range(1, len(densites)):
        if densites[i] > max_densite:
            max_densite = densites[i]
            index_classe_modale = i

    return index_classe_modale

def calculer_mode2(bornes_inf, bornes_sup, effectifs):
    index_classe_modale = trouver_classe_modale2(bornes_inf, bornes_sup, effectifs)
    
    # Calcul des densités
    densites = []
    for i in range(len(effectifs)):
        intervalle = bornes_sup[i] - bornes_inf[i]
        if intervalle > 0:  # Eviter division par zéro
            densites.append(effectifs[i] / intervalle)

    if index_classe_modale > 0:
        Di = densites[index_classe_modale] - densites[index_classe_modale - 1]
    else:
        Di = densites[index_classe_modale]  # Classe modale est la première classe

    if index_classe_modale < len(densites) - 1:
        D_plus_1 = densites[index_classe_modale] - densites[index_classe_modale + 1]
    else:
        D_plus_1 = densites[index_classe_modale]  # Classe modale est la dernière classe

    ai = bornes_inf[index_classe_modale]
    a_plus_1 = bornes_sup[index_classe_modale]

    mode = ai + (Di / (D_plus_1 + Di)) * (a_plus_1 - ai)
    return mode



def afficher_valeurs_centrales2(bornes_inf, bornes_sup, effectifs):
    moyenne = calculer_moyenne2(bornes_inf, bornes_sup, effectifs)
    mediane = calculer_mediane2(bornes_inf, bornes_sup, effectifs)
    mode = calculer_mode2(bornes_inf, bornes_sup, effectifs)
    
    print(f"Moyenne: x̄ = {moyenne}")
    print(f"Médiane: Me = {mediane}")
    print(f"Mode: {mode}")

    indice_modale = trouver_classe_modale2(bornes_inf, bornes_sup, effectifs)
    classe_modale = f"[{bornes_inf[indice_modale]}, {bornes_sup[indice_modale]}["
    print(f"Classe modale: {classe_modale}")


# Calculer la variance
def calculer_variance2(bornes_inf, bornes_sup, centres, effectifs):
    moyenne = calculer_moyenne2(bornes_inf, bornes_sup, effectifs)
    total = 0
    somme_effectifs = 0
    for i in range(len(centres)):
        total += effectifs[i] * (centres[i] - moyenne) ** 2
        somme_effectifs += effectifs[i]
    return total / somme_effectifs

# Calculer l'étendue
def calculer_etendue2(bornes_inf, bornes_sup):
    min_val = bornes_inf[0]
    max_val = bornes_sup[0]
    
    for i in range(1, len(bornes_inf)):
        if bornes_inf[i] < min_val:
            min_val = bornes_inf[i]
        if bornes_sup[i] > max_val:
            max_val = bornes_sup[i]
    
    return max_val - min_val

# Afficher les valeurs de dispersion
def afficher_valeurs_dispersion2(bornes_inf, bornes_sup, centres, effectifs):
    variance = calculer_variance2(bornes_inf, bornes_sup, centres, effectifs)
    ecart_type = variance ** 0.5
    etendue = calculer_etendue2(bornes_inf, bornes_sup)
    q1 = calculer_q12(bornes_inf, bornes_sup, effectifs)
    q3 = calculer_q32(bornes_inf, bornes_sup, effectifs)
    iq = q3 - q1
    
    print(f"Variance: V = {variance}")
    print(f"Écart-type: σ = {ecart_type}")
    print(f"Étendue: E = {etendue}")
    print(f"Q1 = {q1}")
    print(f"Q3 = {q3}")
    print(f"Distance interquartile (IQ): {iq}")


    #cas 3:Variables discrètes bivariees

def calculer_moyenne3(modalites, effectifs):
    total = 0
    somme_effectifs = 0
    for i in range(len(modalites)):
        total += modalites[i] * effectifs[i]
        somme_effectifs += effectifs[i]
    return total / somme_effectifs


def calculer_variance3(modalites, effectifs):
    moyenne = calculer_moyenne3(modalites, effectifs)
    total = 0
    somme_effectifs = 0
    for i in range(len(modalites)):
        total += effectifs[i] * (modalites[i] - moyenne) ** 2
        somme_effectifs += effectifs[i]
    return total / somme_effectifs

def calculer_ecart_type3(modalites, effectifs):
    variance = calculer_variance3(modalites, effectifs)
    return variance ** 0.5

def calculer_covariance3(modalites1, modalites2, effectifs1, effectifs2):
    # Calcul des moyennes pour chaque variable
    moyenne1 = calculer_moyenne3(modalites1, effectifs1)
    moyenne2 = calculer_moyenne3(modalites2, effectifs2)
    
    # Calcul de l'effectif total commun aux deux variables
    effectif_total = 0
    for effectif in effectifs1:
        effectif_total += effectif  

    # Calcul de la somme des produits des modalités
    somme_produits = 0
    for i in range(len(modalites1)):
        somme_produits += modalites1[i] * modalites2[i]   

    # Calcul de la covariance
    covariance = (somme_produits / effectif_total) - (moyenne1 * moyenne2)
    return covariance



def calculer_droite_regression3(modalites1, modalites2, effectifs1, effectifs2):
    covariance = calculer_covariance3(modalites1, modalites2, effectifs1, effectifs2)
    variance1 = calculer_variance3(modalites1, effectifs1)
    moyenne1 = calculer_moyenne3(modalites1, effectifs1)
    moyenne2 = calculer_moyenne3(modalites2, effectifs2)
    a = covariance / variance1
    b = moyenne2 - a * moyenne1
    return a, b

def calculer_coefficient_correlation3(modalites1, modalites2, effectifs1, effectifs2):
    covariance = calculer_covariance3(modalites1, modalites2, effectifs1, effectifs2)
    ecart_type1 = calculer_ecart_type3(modalites1, effectifs1)
    ecart_type2 = calculer_ecart_type3(modalites2, effectifs2)
    return covariance / (ecart_type1 * ecart_type2)

def afficher_moyennes3(modalites1, effectifs1, modalites2, effectifs2):
    moyenne1 = calculer_moyenne3(modalites1, effectifs1)
    moyenne2 = calculer_moyenne3(modalites2, effectifs2)
    print(f"Moyenne de la première variable: x̄ = {moyenne1}")
    print(f"Moyenne de la deuxième variable: ȳ = {moyenne2}")

def afficher_variance_ecart_type3(modalites1, effectifs1, modalites2, effectifs2):
    variance1 = calculer_variance3(modalites1, effectifs1)
    variance2 = calculer_variance3(modalites2, effectifs2)
    ecart_type1 = calculer_ecart_type3(modalites1, effectifs1)
    ecart_type2 = calculer_ecart_type3(modalites2, effectifs2)
    print(f"Variance de la première variable: V(x)={variance1}")
    print(f"Écart-type de la première variable: σ(x)={ecart_type1}")
    print(f"Variance de la deuxième variable: V(y)={variance2}")
    print(f"Écart-type de la deuxième variable: σ(y)={ecart_type2}")

def afficher_covariance3(modalites1, modalites2, effectifs1, effectifs2):
    covariance = calculer_covariance3(modalites1, modalites2, effectifs1, effectifs2)
    print(f"Covariance entre les deux variables: COV(X,Y) = {covariance}")

def afficher_droite_regression3(modalites1, modalites2, effectifs1, effectifs2):
    a, b = calculer_droite_regression3(modalites1, modalites2, effectifs1, effectifs2)
    print(f"Équation de la droite de régression: y = {a}x + {b}")

def afficher_coefficient_correlation3(modalites1, modalites2, effectifs1, effectifs2):
    coefficient = calculer_coefficient_correlation3(modalites1, modalites2, effectifs1, effectifs2)
    print(f"Coefficient de corrélation: r = {coefficient}")
    if coefficient >= 0.8:
        interpretation = "Forte corrélation positive"
    elif coefficient > 0.5:
        interpretation = "Corrélation positive modérée"
    elif coefficient >= 0.3:
        interpretation = "Faible corrélation positive"
    elif coefficient <= -0.3 and coefficient > -0.6 : 
         interpretation = "Faible corrélation négative"
    elif coefficient < -0.5 and coefficient >-0.9: 
         interpretation = "Corrélation négative modérée"  
    elif coefficient <= -0.8 :
          interpretation = "Forte corrélation négative"  
    else:
        interpretation = " corrélation quasi nulle" 
    print(f"On a une {interpretation}")


#cas 4:Variables continues bivariees
def calcul_effectif_total(effectifs):
    effectif_total = 0
    for e in effectifs:
        effectif_total += e
    return effectif_total    


def calculer_distribution_marginale4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    nb_classes_X = len(bornes_inf_X)
    nb_classes_Y = len(bornes_inf_Y)
    
    distribution_marginale_X = {}
    distribution_marginale_Y = {}
    
    for i in range(nb_classes_X):
        classe_X = (bornes_inf_X[i], bornes_sup_X[i])
        if classe_X not in distribution_marginale_X:
            distribution_marginale_X[classe_X] = 0
        for j in range(nb_classes_Y):
            index = j * nb_classes_X + i
            if index < len(effectifs):
                distribution_marginale_X[classe_X] += effectifs[index]

    for j in range(nb_classes_Y):
        classe_Y = (bornes_inf_Y[j], bornes_sup_Y[j])
        if classe_Y not in distribution_marginale_Y:
            distribution_marginale_Y[classe_Y] = 0
        for i in range(nb_classes_X):
            index = i * nb_classes_Y + j
            if index < len(effectifs):
                distribution_marginale_Y[classe_Y] += effectifs[index]

    N = calcul_effectif_total(effectifs)
    
    return distribution_marginale_X, distribution_marginale_Y, N

def afficher_distribution_marginale4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    distribution_marginale_X, distribution_marginale_Y, N = calculer_distribution_marginale4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    
    
    print("Distribution marginale pour X:")
    print(f"{'Classe':<20}{'Effectifs':<10}")
    for classe, effectif in distribution_marginale_X.items():
        print(f"[{classe[0]}, {classe[1]}[ :          {effectif:<10}")
    
    print("\nDistribution marginale pour Y:")
    print(f"{'Classe':<20}{'Effectifs':<10}")
    for classe, effectif in distribution_marginale_Y.items():
        print(f"[{classe[0]}, {classe[1]}[ :          {effectif:<10}")
    
    print(f"\nEffectif total : {N}")





def calculer_moyennes_marginales4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    nb_classes_X = len(bornes_inf_X)
    nb_classes_Y = len(bornes_inf_Y)
    
    somme_ponderee_X = 0
    effectif_total_X = 0
    somme_ponderee_Y = 0
    effectif_total_Y = 0

    for i in range(nb_classes_X):
        centre_X = (bornes_inf_X[i] + bornes_sup_X[i]) / 2
        for j in range(nb_classes_Y):
            index = j * nb_classes_X + i
            if index < len(effectifs):
                somme_ponderee_X += centre_X * effectifs[index]
                effectif_total_X += effectifs[index]

    for j in range(nb_classes_Y):
        centre_Y = (bornes_inf_Y[j] + bornes_sup_Y[j]) / 2
        for i in range(nb_classes_X):
            index = i * nb_classes_Y + j
            if index < len(effectifs):
                somme_ponderee_Y += centre_Y * effectifs[index]
                effectif_total_Y += effectifs[index]

    moyenne_marginale_X = somme_ponderee_X / effectif_total_X if effectif_total_X != 0 else 0
    moyenne_marginale_Y = somme_ponderee_Y / effectif_total_Y if effectif_total_Y != 0 else 0
    
    return moyenne_marginale_X, moyenne_marginale_Y

def afficher_moyennes_marginales4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    moyenne_marginale_X, moyenne_marginale_Y = calculer_moyennes_marginales4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    
    print(f"Moyenne marginale pour X : x̄ = {moyenne_marginale_X}")
    print(f"Moyenne marginale pour Y : ȳ = {moyenne_marginale_Y}")


def calculer_covariance4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    moyenne_marginale_X, moyenne_marginale_Y = calculer_moyennes_marginales4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    nb_classes_X = len(bornes_inf_X)
    nb_classes_Y = len(bornes_inf_Y)

    covariance = 0
    effectif_total = calcul_effectif_total(effectifs)

    for i in range(nb_classes_X):
        centre_X = (bornes_inf_X[i] + bornes_sup_X[i]) / 2
        for j in range(nb_classes_Y):
            centre_Y = (bornes_inf_Y[j] + bornes_sup_Y[j]) / 2
            index = j * nb_classes_X + i
            if index < len(effectifs):
                covariance += (centre_X - moyenne_marginale_X) * (centre_Y - moyenne_marginale_Y) * effectifs[index]

    covariance /= effectif_total if effectif_total != 0 else 1

    return covariance

def afficher_covariance4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    covariance = calculer_covariance4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    print(f"Covariance entre X et Y : COV(X,Y)= {covariance}")


def calculer_variance4(bornes_inf, bornes_sup, effectifs):
    nb_classes = len(bornes_inf)
    centres = [(bornes_inf[i] + bornes_sup[i]) / 2 for i in range(nb_classes)]
    
    effectif_total = 0
    for e in effectifs:
        effectif_total += e
    
    if effectif_total == 0:
        return 0
    
    somme_centres_effectifs = 0
    for i in range(nb_classes):
        somme_centres_effectifs += centres[i] * effectifs[i]
    
    moyenne = somme_centres_effectifs / effectif_total
    
    variance = 0
    for i in range(nb_classes):
        variance += ((centres[i] - moyenne) ** 2) * effectifs[i]
    
    variance /= effectif_total
    
    return variance

def calculer_droite_regression4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    moyenne_marginale_X, moyenne_marginale_Y = calculer_moyennes_marginales4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    covariance = calculer_covariance4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    variance_X = calculer_variance4(bornes_inf_X, bornes_sup_X, effectifs)

    a = covariance / variance_X if variance_X != 0 else 0
    b = moyenne_marginale_Y - a * moyenne_marginale_X

    return a, b

def afficher_droite_regression4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs):
    a, b = calculer_droite_regression4(bornes_inf_X, bornes_sup_X, bornes_inf_Y, bornes_sup_Y, effectifs)
    print(f"L'équation de la droite de régression est : Y = {a}X + {b}")
