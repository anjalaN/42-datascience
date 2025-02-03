# #!/usr/bin/env python3


# import sys

# def main():
#     # Step 1: Ensure correct number of arguments and types
#     if len(sys.argv) != 3:
#         raise AssertionError("Program requires exactly two arguments: a string and an integer.")
    
#     # Extract the arguments
#     S = sys.argv[1]
#     try:
#         N = int(sys.argv[2])  # Convert second argument to an integer
#     except ValueError:
#         raise AssertionError("The second argument must be an integer.")
    
#     # Step 2: List comprehension and lambda function to filter words
#     words = S.split()  # Split the string into a list of words
#     result = [word for word in words if (lambda x: len(x) > N)(word)]  # List comprehension with lambda
    
#     # Output the result
#     print(result)

# if __name__ == "__main__":
#     main()

def ft_filter(function, iterable):
      
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))

# Exemple d'utilisation
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
filtered_numbers = ft_filter(is_even, numbers)
print(list(filtered_numbers))  # Résultat attendu : [2, 4, 6]













 




