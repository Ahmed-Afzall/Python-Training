# 4. Write a Python Count vowels in a string 

def count_vowels(input_string):
    # Defining a set of vowels (both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    
    # Initializing a counter for vowels
    vowel_count = 0

    # Loop through each character in the string
    for char in input_string:
        # If the character is a vowel, incrementing the counter
        if char in vowels:
            vowel_count += 1
    
    # Returning the total number of vowels
    return vowel_count

# Asking the user for a string
input_string = input("Enter a string: ")

# Getting the total count of vowels in the string
vowel_count = count_vowels(input_string)

# Output of the result
print(f"Total vowels are: {vowel_count}")
