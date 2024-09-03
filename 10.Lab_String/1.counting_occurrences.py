'''
1. Write a Python program to count the occurrences of each word in a given sentence
string = “To change the overall look of your document. To change the look available in the gallery”
'''

string = "To change the overall look of your document. To change the look available in the gallery"

# Converting the string to lowercase and split into words
words = string.lower().replace('.', '').split()

# Creating a dictionary to count occurrences
word_count = {}

# Counting each word's occurrences
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Displaying the result
print("Word counts:", word_count)