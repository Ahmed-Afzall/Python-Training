'''1. Write a Python program to Get Only unique items from two sets. 
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}'''

# Defining the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Combining both sets to get unique items (duplicates will automatically be removed)
unique_items = set1.union(set2)

# Printing the result
print("Unique items from both sets:", unique_items)