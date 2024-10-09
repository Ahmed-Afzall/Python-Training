'''
Q9. Write a Python function that takes a digits and characters string and returns a sum of digits in the string.’
Example: If the input is `"Hello World 2345"`, the output should be .= 14
'''

def sum_of_digits(input_string):
    # Initializing sum
    total = 0
    
    # Loop through each character in the string
    for char in input_string:
        # Check if the character is a digit
        if char.isdigit():
            # Convert it to an integer and add it to the total
            total += int(char)
    
    return total

# taking input from user
user_input = input("Enter a string with digits: ")
digit_sum = sum_of_digits(user_input)
print("Sum of digits:", digit_sum)
