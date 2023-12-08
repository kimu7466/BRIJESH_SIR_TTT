from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def area(self, l, b):
        return 0.5 * l * b
    
class square(shape):
    def area(self, l, b, h):
        return h * l * b
    
class circle(shape):
    def area(self, r):
        return 3.14 * ( r ** 2)
    
obj = square()
print(dir(obj))
print(obj.area(10,10,10))

obj = triangle()
print(obj.area(10,20))