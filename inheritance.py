class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self, sound):
        return f"Some generic animal sound {sound}"

class Dog(Animal):  # Inheriting from Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent class constructor
        self.breed = breed

    def make_sound(self):
        print(super().make_sound("woof"))  # Calling parent class method
        return "Bark!"  # Overriding the method

# Creating an object of Dog class
dog1 = Dog("Buddy", "Golden Retriever")

print(dog1.name)          # Output: Buddy (inherited from Animal)
print(dog1.breed)         # Output: Golden Retriever (specific to Dog)
print(dog1.make_sound())  # Output: Bark! (Overridden method)



