
from abc import abstractmethod
class shape:
    @abstractmethod
    def resize(self, new_width, new_height):
        pass
    def area(self):
        pass    
class rectangle(shape):
    def __init__(self, width, height):  
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height
        

class Square(shape):
    def __init__(self, side_length):
        super().__init__()
        self.width = side_length
        self.height = side_length
    
    def area(self):
        return self.width * self.height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

def resize_rectangle(shape, rectangle, new_width, new_height):
    shape.resize(new_width, new_height)
    return rectangle.width, rectangle.height

rect = rectangle(4, 5)
resize_rectangle(rect,4,5)
print("Rectangle before resize:", resize_rectangle(rect, 6, 7))
square = Square(4)
print("Square before resize:", resize_rectangle(square, 6, 7))