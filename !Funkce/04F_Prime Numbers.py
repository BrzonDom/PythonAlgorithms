
maxNum = 1000
primNumLst = [2]

for curNum in range(2, maxNum+1):
    for primNum in primNumLst:
        if curNum % primNum == 0:
            break
        if primNum == primNumLst[-1]:
            primNumLst.append(curNum)

print(f"Print all prime numbers to {maxNum}")
print()

strPrCnt = 0

print("", end="\t")
for prim in primNumLst:
    strPrCnt += len(str(prim)) + 2
    print(prim, end=", ")

    if strPrCnt > 40:
        print("\n", end="\t")
        strPrCnt = 0