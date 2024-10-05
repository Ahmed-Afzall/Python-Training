'''
Q3.Write a Python function to count the number of vowels and consonants in a given string.
Example:  In the string "Hello", there are 2 vowels ('e', 'o') and 3 consonants ('H', 'l', 'l').
'''

def count_vowels_consonants(input_string):
    # Defining vowels
    vowels = "aeiouAEIOU"

    # Initialize counters
    vowel_count = 0
    consonant_count = 0

    # Loop through each character in the string
    for char in input_string:
        # Check if the character is an alphabetic letter
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

#taking input from the user
user_input = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(user_input)
print(f"Vowels: {vowels}, Consonants: {consonants}")
