# Defining a list
list = [1, 2, 2, 3, 4, 4, 5, 1]

# Creating an empty list to store duplicates
duplicates = []

# Looping through the list
for item in list:
    # Checking if the item appears more than once and is not already in duplicates list
    if list.count(item) > 1 and item not in duplicates:
        duplicates.append(item) # this will append/add the item in duplicate list

# Printing the duplicates
print("Duplicate values:", duplicates)

