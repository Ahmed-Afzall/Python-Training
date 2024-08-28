# 8. Python program to check if a given number is an Armstrong number:

num = int(input("Enter a number: "))   # Taking input from the user
sum = 0                                # Initializing sum to store the sum of cubes of digits
temp = num                             # Creating a temporary variable to store the original number

while temp > 0:                        # Loop to calculate the sum of cubes of each digit
    digit = temp % 10                  # Getting the last digit of the number
    sum += digit ** 3                  # Adding the cube of the digit to the sum
    temp //= 10                        # Removing the last digit from the number

if num == sum:                         # Checking if the sum of cubes is equal to the original number
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
