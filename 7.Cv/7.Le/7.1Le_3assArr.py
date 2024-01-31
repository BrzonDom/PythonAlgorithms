
"""
    ’points’ is associative array
"""

points = {}

points["Aaa"] = -1
points["Bbb"] = 3
points["Ccc"] = 0

print(f"Org.:")
for txt in points:
    print(f"\tpoints[{txt}] = {points[txt]}")

for txt in points:
    points[txt] += 1

print()
print(f"Aft.:")
for txt in points:
    print(f"\tpoints[{txt}] = {points[txt]}")