from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]

# Calculer l'IMC
bmi = give_bmi(height, weight)
print(bmi, type(bmi))  # Afficher les valeurs IMC et leur type

# Appliquer la limite
print(apply_limit(bmi, 26))  # Afficher les résultats de la comparaison avec la limite
