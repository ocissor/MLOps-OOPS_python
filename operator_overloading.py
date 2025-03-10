class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading '+' operator
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(1, 2)

p3 = p1 + p2  # Calls __add__ method
print(p3)  # Output: (4, 6)
print(str(p1))

'''__add__ is overridden to define how + behaves when adding two Point objects.
The expression p1 + p2 internally calls p1.__add__(p2), returning a new Point object.'''