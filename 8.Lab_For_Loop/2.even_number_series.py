# 2. Print even number series by taking input from the user:

# Taking input from the user for the range (stop value) 
n = int(input("Enter the range for the even number series: "))

#the first 2 in range is the start value, then n+1 is the stop value to ensure n itself is even I wrote +1,
# and last 2 is the step value to ensure we get even numbers only
for i in range(2, n + 1, 2): 
    print(i, end=" ")


'''
Output -
if given input is 10 
2,4,6,8,10
if given input is 15
2,4,6,8,10,12,14
'''