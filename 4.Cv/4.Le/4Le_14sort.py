
def isSort(set):

    for i in range(len(set) - 1):
        if not set[i] <= set[i+1]:
            return False

    return True


set = [10, -1, 2, 0, 0]
print(set, " Sorted: ", isSort(set))

set.sort()
print(set, " Sorted: ", isSort(set))
