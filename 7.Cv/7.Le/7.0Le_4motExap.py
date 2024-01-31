import math


# def findLarg(circles):
#
#     maxCirc = None
#
#     for circ in circles:
#         x, y, rad, col = circ
#

class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.rad = radius
        self.col = color

"""     circ_n = [x, y, radius, color]      """

circ1 = [3, 1, 0.25, "red"]
circ2 = [1, 1, 1, "green"]
circ3 = [3, 4, 0.5, "blue"]

circ_lst = [circ1, circ2, circ3]

for c, circ in enumerate(circ_lst):
    print(f"{c+1}. Circle:")
    print(f"\t[x, y] = [{circ[0]}, {circ[1]}]")
    print(f"\tradius = {circ[2]}")
    print(f"\tcolor = {circ[3]}")
    print()

print()

clC1 = Circle(1, 1, 1, "green")
clC2 = Circle(3, 1, 0.25, "red")
clC3 = Circle(3, 4, 0.5, "blue")

clCirc_lst = [clC1, clC2, clC3]


print("Class circle:")

print("\t[x, y] coordinates:")
for circ in clCirc_lst:
    print(f"\t\t[{circ.x}, {circ.y}]")

print("\tradius:")
for circ in clCirc_lst:
    print(f"\t\t{circ.rad}")
print("\tvolume:")
for circ in clCirc_lst:
    print(f"\t\tπ⋅{circ.rad}² = {math.pi * (circ.rad**2)}")

print("\tcolor:")
for circ in clCirc_lst:
    print(f"\t\t{circ.col}")