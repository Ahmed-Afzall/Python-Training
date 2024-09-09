# 2. Function with Parameter:

# 1. How do you define a function that takes parameters?
'''When defining a function that accepts parameters, the parameter names must be enclosed in parenthesis within the function definition. 
For example,'''

# Defining the function
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with a parameter
greet("Afzal")

'''In this instance, a personalized greeting is printed using the function greet(name), which accepts one input, name.'''


# 2. What are the rules for passing arguments to a function?

'''Positional Arguments: arguements that are positional are presented in the order that they are defined. 
For example, "Afzal" is supplied to name in greet("Afzal").

Keyword Arguments: You can designate which parameter receives which value by passing arguments by name. 
For example, greet(name="Afzal").

Default Parameters: You can make parameters optional by setting default values for them. 
In the absence of one, the default is applied.

Arguments of Variable Length: For positional arguments with variable length, use *args; 
for keyword arguments with variable length, use **kwargs.
'''

# 3.How can you use parameters to make a function more flexible or reusable?

'''Functions are made more reusable and flexible by parameters, which let them work with multiple types 
of data without requiring modifications to the function's code. For instance:
'''
def add(a, b):
    return a + b

result1 = add(2, 3)  
result2 = add(10, 20)
print(result1)
print(result2)

'''Since the add() function may add any two numbers in this situation, it is flexible and reusable in other situations.

By writing more general-purpose functions and eliminating repetition, you can increase the maintainability and 
scalability of your code by utilizing parameters.
'''
