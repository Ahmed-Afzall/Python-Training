'''1. Write a Python program to find the number of times 4 appears in the tuple. 
Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) '''

# Defining the tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Using the count() method to find how many times 4 appears
count_of_4 = tuplex.count(4)

# Printing the result
print("Number of times 4 appears is", count_of_4)