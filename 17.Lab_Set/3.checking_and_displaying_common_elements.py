'''3. Write a Python program to Check if two sets have any elements in common. If yes, display the common elements. 
Input: 
set1 = {10, 20, 30, 40, 50} 
set2 = {60, 70, 80, 90, 10} '''

# Defining the sets
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# Finding common elements using intersection
common_elements = set1.intersection(set2)

# Checking if there are common elements and display them
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements")