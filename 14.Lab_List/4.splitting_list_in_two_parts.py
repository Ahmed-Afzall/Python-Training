# Defining the original list and the length for the first part
list = [1, 1, 2, 3, 4, 4, 5, 1]
length_of_first_part = 3 #it is set to 3 which means the first part will contain first 3 elements of original list

# Splitting the list
first_part = list[:length_of_first_part]  # First part / (:) slicing used to split list in two parts
second_part = list[length_of_first_part:]  # Second part

# Printing the results
print("First part:", first_part)
print("Second part:", second_part)