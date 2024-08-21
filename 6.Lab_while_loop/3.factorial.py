# 3. Write a python program finding the factorial of a given number using a while loop. 

number = int(input("Enter a number to find its factorial: "))
factorial = 1 #This will eventually hold the factorial of the original number.

while number > 0:
    factorial *= number
    number -= 1

print("Factorial:", factorial)