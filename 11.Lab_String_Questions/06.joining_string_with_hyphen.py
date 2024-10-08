'''
Q6.Write a Python function that splits a string into a list of words and then joins the list back 
into a single string with hyphens (-) between the words.
Example: If the input is "Python is fun", the output should be "Python-is-fun".
'''

def split_and_replace(input_string):
    # Splitting the string by spaces
    parts = input_string.split()
    # Joining the parts with hyphens
    result = '-'.join(parts)
    return result

#taking input from user
user_input = input("Enter a string: ")
output = split_and_replace(user_input)
print("New string:", output)
