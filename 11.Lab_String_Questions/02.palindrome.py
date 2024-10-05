'''
Q2.Write a Python function that checks if a given string is a palindrome (reads the same forward and backward).
Example: "madam" is a palindrome, but "hello" is not.
'''
#defining function as palindrome
def palindrome(s):
        # Removing spaces and converting the string to lowercase
    s = s.replace(" ", "").lower()
    return s == s[::-1] #It then compares the string to its reverse (s[::-1]).

#taking input from the user
string = input("Enter a string: ")

#using if else statements to determine palindrome or not
if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
