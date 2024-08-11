# 2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# taking input from the user to enter their age
age = int(input("Enter your age: "))

# Checking if the person is 18 or older by using if statements

if age >= 18:  #if the user's age is greater or equal than 18, it will print "You are eligible to vote"
    print("You are eligible to vote.")
    
else:          #in else if the users age is less then 18, then it will print "You are not eligible to vote"
    print("You are not eligible to vote.")
