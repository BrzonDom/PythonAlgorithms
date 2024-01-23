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
# Input = "1 2 3 4 5 6"
# Input = "-2 -1 -3 -4 -5 -6"
Input = "1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3"

# Input = input()

print("Input: ", end="")
print(Input)

numList = [0]
numCnt = add = 0
pol = 1

In_Len = len(Input)
print("Input Character Lenght: ", end="")
print(In_Len)

for i in range(In_Len):
    if (Input[i] != ' '):
        if (Input[i] == '-'):
            pol = -1
            # print("Minus")
        elif (('0' <= Input[i]) & (Input[i] <= '9')):
            numList[numCnt] = numList[numCnt] * 10 + pol * int(Input[i])
            # print("Number: ", end="")
            # print(Input[i])
    else:
        numCnt += 1
        pol = 1
        numList.append(0)
numCnt += 1

print()
print("List of numbers:")

for i in range(numCnt-1):
    print(numList[i], end=", ")
print(numList[numCnt-1])

maxSeq = seq = [numList[0]]
seqTot = maxSeqTot = numList[0]
seqCnt = maxSeqCnt = 1

seqCond = [numList[0] - 1, numList[0] + 1]

for i in range(1, numCnt+1):
    if seqTot > maxSeqTot:
        maxSeq = seq
        maxSeqTot = seqTot
        maxSeqCnt = seqCnt

    if i == numCnt:
        break
    elif numList[i] > maxSeqTot:
        maxSeq = [numList[i]]
        maxSeqTot = numList[i]
        maxSeqCnt = 1

    if numList[i] in seqCond:
        seq.append(numList[i])
        seqCnt += 1
        seqTot += numList[i]
        if numList[i] == (numList[i-1] + 1):
            seqCond = [numList[i] + 1]
        elif numList[i] == (numList[i-1] - 1):
            seqCond = [numList[i-1] - 1]
    else:
        seqCond = [numList[i] - 1, numList[i] + 1]
        seq = [numList[i]]
        seqTot = numList[i]
        seqCnt = 1


print("\nMax sequence: ", end="")
for i in range(maxSeqCnt-1):
    print(maxSeq[i], end=", ")
print(maxSeq[maxSeqCnt-1])
print("\nMax sequence count: ", end="")
print(maxSeqCnt)
print("\nMax sequence total: ", end="")
print(maxSeqTot)