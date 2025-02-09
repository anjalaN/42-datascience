#!/usr/bin/env python3

def ma_fonction():
    # x est une variable locale
    x = 10
    print("La valeur de x dans la fonction est :", x)

ma_fonction()

# Si on tente d'accéder à x en dehors de la fonction, cela provoque une erreur
# print(x)  # Erreur: NameError: name 'x' is not defined


x = 20  # x est une variable globale

def ma_fonction():
    print("La valeur de x dans la fonction est :", x)  # On accède à la variable globale

ma_fonction()
print("La valeur de x en dehors de la fonction est :", x)


















