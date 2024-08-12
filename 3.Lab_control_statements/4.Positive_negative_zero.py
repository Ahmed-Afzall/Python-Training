# 4. Create a Python program that checks if a user-given number is positive, negative, or zero.

# taking input from the user to enter a number
number = float(input("Enter a number: "))

# Checking if the number is positive, negative, or zero
if number > 0:  # if number is greator than 0, it is positve
    print("The number is positive.")
elif number < 0:  #  if number is less than 0, it is negative
    print("The number is negative.")
else:            # else it is 0.
    print("The number is zero.")
