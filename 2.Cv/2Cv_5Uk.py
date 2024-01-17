"""
Break cykl
Napište program, který načte číslo n a najde jeho nejmenšího dělitele většího než 1.

Je vhodné použít konstrukci break, cyklus můžete použít while i for.

Otestujte svůj program na čísle 999962000357
"""

# Find Prime Numbers Function
# maxNum = 17
# primNumLst = [2]
#
# for curNum in range(2, maxNum+1):
#     for primNum in primNumLst:
#         if curNum % primNum == 0:
#             break
#         if primNum == primNumLst[-1]:
#             primNumLst.append(curNum)
#
# print(primNumLst)

num = 999962000357

for curNum in range(2, num+1):
    if num % curNum == 0:
        print(curNum)
        break


# num = 999962000357
# primNumLst = [2]
# minDiv = 0
#
# for curNum in range(2, num+1):
#     for primNum in primNumLst:
#         if curNum % primNum == 0:
#             break
#         if primNum == primNumLst[-1]:
#             primNumLst.append(curNum)
#             if num % curNum == 0:
#                 print(curNum)
#                 minDiv = curNum
#     if minDiv:
#         break
#
# print("Done")