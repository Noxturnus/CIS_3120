#Lab: Inheritance

#Shape :Base class
class Shape:
    def area(self):
        return 0

    def describe(self):
        print("This is a shape！")

#subclass 1: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        print("This is a rectangle!")

#subclass 2: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def describe(self):
        print("This is a circle!")

#Define the main and create objects
def main():
    rect1 = Rectangle(5, 10)
    circle1 = Circle(7)

    rect1.describe()
    print("Area of rectangle: ", rect1.area())
    print("-----------------------------")
    circle1.describe()
    print("Area of circle: ", circle1.area())

main()