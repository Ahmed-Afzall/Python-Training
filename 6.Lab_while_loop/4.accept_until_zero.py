# 4. Accept numbers using input() function until the user enters 0. 
# If user input 0 then break the while loop and display the sum of all the numbers.

total_sum = 0

'''A while True loop is used here to create an infinite loop, which means
the loop will keep running until it is explicitly stopped using a break statement.'''

while True:
    number = int(input("Enter a number (Enter 0 to stop): "))
    if number == 0:
        break
    total_sum += number

print("Sum of all numbers:", total_sum)