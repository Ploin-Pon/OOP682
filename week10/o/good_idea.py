#good idea
from abc import abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def calculate_area(shape):
    return shape.area() 