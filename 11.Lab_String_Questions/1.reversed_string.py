'''
Q1.Write a Python function that takes a string as input and returns the reversed string.
Example: If the input is "Hello World", the output should be "dlroW olleH".
'''

#defining function
def reversing(s):
    return s[::-1]
#s[::-1] uses Python's slice notation to reverse the string means start from the end towards the first element with a step of -1 (reverse).

actual_string = input("Enter a String:") 
reversed_string = reversing(actual_string)
print(reversed_string)