# 2. Write a Python program to remove duplicate characters of a given string.

def remove_duplicate_words(input_string):
    # Splitting the input string into a list of words
    words = input_string.split()
    
    # Initializing an empty list to store unique words
    unique_words = []
    
    # Loop through each word in the list
    for word in words:
        # If the word is not already in unique_words, add it
        if word not in unique_words:
            unique_words.append(word)
    
    # Joining the unique words back into a single string
    result = ' '.join(unique_words)
    
    # Return the string with duplicate words removed
    return result

# Asking the user for a string
input_string = input("Enter a string: ")

# Getting the string with duplicate words removed
output_string = remove_duplicate_words(input_string)

# Output of the result
print("String after removing duplicate words:", output_string)