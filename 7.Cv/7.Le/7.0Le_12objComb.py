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

    def sumArea(self, other):
        return self.area() + other.area()

    def intersect(self, other):

        dx = self.x - other.x
        dy = self.y - other.y

        return (dx ** 2 + dy ** 2) ** (0.5) <= self.rad + other.rad



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

print()
print("Area sum of 1.Circle and 3.Circle:\n")
print(f"\tArea of 1.Circle = {clC1.area()}")
print(f"\tArea of 3.Circle = {clC3.area()}")
print(f"\n\tCombined area = {clC1.area()} + {clC3.area()} = {clC1.sumArea(clC3)}")
print("\n")

print("Do circles intersect:")
print()

crcInt = [1, 2]
print(f"\t{crcInt[0]}. Circle and {crcInt[1]}.Circle")
print(f"\t\t{crcInt[0]}.Circle:")
print(f"\t\t\tCoord: [{clCirc_lst[crcInt[0]-1].x}, {clCirc_lst[crcInt[0]-1].y}]")
print(f"\t\t\tRadius: {clCirc_lst[crcInt[0]-1].rad}")
print(f"\t\t{crcInt[1]}.Circle:")
print(f"\t\t\tCoord: [{clCirc_lst[crcInt[1]-1].x}, {clCirc_lst[crcInt[1]-1].y}]")
print(f"\t\t\tRadius: {clCirc_lst[crcInt[1]-1].rad}")
# print(f"\t\t{crcInt[1]}.Circ coord: [{clCirc_lst[crcInt[1]-1].x}, {clCirc_lst[crcInt[1]-1].y}]")
# print(f"\t\t{crcInt[0]}.Circ radius: {clCirc_lst[crcInt[0]-1].rad}")
# print(f"\t\t{crcInt[1]}.Circ radius: {clCirc_lst[crcInt[1]-1].rad}")
if (clCirc_lst[crcInt[0]-1].intersect(clCirc_lst[crcInt[1]-1])):
    print("\tThey DO intersect")
else:
    print("\tThey DON'T intersect")
print()

crcInt = [1, 3]
print(f"\t{crcInt[0]}. Circle and {crcInt[1]}.Circle")
print(f"\t\t{crcInt[0]}.Circle:")
print(f"\t\t\tCoord: [{clCirc_lst[crcInt[0]-1].x}, {clCirc_lst[crcInt[0]-1].y}]")
print(f"\t\t\tRadius: {clCirc_lst[crcInt[0]-1].rad}")
print(f"\t\t{crcInt[1]}.Circle:")
print(f"\t\t\tCoord: [{clCirc_lst[crcInt[1]-1].x}, {clCirc_lst[crcInt[1]-1].y}]")
print(f"\t\t\tRadius: {clCirc_lst[crcInt[1]-1].rad}")
# print(f"\t\t{crcInt[1]}.Circ coord: [{clCirc_lst[crcInt[1]-1].x}, {clCirc_lst[crcInt[1]-1].y}]")
# print(f"\t\t{crcInt[0]}.Circ radius: {clCirc_lst[crcInt[0]-1].rad}")
# print(f"\t\t{crcInt[1]}.Circ radius: {clCirc_lst[crcInt[1]-1].rad}")
if (clCirc_lst[crcInt[0]-1].intersect(clCirc_lst[crcInt[1]-1])):
    print("\tThey DO intersect")
else:
    print("\tThey DON'T intersect")
print()

crcInt = [2, 3]
print(f"\t{crcInt[0]}. Circle and {crcInt[1]}.Circle")
print(f"\t\t{crcInt[0]}.Circle:")
print(f"\t\t\tCoord: [{clCirc_lst[crcInt[0]-1].x}, {clCirc_lst[crcInt[0]-1].y}]")
print(f"\t\t\tRadius: {clCirc_lst[crcInt[0]-1].rad}")
print(f"\t\t{crcInt[1]}.Circle:")
print(f"\t\t\tCoord: [{clCirc_lst[crcInt[1]-1].x}, {clCirc_lst[crcInt[1]-1].y}]")
print(f"\t\t\tRadius: {clCirc_lst[crcInt[1]-1].rad}")
# print(f"\t\t{crcInt[1]}.Circ coord: [{clCirc_lst[crcInt[1]-1].x}, {clCirc_lst[crcInt[1]-1].y}]")
# print(f"\t\t{crcInt[0]}.Circ radius: {clCirc_lst[crcInt[0]-1].rad}")
# print(f"\t\t{crcInt[1]}.Circ radius: {clCirc_lst[crcInt[1]-1].rad}")
if (clCirc_lst[crcInt[0]-1].intersect(clCirc_lst[crcInt[1]-1])):
    print("\tThey DO intersect")
else:
    print("\tThey DON'T intersect")
print()

