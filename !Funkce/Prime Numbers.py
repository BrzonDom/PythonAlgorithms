
maxNum = 1000
primNumLst = [2]

for curNum in range(2, maxNum+1):
    for primNum in primNumLst:
        if curNum % primNum == 0:
            break
        if primNum == primNumLst[-1]:
            primNumLst.append(curNum)

print(primNumLst)