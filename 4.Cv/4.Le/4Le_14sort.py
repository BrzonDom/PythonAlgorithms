
def isSort(set):

    for i in range(len(set) - 1):
        if not set[i] <= set[i+1]:
            return False

    return True


def bubbleSort(set):

    for _ in range(len(set)):
        for i in range(len(set) - 1):
            if set[i] > set[i + 1]:
                set[i], set[i + 1] = set[i + 1], set[i]



set = [10, -1, 2, 0, 0]

print(f"List: {set}\n")

print(set, " Sorted: ", isSort(set))

set.sort()
print(set, " Sorted: ", isSort(set))
print()

set = [100, -10, 0, 1, -3, 5, 4]
print(f"List: {set}")

print("\t", set)

for _ in range(len(set)):
    for i in range(len(set) - 1):
        if set[i] > set[i+1]:
            set[i], set[i+1] = set[i+1], set[i]

print("\t", set)
print()

set = [100, -10, 0, 1, -3, 5, 4]

print(f"List: {set}")

print("\t", set)

bubbleSort(set)

print("\t", set)
print()

set = [100, -10, 0, 1, -3, 5, 4]

print(f"List: {set}")

print("\t", set)

while not isSort(set):
    for i in range(len(set) - 1):
        if set[i] > set[i + 1]:
            set[i], set[i + 1] = set[i + 1], set[i]

print("\t", set)