# Q.1 print helloworld
print("Hello world")


# Q.2 describe local variable and global variable code
global_var = "I am a global variable"

def example_function():
    local_var = "I am a local variable"
    print(local_var)  # Output: I am a local variable

example_function()
print(global_var)  # Output: I am a global variable
# print(local_var)  # This will raise an error because local_var is not accessible outside the function


# Q.3 Write a code that describe Indentation error
"""def example_function():
print("This will cause an IndentationError because it is not properly indented")
"""

#Q.4 write a code that describe local and global variable with same name follows the roles 
var = "I am a global variable"

def example_function():
    var = "I am a local variable"
    print(var)  # Output: I am a local variable

example_function()
print(var)  # Output: I am a global variable


#Q.5 Write a code for string, int and float input.
# Input for string
string_input = input("Enter a string: ")

# Input for integer
int_input = int(input("Enter an integer: "))

# Input for float
float_input = float(input("Enter a float: "))

print("String input:", string_input)
print("Integer input:", int_input)
print("Float input:", float_input)
