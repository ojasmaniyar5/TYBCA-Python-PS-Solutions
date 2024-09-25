import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Example usage
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

print(f"Area: {circle.area():.2f}")
print(f"Circumference: {circle.circumference():.2f}")
