"""
Sexy prvočísla

    Sexy prime jsou takové dvojice prvočísel, jejichž (kladný) rozdíl je 6. Například 5 a 11 jsou prvočísla a zároveň se liší o 6, tedy dvojice (5,11) jsou tzv. sexy-primes.
    Napište program, který vypíše všechny takové dvojice menší než 1000.

"""

maxNum = 1000
primNumLst = [2]


for curNum in range(2, maxNum+1):
    for primNum in primNumLst:
        if curNum % primNum == 0:
            break
        if primNum == primNumLst[-1]:
            primNumLst.append(curNum)


print(primNumLst)

sexy_primeLst = []


for prIn in range(len(primNumLst)):
    for pr in range(1, prIn):
        # print(pr)
        print(f"{primNumLst[prIn-pr]} - {primNumLst[prIn]} = {abs(primNumLst[prIn] - primNumLst[prIn-pr])}")
        if abs(primNumLst[prIn] - primNumLst[prIn-pr]) == 6:
            sexy_primeLst.append([primNumLst[prIn], primNumLst[prIn-pr]])
            print()
            break
        elif abs(primNumLst[prIn] - primNumLst[prIn-pr]) > 6:
            break

print(sexy_primeLst)
