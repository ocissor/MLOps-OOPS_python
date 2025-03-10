class Parent:
    def show(self):
        return "This is the parent class"

class Child(Parent):
    def show(self):  # Overriding the 'show' method
        return "This is the child class"

obj1 = Parent()
obj2 = Child()

print(obj1.show())  # Output: This is the parent class
print(obj2.show())  # Output: This is the child class (Overridden method)

'''The Child class overrides the show() method of Parent class.
When calling show() from a Child object, it executes the child class version instead of the parent’s.'''