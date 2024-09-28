'''Q4. Write a Python function to find all the occurrences of a substring in a given string.
Example: In the string "abracadabra", find all occurrences of the substring "abra".
'''

def substring_occurrences(main_string, substring):
    count = main_string.count(substring) # Counting the number of occurrences
    for _ in range(count):
        print(substring)

# taking input from user
main_string = input("Enter the main string: ")
substring = input("Enter the substring to find: ")
substring_occurrences(main_string, substring)