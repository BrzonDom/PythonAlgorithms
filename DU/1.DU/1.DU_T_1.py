"""
Napište program max_seq.py, který v posloupnosti čísel najde podposloupnost, která má největší součet.

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
        
    Vstup:
        3 1 -6 2 4 1 -3 2 -5 4 -5
    Výstup:
        3 7
"""
import copy


def sumArr(Arr):

    sum = 0

    for num in Arr:
        sum = sum + num

    return(sum)


def seqMax(seq):

    seqCnt = len(seq)

    """     Prints the original sequence    """
    # print(f"Sequence: {seq}")
    # print(f"\tLen of sequence: {seqCnt}")

    maxSeq = curSeq = [0]

    """     Count of the sequence   """
    maxCnt = curCnt = 0
    """     Sum of the sequence     """
    maxTot = curTot = 0
    i = 2

    for num in range(seqCnt):

        """     1. instance - initial values
                    Skips 1. loop   """
        if num == 0:
            maxSeq = curSeq = [seq[0]]
            maxTot = curTot = seq[0]
            maxCnt = curCnt = 1
            continue

        """     Prints the sequence that has been analysed  """
        # print("\nSeq: ", end="")
        # for _ in range(i):
        #     print(seq[_], end=" ")
        # print()
        # i += 1

        """     Updates current sequence    """
        curSeq.append(seq[num])
        curTot += seq[num]
        curCnt += 1

        """     If current total is less than added num
                    Resets current values   """
        if curTot < seq[num]:
            curSeq = [seq[num]]
            curTot = seq[num]
            curCnt = 1

        """     Prints current sequence, total & count  """
        # print("\tCurSeq: ", end="")
        # for _ in range(curCnt):
        #     print(curSeq[_], end=" ")
        # print(f"\n\t\tTot: {curTot}  |  Cnt: {curCnt}")

        """     If max total is less than current total
                    Updates max values  """
        if maxTot < curTot:
            maxSeq = copy.deepcopy(curSeq)
            maxTot = curTot
            maxCnt = curCnt
            # print(maxSeq)

            # print("\t! MaxSeq !")
            # for _ in range(maxCnt):
            #     print(maxSeq[_], end=" ")
            # print(f"\n\t\tTot: {maxTot}  |  Cnt: {maxCnt}")

    return maxSeq

# Input = "1 2 3 4 5 6"
# Input = "-2 -1 -3 -4 -5 -6"
# Input = "1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3"


Input_list = ["1 2 3 4 5 6",
              "-2 -1 -3 -4 -5 -6",
              "1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3",
              "3 1 -6 2 4 1 -3 2 -5 4 -5"]
Input = Input_list[3]


# Input = input()

print("Input: ", end="")
print(Input)

In_Len = len(Input)
print(f"Input Character Lenght: {In_Len}")
print()

# numList = [0]
# numCnt = add = 0
# pol = 1

"""     Manual convert from string to int list  """
# for char in Input:
#     if (char != ' '):
#         if (char == '-'):
#             pol = -1
#             # print("Minus")
#         elif (('0' <= char) & (char <= '9')):
#             numList[numCnt] = numList[numCnt] * 10 + pol * int(char)
#             # print("Number: ", end="")
#             # print(Input[i])
#     else:
#         numCnt += 1
#         pol = 1
#         numList.append(0)
# numCnt += 1

numList = list(map(int, Input.split()))

print("List of numbers: ", end="")

# for i in range(numCnt-1):
#     print(numList[i], end=", ")
# print(numList[numCnt-1])

for num in numList[:-1]:
    print(f"{num} ", end="")
print(numList[-1])

numCnt = len(numList)
print(f"Number of numbers: {len(numList)}")
print()

# maxSeq = [0]
# curSeq = [0]
#
# """     Count of the sequence   """
# maxCnt = curCnt = 0
# """     Sum of the sequence     """
# maxTot = curTot = 0
# i = 2
#
#
# for num in range(numCnt):
#
#     """     1. instance - initial values
#                 Skips 1. loop   """
#     if num == 0:
#         maxSeq = curSeq = [numList[0]]
#         maxTot = curTot = numList[0]
#         maxCnt = curCnt = 1
#         continue
#
#     # print(f"{numList[num]}\n")
#
#     """     Prints the sequence that has been analysed  """
#     print("\nSeq: ", end="")
#     for _ in range(i):
#        print(numList[_], end=" ")
#     print()
#     i += 1
#
#     """     Updates current sequence    """
#     curSeq.append(numList[num])
#     curTot += numList[num]
#     curCnt += 1
#
#     """     If current total is less than added num
#                 Resets current values   """
#     if curTot < numList[num]:
#         curSeq = [numList[num]]
#         curTot = numList[num]
#         curCnt = 1
#
#     """     Prints current sequence, total & count  """
#     print("\tCurSeq: ", end="")
#     for _ in range(curCnt):
#         print(curSeq[_], end=" ")
#     print(f"\n\t\tTot: {curTot}  |  Cnt: {curCnt}")
#
#     """     If max total is less than current total
#                 Updates max values  """
#     if maxTot < curTot:
#         maxSeq = copy.deepcopy(curSeq)
#         maxTot = curTot
#         maxCnt = curCnt
#         # print(maxSeq)
#
#         print("\t! MaxSeq !")
#         # for _ in range(maxCnt):
#         #     print(maxSeq[_], end=" ")
#         # print(f"\n\t\tTot: {maxTot}  |  Cnt: {maxCnt}")


# print("\n\nDone\n")
print("\n")

maxSeq = seqMax(numList)
print(f"MaxSeq: {maxSeq}")

maxCnt = len(maxSeq)
print(f"\tMaxCnt: {maxCnt}")

maxTot = sumArr(maxSeq)
print(f"\tMaxTot: {maxTot}")

