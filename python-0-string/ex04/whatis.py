#!/usr/bin/env python3
import sys
import sys

def main():
    try:
        # Vérifier le nombre d'arguments
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        if len(sys.argv) < 2:
            return  # Aucun argument, terminer le programme

        # Extraire l'argument
        argument = sys.argv[1]

        try:
            # Convertir l'argument en entier
            number = int(argument)
        except ValueError:
            raise AssertionError("argument is not an integer")

        # Vérifier si le nombre est pair ou impair
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        # Afficher uniquement le message d'erreur
        print(e)

if __name__ == "__main__":
    main()








