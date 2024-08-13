# 1. Function without Parameters:

# Q1. What is a function without parameters, and when might you use one?
'''
A1. A function that doesn't require any input arguments when called is known as a function without parameters. 
This indicates that the function operates without the need for any outside input to complete its task.

When an operation needs to be completed and either depends on external data sources or cannot be supplied 
as arguments, functions without parameters come in handy. For example:

- print_hello() is an example of a function that outputs a predetermined message.
- a function that generates numbers at random.
- a function responsible for setting some global variables to their initial values.
'''

# 2. How do you define and call a function that does not take any arguments?

# Defining the function
def myName():
    print("My name is Afzal")

myName() # Calling the function

'''The myName() function in this example is defined without any parameters and is called by just passing its name between parenthesis.'''


# 3. Can a function without parameters return a value? If so, how?

'''Yes, It is possible for a function to return a value without any parameters. To send a value back to the caller, 
you define it in the same way as any other function and use the return statement.'''

# Defining the function
def get_pi():
    return 3.14159

# Calling the function
pi_value = get_pi()
print(pi_value)

'''Get_pi() in this example returns Pi's value without accepting any parameters.'''
