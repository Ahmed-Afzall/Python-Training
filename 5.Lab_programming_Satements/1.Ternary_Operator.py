# 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd 

'''Ternary Operator: a one-liner conditional expression that allows 
you to write a simple 'if-else' statement in a more concise way'''

# Here we will take input from user
num = int(input("Enter a number: "))

# Ternary operator to determine whether the given number is greater or smaller than 50
result = "Number is Greater than 50" if num > 50 else "Number is smaller than 50"

print(result)