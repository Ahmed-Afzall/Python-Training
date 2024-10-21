'''
Question: Create a base class Employee with attributes name and salary. 
Create a derived class Manager that inherits from Employee and adds an additional 
attribute department. Implement a method in the Manager class to display the manager's details, including name, salary, and department.
'''

# Parent class / Base Class / Super class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Child Class / Derived Class / Sub Class
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")

# Creating an instance of the Manager class
manager = Manager("Afzal", 1000, "IT")

# Calling the display_details method
manager.display_details()