import math

print('\n\nThis program will demonstrate the concept of inheritance...\n')
#Parent Class
class Shape:
    def __init__ (self, color='black', filled = False):
        self._color = color
        self._filled = filled
    
    def getColor(self):
        return self._color
    
    def setColor(self, color):
        self._color = color
        
    def getFilled(self):
        return self._filled
    
    def setFilled(self, filled):
        self._filled = filled

#Child/Derived Class
class Rectangle(Shape): #inheriting from the Shape class
    def __init__(self, length, width):
        super().__init__()  #calling the constructor of the parent class and other methods - Shape
        self._width = width
        self._length = length
        
    def getLength(self):
        return self._length
    
    def setLength(self, length):
        self._length = length
        
    def getWidth(self):
        return self._width
    
    def setWidth(self, width):
        self._width = width
        
    def getArea(self):
        return self._width * self._length

    def getPerimeter(self):
        return (self._width + self._length) * 2

#Child/Derived Class
class Circle(Shape):
    def __init__ (self, radius):
        super().__init__()  #calling the constructor of the parent class and other methods - Shape
        self._radius = radius
    
    def getRadius(self):
        return self._radius
    
    def setRadius(self, radius):
        self._radius = radius
        
    def getArea (self):
        return math.pi * self._radius ** 2
    def getPerimeter (self):
        return math.pi * self._radius * 2

#creating an instance of Rectangle - r1
r1 = Rectangle(10, 2)
print(f'\nArea of the rectangle is : {r1.getArea()} ')
print(f'Perimeter of the rectangle is: {r1.getPerimeter()}')
print(f'Color of the rectangle is: {r1.getColor()}')
print('Is rectangle r1 filled ? ', r1.getFilled())
r1.setFilled(True)
print('Is rectangle r1 filled ? ', r1.getFilled())
r1.setColor('blue')
print('Color of rectangle r1: ', r1.getColor())

#creating an instanc of Circle - c1
c1 = Circle(2)
print(f"\nArea of the Circle is :", format(c1.getArea(), '0.2f'))
print(f"Perimeter of the Circle is: ", format(c1.getPerimeter(), '0.2f'))
print(f'Color of the Circle is: {c1.getColor()}')
print('Is Cirlce r1 filled ? ', c1.getFilled())
c1.setFilled(True)
print('Is Circle r1 filled ? ', c1.getFilled())
c1.setColor('pink')
print('Color of Cirlce r1: ', c1.getColor())