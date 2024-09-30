'''
Q5. Write a Python function that checks if two given strings are anagrams (contain the same 
characters with the same frequencies).
Example: "listen" and "silent" are anagrams.'''


def are_anagrams(str1, str2):
    # Removing spaces and converting to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    # Checking if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)

#input from user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

#using if-else statements to check whether anagram or not
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")