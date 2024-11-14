'''3. Write a Python program to calculate the sum of the numbers in a given tuple. 
Input: tuples_list = [(1, 2), (3, 4), (5, 6)]'''

# Defining the list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Initializing a variable to store the sum
total_sum = 0

# Looping through each tuple in the list
for tuples in tuples_list:
    total_sum += sum(tuples)  # Sum of each tuple and add it to total_sum

# Printing the result
print("Sum of the numbers:", total_sum)