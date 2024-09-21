#  1. Write a Python program to Count all letters, digits, and special symbols from the given string

def count_characters(input_string):
    # Initializing counters
    letters = 0
    digits = 0
    special_symbols = 0

    # Loop through each character in the string
    for char in input_string:
        # Checking if the character is a letter (a-z, A-Z)
        if char.isalpha():
            letters += 1
        # Checking if the character is a digit (0-9)
        elif char.isdigit():
            digits += 1
        # If it's neither a letter nor a digit, it's a special symbol
        else:
            special_symbols += 1
    
    # Returning the counts
    return letters, digits, special_symbols

# Asking the user for a string
input_string = input("Enter a string: ")

# Getting the counts of letters, digits, and special symbols
letters, digits, special_symbols = count_characters(input_string)

# Output of the results
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")
