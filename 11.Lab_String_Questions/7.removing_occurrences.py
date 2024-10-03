'''
Q7.Write a Python function that removes all occurrences of a specified character from a string.
Example: In the string "balloon", remove all occurrences of "l" to get "baoon".
'''

def remove_character(input_string, char_to_remove):
    # Removing all occurrences of char_to_remove from input_string
    result = input_string.replace(char_to_remove, '')
    return result

#taking input from the user
user_input = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
output = remove_character(user_input, char_to_remove)
print("New string:", output)