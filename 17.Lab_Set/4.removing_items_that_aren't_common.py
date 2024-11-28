'''4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} '''

# Defining the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Using intersection_update to retain only the common items in set1
set1.intersection_update(set2)

# Printing the modified set1
print("Items common to both sets:", set1)