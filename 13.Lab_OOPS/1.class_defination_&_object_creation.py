'''
Question: Create a Python class named Person with attributes name and age. 
Implement a method greet that prints a greeting message including the person's name. 
Create an instance of the Person class and call the greet method.
'''
#Defining Class named Person
class Person:
    def __init__(self, name, age): #attributes are name and age
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")
        print(f"I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Afzal", 20)

# Object creation - Calling the greet method
person1.greet()