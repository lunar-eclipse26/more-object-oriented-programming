import math
class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
def main():
    radius = float(input("enter the radius of your circular 2 dimensional shape:"))
    circular = circle(radius)
    print("Area of circle:", circular.area())
    print("Perimeter (Circumference):", circular.perimeter())
if __name__ == "__main__":
    main()