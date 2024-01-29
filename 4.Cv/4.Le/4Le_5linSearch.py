
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


def findItms(set, theItm):

    index = []

    for i in range(len(set)):
        if set[i] == theItm:
            index.append(i)

    return index


a = [0, 1, 0, 2]

search = findItm(a, 0)
print(search)

if search:
    index = findItmIndx(a, 0)
    print(index)
print()

print(findItm(a, '0'))
print()

a = ['a', 'b', 'aa', 'a', 'bb', 'a']

index = findItms(a, 'a')
print(index)
index = findItms(a, 'A')
print(index)
