
def sortAB(a, b):
    if a < b:
        return a, b

    else:
        return b, a

x, y = sortAB(10, -1)

print(x, y)
