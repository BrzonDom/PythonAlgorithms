
def findItm(set, theItm):

    for itm in set:
        if itm == theItm:
            return True
    return False


def findItmIndx(set, theItm):

    for i in range(len(set)):
        if set[i] == theItm:
            return i

    return -1

a = [0, 1, 0, 2]

search = findItm(a, 0)
print(search)

if search:
    index = findItmIndx(a, 0)
    print(index)
print()

print(findItm(a, '0'))