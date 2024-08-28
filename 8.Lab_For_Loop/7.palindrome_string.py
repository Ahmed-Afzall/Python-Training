# 7. Python program to check if the given string is a palindrome:
def palindrome(s):
    # Removing any spaces and converting to lowercase
    s = s.replace(" ", "").lower()
    # Checking if the string is equal to its reverse
    return s == s[::-1]

# taking input from user
string = input("Enter a string: ")

if palindrome(string):
    print("The string is a palindrome.") # if input given is palindrome, for ex, mom, dad, wow, it will print this
else:
    print("The string is not a palindrome.") # if input given is not palindrome, for ex, mother, father, it will print this