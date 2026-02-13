class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

class Square(rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_width(self, width):
        self.set_width(width)
        self.set_height(width)
 
    def set_height(self, height):
        self.set_width(height)
        self.set_height(height)
def resize_rectangle(rectangle, new_width, new_height):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width, rectangle.height

rect = rectangle(4, 5)
print("Rectangle before resize:", resize_rectangle(rect, 6, 7))
square = Square(4)
print("Square before resize:", resize_rectangle(square, 6, 7))