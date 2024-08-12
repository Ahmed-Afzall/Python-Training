# 5.Write a Python program that determines the largest of three numbers entered by the user.

# thaking input from the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# determining the largest number out of three
if num1 >= num2 and num1 >= num3:    #if number 1 is greater or equal to number 2 and number 3, then number 1 is largest.
    largest = num1
elif num2 >= num1 and num2 >= num3:  #if number 2 is greater or equal to number 1 and number 3, then number 2 is largest.
    largest = num2
else:
    largest = num3                   #else number 3 is the largest.

# Printing the largest number out of three
print(f"The largest number is {largest}.")