import math

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.rad = radius
        self.col = color

    def area(self):
        return math.pi * self.rad ** 2

    def circum(self):
        return 2 * math.pi * self.rad

    def isIn(self, x, y):
        return (x - self.x) ** 2 + (y - self.y) ** 2 <= self.rad ** 2


clC1 = Circle(1, 1, 1, "green")
clC2 = Circle(3, 1, 0.25, "red")
clC3 = Circle(3, 4, 0.5, "blue")
clCirc_lst = [clC1, clC2, clC3]

point = [2, 2]
cirCnt = 1

for circ in clCirc_lst:
    print(f"{cirCnt}. Circle:")
    print(f"\tColor:              {circ.col}")
    print(f"\tCoordinates:        [{circ.x}, {circ.y}]")
    print(f"\tRadius:             {circ.rad}")
    print(f"\tArea:               {circ.area()}")
    print(f"\tCircumference:      {circ.circum()}")
    print(f"\tIs {point} within:   {circ.isIn(point[0],point[1])}")
    print()
    cirCnt += 1

