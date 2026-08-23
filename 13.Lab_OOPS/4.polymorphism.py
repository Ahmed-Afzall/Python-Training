'''
Question: Define a function print_area() that takes a Shape object and prints its area. 
Use this function with instances of Rectangle and Circle to demonstrate polymorphism.
'''

# Defining Class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Child Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Child Class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Using an approximation for π

def print_area(shape):
    print(f"Area: {shape.area()}")

# Creating instances of Rectangle and Circle
rectangle = Rectangle(10, 5)
circle = Circle(7)

# Using the print_area function
print_area(rectangle)  # Should print the area of the rectangle
print_area(circle)     # Should print the area of the circle

