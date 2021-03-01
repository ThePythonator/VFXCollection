from math import sqrt as math_sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def magnitude(self):
        return math_sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point(self.x + other[0], self.y + other[1])
        else:
            return Point(self.x + other, self.y + other)
    
    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point(self.x - other[0], self.y - other[1])
        else:
            return Point(self.x - other, self.y - other)
    
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point(self.x * other[0], self.y * other[1])
        else:
            return Point(self.x * other, self.y * other)
    
    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.x / other.x, self.y / other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point(self.x / other[0], self.y / other[1])
        else:
            return Point(self.x / other, self.y / other)
            
    def __floordiv__(self, other):
        if isinstance(other, Point):
            return Point(self.x // other.x, self.y // other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point(self.x // other[0], self.y // other[1])
        else:
            return Point(self.x // other, self.y // other)
            
    def __mod__(self, other):
        if isinstance(other, Point):
            return Point(self.x % other.x, self.y % other.y)
        elif isinstance(other, list) or isinstance(other, tuple):
            return Point(self.x % other[0], self.y % other[1])
        else:
            return Point(self.x % other, self.y % other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not (self.x == other.x and self.y == other.y)