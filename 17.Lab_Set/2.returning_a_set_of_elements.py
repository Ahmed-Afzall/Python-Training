'''2. Write a Python program to Return a set of elements present in Set A or B, but not both.
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}'''

# Defining the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Getting elements that are in set1 or set2 but not both
unique_items = set1.symmetric_difference(set2)

# Printing the result
print("Elements present in Set A or B, but not both:", unique_items)