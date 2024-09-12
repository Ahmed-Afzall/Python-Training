# 1. Write a python program to reverse a number using a while loop. 

number = int(input("Enter a number to reverse: "))
reversed_number = 0

while number > 0:
    remainder = number % 10  #The % (modulus) operator is used to get the last digit of the number.

  #The current reversed_number is multiplied by 10 (to shift its digits left) and the remainder (last digit of the original number) is added to it.
    reversed_number = (reversed_number * 10) + remainder  

  #The // (floor division) operator removes the last digit of the original number.
    number = number // 10
print("Reversed Number:", reversed_number)
