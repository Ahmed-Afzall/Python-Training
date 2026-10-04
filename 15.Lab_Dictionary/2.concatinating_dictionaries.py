# Defining multiple dictionaries
dic1 = {"A": 10, "B": 20}
dic2 = {"C": 30, "D": 40}
dic3 = {"E": 50, "F": 60}

# Creating a new dictionary by concatenating the dictionaries
new_dict = {}

# Adding the items from each dictionary to the new dictionary
new_dict.update(dic1) # (.update) method is used to add elements
new_dict.update(dic2)
new_dict.update(dic3)

# Printing the result
print("Concatenated Dictionary:", new_dict)
