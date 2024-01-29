
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

print(f"List: {a}")
print()

print(f"Item: 0")
search = findItm(a, 0)
print("\t", search)

if search:
    index = findItmIndx(a, 0)
    print("\t", index)
print()

print(f"Item: '0'")
print("\t", findItm(a, '0'))
print()

a = ['a', 'b', 'aa', 'a', 'bb', 'a']

print(f"List: {a}")
print()

print(f"Item: 'a'")
index = findItms(a, 'a')
print("\t", index)
print()

print(f"Item: 'A'")
index = findItms(a, 'A')
print("\t", index)

print()

print(f"Item: 'a'")
if 'a' in a:
    print("\t", True)
    i = 0
    index = []

    while i < len(a):
        if 'a' in a[i:]:
            i = a.index('a', i)
            index.append(i)
            # print(index)
            i += 1
        else:
            break

    print("\t", index)

else:
    print("\t", False)