'''
2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n"
'''

def remove_newlines(s):
    # Using the replace method to remove newline characters
    return s.replace('\n', '')

string = "\nBest \nDeeptech \nPython \nTraining\n"
print(remove_newlines(string))