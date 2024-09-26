'''
4. Write a Python program to count and display the vowels of a given text
String=”Welcome to python Training”
'''

def count_vowels(s):
    # Defining the vowels
    vowels = 'aeiouAEIOU'
    # Initializing a dictionary to hold vowel counts
    vowel_count = {}
    # Iterating over each character in the string
    for char in s:
        if char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1
    return vowel_count

string = "Welcome to python Training"
print(count_vowels(string))