#### Fonction secondaire
"""
Ce module contient une fonction pour vérifier si une chaîne de caractères est un palindrome,
en ignorant les accents, les espaces et la casse.

Il inclut également une fonction principale pour tester cette vérification avec quelques
exemples de chaînes de caractères.
"""

def ispalindrome(p):
    """
    Vérifie si une chaîne de caractères est un palindrome, en ignorant les accents,
    les espaces et la casse.

    Cette fonction remplace les caractères accentués par leurs équivalents non accentués,
    convertit la chaîne en minuscules, puis supprime les espaces et les caractères
    non alphanumériques. Elle compare ensuite la chaîne traitée avec son inverse pour
    déterminer si elle est un palindrome.

    Args:
        p (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    noaccent = str.maketrans("àéèçùîïäâêôë", "aeecuiiaaeoe")
    p = p.replace(" ", "").lower()
    p = p.translate(noaccent)
    p = "".join(char for char in p if char.isalnum())
    return p == p[::-1]

#### Fonction principale


def main():
    """
    Fonction principale pour tester la fonction ispalindrome avec quelques exemples.

    Cette fonction vérifie plusieurs chaînes de caractères pour déterminer si chacune
    d'elles est un palindrome, et imprime le résultat pour chaque chaîne.
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
