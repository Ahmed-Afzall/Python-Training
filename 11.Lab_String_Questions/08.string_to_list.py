'''
Q8.Write a Python function that takes a string and returns a list of characters in the string.
Example: If the input is `"hello"`, the output should be `['h', 'e', 'l', 'l', 'o']`.
'''

def string_to_char_list(input_string):
    # Converting the string into a list of characters
    return list(input_string)

#taking input from the user
user_input = input("Enter a string: ")
char_list = string_to_char_list(user_input)
print("List of characters:", char_list)
