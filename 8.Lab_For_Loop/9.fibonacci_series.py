# 9. Python program to get the Fibonacci series between 0 to 50:

a, b = 0, 1              # Initializing the first two numbers of the Fibonacci series

while a <= 50:           # Loop to print Fibonacci numbers until 'a' is less than or equal to 50
    print(a, end=" ")    # Printing the current value of 'a'
    a, b = b, a + b      # Update the values of 'a' and 'b. The new 'a' becomes the old 'b', and the new 'b' becomes the sum of old 'a' and 'b'