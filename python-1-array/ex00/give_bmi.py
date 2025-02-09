#!/usr/bin/env python3
from typing import List, Union

# Fonction pour calculer l'IMC
def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
    # Vérifier que les deux listes ont la même taille
    if len(height) != len(weight):
        raise ValueError("Les listes height et weight doivent avoir la même taille.")
    
    # Vérifier que les éléments sont bien des nombres (int ou float)
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Les éléments des listes doivent être des entiers ou des flottants.")
    
    # Calculer l'IMC pour chaque pair (taille, poids)
    bmi = []
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)  # Formule de l'IMC
        bmi.append(bmi_value)
    
    return bmi

# Fonction pour appliquer une limite et retourner des booléens
def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    # Vérifier que limit est un entier
    if not isinstance(limit, int):
        raise TypeError("La limite doit être un entier.")
    
    # Appliquer la limite à chaque valeur d'IMC
    result = [b > limit for b in bmi]
    
    return result

from typing import List, Union

# Fonction pour calculer l'IMC
def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
    # Vérifier que les deux listes ont la même taille
    if len(height) != len(weight):
        raise ValueError("Les listes height et weight doivent avoir la même taille.")
    
    # Vérifier que les éléments sont bien des nombres (int ou float)
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Les éléments des listes doivent être des entiers ou des flottants.")
    
    # Calculer l'IMC pour chaque pair (taille, poids)
    bmi = []
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)  # Formule de l'IMC
        bmi.append(bmi_value)
    
    return bmi

# Fonction pour appliquer une limite et retourner des booléens
def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    # Vérifier que limit est un entier
    if not isinstance(limit, int):
        raise TypeError("La limite doit être un entier.")
    
    # Appliquer la limite à chaque valeur d'IMC
    result = [b > limit for b in bmi]
    
    return result

from typing import List, Union

# Fonction pour calculer l'IMC
def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
    # Vérifier que les deux listes ont la même taille
    if len(height) != len(weight):
        raise ValueError("Les listes height et weight doivent avoir la même taille.")
    
    # Vérifier que les éléments sont bien des nombres (int ou float)
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Les éléments des listes doivent être des entiers ou des flottants.")
    
    # Calculer l'IMC pour chaque pair (taille, poids)
    bmi = []
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)  # Formule de l'IMC
        bmi.append(bmi_value)
    
    return bmi

# Fonction pour appliquer une limite et retourner des booléens
def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    # Vérifier que limit est un entier
    if not isinstance(limit, int):
        raise TypeError("La limite doit être un entier.")
    
    # Appliquer la limite à chaque valeur d'IMC
    result = [b > limit for b in bmi]
    
    return result

from typing import List, Union

# Fonction pour calculer l'IMC
def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
    # Vérifier que les deux listes ont la même taille
    if len(height) != len(weight):
        raise ValueError("Les listes height et weight doivent avoir la même taille.")
    
    # Vérifier que les éléments sont bien des nombres (int ou float)
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Les éléments des listes doivent être des entiers ou des flottants.")
    
    # Calculer l'IMC pour chaque pair (taille, poids)
    bmi = []
    for h, w in zip(height, weight):
        bmi_value = w / (h ** 2)  # Formule de l'IMC
        bmi.append(bmi_value)
    
    return bmi

# Fonction pour appliquer une limite et retourner des booléens
def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    # Vérifier que limit est un entier
    if not isinstance(limit, int):
        raise TypeError("La limite doit être un entier.")
    
    # Appliquer la limite à chaque valeur d'IMC
    result = [b > limit for b in bmi]
    
    return result
