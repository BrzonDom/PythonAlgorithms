"""
Napište program int_sum.py, který v posloupnosti čísel najde podposloupnost, která má největší součet.

Vstup:
    - jedna řádka ze standarního vstupu
    - řádka obsahuje posloupnost celých čísel x_1,...,x_n oddělených mezerou
    - pro načtení a převedení vstupu na pole celých čísel můžete použít příkaz
        nums = list(map(int, input().split()))

Výstup: D S, kde D je délka a S je součet nalezené podposloupnosti

Poznámka:
    - Pole na vstupu obsahuje vždy alespoň jedno číslo.
    - Podposloupnost s jedním číslem je také podposloupnost s délkou 1. Podposloupnost musí mít alespoň jedno číslo.
    - Posloupnost obsahuje i záporná čísla.
    - Snažte se najít co nejrychlejší algoritmus, který by fungoval i pro dlouhé sekvence o 20000 prvcích rychle (nejlépe do 1s).
    - Snažte se analyzovat, co musí pro podposloupnost s největším součtem platit a zkusit procházet prvky vstupní posloupnosti pouze jednou.
    - Příklad:
        podposloupnost s největším součtem v posloupnosti 3 1 -6 2 4 1 -3 2 -5 4 -5 je 2 4 1, jenž má největší možný součet 7. Výstupem programu bude délka podposloupnosti a její součet, tedy 3 7
"""

"""
Příklady:

    Vstup:
       1 2 3 4 5 6
    Výstup:
        6 21

    Vstup:
        -2 -1 -3 -4 -5 -6
    Výstup:
        1 -1

    Vstup:
        1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3
    Výstup:
        8 12
"""

def sumArr(Arr):

    sum = 0

    for num in Arr:
        sum = sum + num

    return(sum)

# Input = "1 2 3 4 5 6"
# Input = "-2 -1 -3 -4 -5 -6"
# Input = "1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3"

Input = input()

# print("Input: ", end="")
# print(Input)

numList = [0]
numCnt = add = 0
pol = 1

# In_Len = len(Input)
# print("Input Character Lenght: ", end="")
# print(In_Len)

for char in Input:
    if (char != ' '):
        if (char == '-'):
            pol = -1
            # print("Minus")
        elif (('0' <= char) & (char <= '9')):
            numList[numCnt] = numList[numCnt] * 10 + pol * int(char)
            # print("Number: ", end="")
            # print(Input[i])
    else:
        numCnt += 1
        pol = 1
        numList.append(0)
numCnt += 1

# print()
# print("List of numbers:")

# for i in range(numCnt-1):
#     print(numList[i], end=", ")
# print(numList[numCnt-1])
#
# print()

maxSeq = [0]
curSeq = [0]
maxCnt = curCnt = maxTot = curTot = 0
# i = 2


for num in range(numCnt):
    if num == 0:
        maxSeq = curSeq = [numList[0]]
        maxTot = curTot = numList[0]
        maxCnt = curCnt = 1
        continue

    # print(f"{numList[num]}\n")
    # print("\nSeq: ", end="")
    # for _ in range(i):
    #     print(numList[_], end=" ")
    # print()
    # i += 1

    curSeq.append(numList[num])
    curTot += numList[num]
    curCnt += 1

    if curTot < numList[num]:
        curSeq = [numList[num]]
        curTot = numList[num]
        curCnt = 1

    # print("\tCurSeq: ", end="")
    # for _ in range(curCnt):
    #     print(curSeq[_], end=" ")
    # print(f"\n\t\tTot: {curTot}  |  Cnt: {curCnt}")

    if maxTot < curTot:
        maxSeq = curSeq
        maxTot = curTot
        maxCnt = curCnt
        # print("\t! MaxSeq !")

        # print("\tMaxSeq: ", end="")
        # for _ in range(maxCnt):
        #     print(maxSeq[_], end=" ")
        # print(f"\n\t\tTot: {maxTot}  |  Cnt: {maxCnt}")

print(f"{maxCnt} {maxTot}")