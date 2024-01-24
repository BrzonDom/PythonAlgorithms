"""
Lehká varianta

    V zadané množině čísel najděte číslo, které má největší společný dělitel s prvním zadaným číslem a tento největší společný dělitel vytiskněte.

    Vstup:

        první řádka obsahuje počet zadaných čísel
        ostatní řádky obsahují vždy jedno celé číslo.
    Výstup:

        největší společný dělitel s prvním číslem

    Program pro úlohu HW03 pojmenujte gcd_max.py
"""

"""
Příklady:
    Vstup:
        5
        21
        9
        8
        7
        6
    Výstup:
        7

    Vstup:
        12
        192779
        253
        263
        273
        283
        683
        693
        703
        713
        723
        733
        743
    Výstup:
        733

    Vstup:
        6
        3099
        6376
        8005
        4116505
        9980
        10000
    Výstup:
        1033
"""

# str_input = """        3099
#         6376
#         8005
#         4116505
#         9980
#         10000"""
#
# int_input = list(map(int, str_input.split()))
# print(int_input)

inNum_list = [[21, 9, 8, 7, 6],
              [192779, 253, 263, 273, 283, 683, 693, 703, 713, 723, 733, 743],
              [3099, 6376, 8005, 4116505, 9980, 10000]]

inNum = inNum_list[1]

print(f"Number input: {inNum}")

print(f"\n\tBase number:             {inNum[0]}")
baseNum = inNum[0]

print(f"\tNumber of numbers:       {len(inNum)}")
print(f"\tNumber of test numbers:  {len(inNum) - 1}")

# maxNum = 1000
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

def GCD(num1, num2):

    """
        Dokud b není rovno nule
            t = b
            b = a mod b
            a = t
        a je největší společný dělitel původních čísel
    """

    a = num1
    b = num2

    steps = 0

    while b != 0:
        # steps += 1

        t = b
        b = a % b
        a = t

    # print(f"GCD.2: ({num1},{num2}) = {a}\n\tSteps: {steps}\n")
    return a

print("\nNumber decomposition:")

for num in inNum:
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

GCD_list = []
GCD_dict = {}

print("\nGreatest common divisor:")
for num in inNum[1:]:
    numGCD = GCD(baseNum, num)
    GCD_list.append(numGCD)
    GCD_dict[numGCD] = num
    print(f"\tGCD ({baseNum}, {num}) = {numGCD}")
    print(f"\t\t{numGCD} : {GCD_dict[numGCD]}")

maxGCD = max(GCD_list)
maxNum = GCD_dict[maxGCD]

print()
print(f"For base number: {baseNum}")
print(f"\tMax GCD:        {maxGCD}")
print(f"\tNum of max GCD: {maxNum}")

