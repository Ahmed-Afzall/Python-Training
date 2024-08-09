#Q.4 Write a program to calculate the greatest of three numbers

# Taking Input of three numbers from user
num1 = float(input("Enter the first number: "))  #taking float here so that it can take both int and decimal values if given by the user
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Checking which number is the greatest
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3

# Printing the greatest number
print("The greatest number is:", greatest)