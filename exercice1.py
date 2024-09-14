"""
Nom du fichier : exercice1.py
Description : Ce fichier contient le programme de l'exercice 1 de l'atelier 4.
Auteur : NDE SOH ARNAULD WILFRIDE
Date : 12 septembre 2024
"""


# Ma fonction somme
def somme_recursive(liste: list[float]) -> float:
    """
    Cette fonction calcule la somme des nombres de la liste
    passée en paramètre de manière recursive.

    :param liste: Une liste de nombre
    :return: La somme des nombres de la liste
    """
    # Si la liste est vide
    if len(liste) <= 0:
        return 0.0

    # Nous effectuons une copie de la liste pour ne pas modifier l'originale
    copie_liste = liste[:]

    # Si la liste contient un seul élément, on le retourne
    if len(copie_liste) == 1:
        return copie_liste[0]

    # Nous additionnons le premier nombre au deuxième,
    # puis nous rappelons la fonction avec la même liste,
    # mais sans le premier nombre
    copie_liste[1] += copie_liste[0]
    return somme_recursive(copie_liste[1:])


# Ma fonction factorielle
def factorielle_recursive(nombre: int) -> int:
    """
    Cette fonction calcule la factorielle d'un nombre donné,
    de manière recursive

    :param nombre: Le nombre dont ont souhait calculer la factorielle
    :return: le resultat
    """

    if nombre > 0:
        return nombre * factorielle_recursive(nombre - 1)
    elif nombre < 0:
        raise ArithmeticError("La factorielle d'un nombre négatif n'est pas calculable! "
                              "Veuillez entrez un nombre positif.")
    else:
        return 1


# Ma fonction longueur
def longueur(lst: list) -> int:
    if len(lst) <= 0:
        return 0
    else:
        return 1 + longueur(lst[1:])


def minimum(lst: list[float]) -> float:
    if len(lst) <= 0:
        raise ValueError("Il n'existe pas de minimum dans une liste vide.")

    if len(lst) == 1:
        return lst[0]

    copie_lst = lst[:]

    if copie_lst[0] < copie_lst[1]:
        copie_lst[1] = copie_lst[0]

    return minimum(copie_lst[1:])


def listPairs(liste: list[int]) -> list[int]:
    if len(liste) <= 0:
        return []

    copie_liste = liste[:]

    


def main():
    # Test de la fonction
    print("1) Somme recursive")
    liste1 = [1.0, 2.0, 3.0, -4.0, 5.0]
    resultat1 = somme_recursive(liste1)
    print("La somme de la liste est :", resultat1)

    liste2 = []
    resultat2 = somme_recursive(liste2)
    print("La somme de la liste est :", resultat2)

    print("2) Factorielle recursive")
    # Test de la fonction
    try:
        nombre = 5
        resultat = factorielle_recursive(nombre)
        print("Le factoriel de", nombre, "est :", resultat)
        nombre1 = 0
        resultat = factorielle_recursive(nombre1)
        print("Le factoriel de", nombre1, "est :", resultat)
        nombre2 = 1
        resultat = factorielle_recursive(nombre2)
        print("Le factoriel de", nombre2, "est :", resultat)
        nombre3 = -1
        resultat = factorielle_recursive(nombre3)
        print("Le factoriel de", nombre3, "est :", resultat)
    except ArithmeticError as ae:
        print("Message :", ae.args)

    print("3) Taille liste recursive")
    lst = []
    print("La taille de la liste est :", longueur(lst))
    lst1 = [0]
    print("La taille de la liste est :", longueur(lst1))
    lst2 = [-1, 16, 25]
    print("La taille de la liste est :", longueur(lst2))

    print("4) Minimum de la liste recursive")
    lst = [-1, 16, 25]
    print("Le minimum de la liste est :", minimum(lst))


if __name__ == "__main__":
    main()
