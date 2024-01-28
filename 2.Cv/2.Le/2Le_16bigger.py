
def sortAB(a, b):
    if a < b:
        return a, b

    else:
        return b, a

x, y = sortAB(10, -1)
print(type(x))
print(x, y)
print()

z = sortAB(10, -1)
print(type(z))
print(z)

