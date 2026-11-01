# 3. Write a Program to Convert Kilometers to Miles 

# Taking desired kilometers in input from the user
kilometers = float(input("Enter the distance in kilometers: "))

# 1 km = 0.621371 miles; 
conversion_rate = 0.621371

# Converting kilometers to miles by multiplying it with 0.621371
miles = kilometers * conversion_rate

# Displaying the conversion
print(f"{kilometers} kilometers is equal to {miles} miles")
