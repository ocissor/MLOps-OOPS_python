from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Must be implemented
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())  # Output: 78.5

#Shape is an abstract class, and area() is an abstract method

from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

# Concrete class (Child class implementing abstract method)
class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# obj = Animal()  # ❌ ERROR: Cannot instantiate an abstract class

dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof! Woof!
print(cat.make_sound())  # Output: Meow! Meow!
