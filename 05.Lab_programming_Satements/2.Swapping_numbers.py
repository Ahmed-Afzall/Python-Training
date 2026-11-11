# 2. Using input function take two number and then swap the number 

# Taking two numbers as input from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Swapping the numbers; here num1 value is assigned to num2 and num2 value is assigned to num1
num1, num2 = num2, num1

# Displaying the swapped values
print(f"After swapping the numbers:\nFirst number: {num1}\nSecond number: {num2}")
