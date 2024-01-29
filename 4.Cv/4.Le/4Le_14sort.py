
def isSort(set):

    for i in range(len(set) - 1):
        if not set[i] <= set[i+1]:
            return False

    return True


set = [10, -1, 2, 0, 0]

print(f"List: {set}\n")

print(set, " Sorted: ", isSort(set))

set.sort()
print(set, " Sorted: ", isSort(set))
print()

set = [100, -10, 0, 1, -3, 5, 4]
print(f"List: {set}\n")

print(set)

for i in range(len(set) - 1):
    if set[i] > set[i+1]:
        set[i], set[i+1] = set[i+1], set[i]

print(set)