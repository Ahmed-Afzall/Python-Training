# 1.Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen. 

def read_file_line_by_line():
    with open('ABC.txt', 'r') as file:
        for line in file:
            print(line, end='')

# Call the function by
read_file_line_by_line()


# 2.Write a function in Python to count and display the total number of words in a text file “ABC.txt”

def count_words_in_file():
    with open('ABC.txt', 'r') as file:
        text = file.read()
        words = text.split()
        word_count = len(words)
        print(f"The total number of words in the file is: {word_count}")

# Call the function by
count_words_in_file()



# 3. Write a function in Python to count uppercase character in a text file “ABC.txt”

def count_uppercase_in_file():
    with open('ABC.txt', 'r') as file:
        text = file.read()
        uppercase_count = sum(1 for char in text if char.isupper())
        print(f"The total number of uppercase characters in the file is: {uppercase_count}")

# Call the function by
count_uppercase_in_file()



# 4. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    # Open the file in read mode
    file = open("Story.txt", "r")
    content = file.read()
    file.close()  # Close the file after reading

    # Split content into a list of words
    words = content.split()

    # Loop through each word and print it if its length is less than 4
    for word in words:
        if len(word) < 4:
            print(word)
#call the function by
display_words()
#these codes are running fine in IDLE only but not in VS code. Might be issue within my PC, will be resolved in future.