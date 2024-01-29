
def findItm(set, theItm):

    for itm in set:
        if itm == theItm:
            return True
    return False


a = [0, 1, 0, 2]

print(findItm(a, 0))
print(findItm(a, '0'))