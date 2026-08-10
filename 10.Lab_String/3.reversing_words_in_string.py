'''
3. Write a Python program to reverse words in a string
String = “Deeptech Python Training”
'''

def reverse_words(s):
    # Splitting the string into words
    words = s.split()
    # Reversing the list of words
    reversed_words = words[::-1]
    # Joining the reversed list back into a string
    return ' '.join(reversed_words)

string = "Deeptech Python Training"
print(reverse_words(string))