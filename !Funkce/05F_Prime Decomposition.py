def primNum(num):

    primNumLst = [2]

    for curNum in range(2, num + 1):
        for primNum in primNumLst:
            if curNum % primNum == 0:
                break
            if primNum == primNumLst[-1]:
                primNumLst.append(curNum)
    # print(primNumLst)
    return primNumLst


def primDec(num):

    primNumLst = primNum(num)
    primDecLst = [1]

    while num != 1:
        for prim in primNumLst:
            if num % prim == 0:
                num = num // prim
                primDecLst.append(prim)
                break
    # print(primDecLst)
    return primDecLst


num_list = [26, 24, 25, 21, 18, 17, 16, 15, 12, 10, 9, 8, 6, 4]

print(f"Number input: {num_list}")

print("\nNumber decomposition:")

for num in num_list:
    numDec = primDec(num)
    numDecStr = ""
    print(f"\t{num}", end=" = ")
    for prim in numDec[1:]:
        # if prim == numDec[-1]:
        #     print(f"{prim}")
        # else:
        #     print(f"{prim} * ", end="")
        numDecStr += f"{prim} * "
    print(numDecStr[:-3])
