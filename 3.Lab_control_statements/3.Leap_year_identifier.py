# 3. Write a Python program that determines if a given year is a leap year or not.

# taking the input from user to enter a year
year = int(input("Enter a year: "))

# Checking if the year is a leap year or not
if year % 400 == 0:   # this statement checks if the year is divisible by 400. If true, it's a leap year.
    print(f"{year} is a leap year.")

elif year % 100 == 0:  # This statement checks if the year is divisible by 100. If true, it's not a leap year (unless it was divisible by 400, which is already checked).
    print(f"{year} is not a leap year.")

elif year % 4 == 0:    #This statement checks if the year is divisible by 4. If true, it's a leap year.
    print(f"{year} is a leap year.")

else:                  #In this statement if none of the above conditions are met, it's not a leap year.
    print(f"{year} is not a leap year.")  #The f in print(f"{year} is/not a leap year.") is part of an f-string, which stands for "formatted string literal."