#single inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return "Bark!"

dog = Dog("Buddy")
print(dog.name)   # Output: Buddy
print(dog.speak())  # Output: Bark!


#multiple inheritance
class Parent1:
    def feature1(self):
        return "Feature 1 from Parent1"

class Parent2:
    def feature2(self):
        return "Feature 2 from Parent2"

class Child(Parent1, Parent2):  # Inherits from both Parent1 & Parent2
    def feature3(self):
        return "Feature 3 from Child"

obj = Child()
print(obj.feature1())  # Output: Feature 1 from Parent1
print(obj.feature2())  # Output: Feature 2 from Parent2
print(obj.feature3())  # Output: Feature 3 from Child


#multilevel inheritance
class Grandparent:
    def feature1(self):
        return "Feature 1 from Grandparent"

class Parent(Grandparent):
    def feature2(self):
        return "Feature 2 from Parent"

class Child(Parent):
    def feature3(self):
        return "Feature 3 from Child"

obj = Child()
print(obj.feature1())  # Output: Feature 1 from Grandparent
print(obj.feature2())  # Output: Feature 2 from Parent
print(obj.feature3())  # Output: Feature 3 from Child

#hierarchical inheritance
class Parent:
    def feature1(self):
        return "Feature 1 from Parent"

class Child1(Parent):
    def feature2(self):
        return "Feature 2 from Child1"

class Child2(Parent):
    def feature3(self):
        return "Feature 3 from Child2"

obj1 = Child1()
obj2 = Child2()

print(obj1.feature1())  # Output: Feature 1 from Parent
print(obj1.feature2())  # Output: Feature 2 from Child1

print(obj2.feature1())  # Output: Feature 1 from Parent
print(obj2.feature3())  # Output: Feature 3 from Child2

#hybrid inheritance
class Base:
    def feature1(self):
        return "Feature 1 from Base"

class Parent1(Base):
    def feature2(self):
        return "Feature 2 from Parent1"

class Parent2(Base):
    def feature3(self):
        return "Feature 3 from Parent2"

class Child(Parent1, Parent2):
    def feature4(self):
        return "Feature 4 from Child"

obj = Child()
print(obj.feature1())  # Output: Feature 1 from Base
print(obj.feature2())  # Output: Feature 2 from Parent1
print(obj.feature3())  # Output: Feature 3 from Parent2
print(obj.feature4())  # Output: Feature 4 from Child


