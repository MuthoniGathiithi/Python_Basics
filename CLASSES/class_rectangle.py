class Rectangle:
    def __init__(self,length , width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width) 

    def is_square(self):
        return self.length == self.width   
    
r1 = Rectangle(5, 3)
print(f"Area: {r1.calculate_area()}")
print(f"Perimeter: {r1.perimeter()}")
       
       