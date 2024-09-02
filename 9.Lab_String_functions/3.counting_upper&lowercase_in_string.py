# 3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

def count_char_types(input_string):
    # Initializing counters for each type
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0

    # Loop through each character in the string
    for char in input_string:
        # Checking if the character is an uppercase letter
        if char.isupper():
            uppercase_count += 1
        # Checking if the character is a lowercase letter
        elif char.islower():
            lowercase_count += 1
        # Checking if the character is a digit
        elif char.isdigit():
            digit_count += 1
        # If it's not a letter or digit, it's a special character
        else:
            special_count += 1

    # Returning all the counts
    return uppercase_count, lowercase_count, digit_count, special_count

# Asking the user for a string
input_string = input("Enter a string: ")

# Getting the counts for each type of character
uppercase_count, lowercase_count, digit_count, special_count = count_char_types(input_string)

# Output of the results
print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")