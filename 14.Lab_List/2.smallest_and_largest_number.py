# Defining a list
list = [5, 1, 9, 3, 7]

# Setting the first element as the initial largest and smallest
largest = list[0]
smallest = list[0]

# Looping through the list to find the largest and smallest
for item in list:
    if item > largest:
        largest = item # it will store the largest number in largest variable
    if item < smallest:
        smallest = item # it will store the smallest number in smallest variable

# Print the results
print("Largest number:", largest)
print("Smallest number:", smallest)