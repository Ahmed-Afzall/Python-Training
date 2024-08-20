# 2. Write a python program to check whether a number is palindrome or not? 
# A palindrome is a number or a text phrase that reads the same backwards as forwards. For example 12321 is a palindrome number

number = int(input("Enter a number to check for palindrome: "))
original_number = number
reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")