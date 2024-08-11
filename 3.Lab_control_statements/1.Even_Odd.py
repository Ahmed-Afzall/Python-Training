# 1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

# Taking input from the user to enter a number -
number = int(input("Enter a number: "))

# Checking if the number is even or odd by checking if the number is divisible by 2 
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
