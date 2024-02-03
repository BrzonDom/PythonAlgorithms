"""
Těžká varianta

    Napište program max_sum.py, který v posloupnosti čísel najde souvislé podposloupnosti, které se v posloupnosti vyskytují dvakrát. Pokud je takových dvojic podposloupností více, program nalezne tu s největším součtem. Pokud existuje vícero dvojic se shodným součtem, program vybere tu s nejdelší délkou.

    Vstup:
        jedna řádka ze standarního vstupu
        řádka obsahuje posloupnost celých čísel x_1,..., x_n oddělených mezerou
        pro načtení a převedení vstupu na pole celých čísel můžete použít příkaz

            x = list(map(int, input().split()))

    Úkol:

        Program nalezne dvě souvislé podposloupnosti x_i, x_i+1,..., x_i+j a x_k, x_k+1 ,..., x_k+j,
        které:

            jsou shodné jak číselně tako svou délkou, tedy platí x_i = x_k, x_i+1 = x_k+1,..., x_i+j = x_k+j

            nepřekrývají se

            mají největší součet x_i + x_i+1 + ... + x_i+j ze všech podposloupností s uvedenou vlastností.

    Výstup:

        2 čísla oddělená mezerou: počet čísel (délku) a součet čísel ve zdvojené podposloupnosti.

    Poznámky:

        Pole na vstupu obsahuje vždy alespoň dvě čísla a alespoň jednu opakující se sekvenci (minimálně tedy dvě stejná čísla).
        Délka jednočíselné podposloupnosti je 1.

    Odevzdání:

        Program v souboru max_sum.py odevzdejte pomocí odevzdávacího systému BRUTE, úloha HW04.

"""

"""
Příklady:
    Vstup:
        3 3 3 3 3 3 3 3 3
    Výstup:
        4 12
        
        protože program obsahuje dvě nepřekrývající se podposloupnosti délky 4 3 3 3 3, jejíž součet je 12. 
    
    Vstup:
        1 1 1 6 2 2 2 6 1 1 1
    Výstup:
        1 6
        
        protože opakující se podposloupnost s největším součtem je posloupnost s jedním prvkem 6. 
        
    Vstup:
        1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3
    Výstup:
        4 9
        
        Přestože nejdelší stejné podposloupnosti jsou 2 5 -6 8 -3 2, větší součet má její část 2 5 -6 8 o délce 4. 
        
"""
import copy


def LCS_1Vis(seq, Mat):
    len_seq = len(seq)

    # LCS_Mat = [[0 for i in range(lenSeq + 1)] for j in range(lenSeq + 1)]

    print("\n\n\t   |", end="")
    for b in range(lenSeq):
        print(f" {seq[b]:2} |", end="")
    print("\n\t", end="")

    for r in range(1, lenSeq + 2):
        print(" --", end="")
        for b in range(1, lenSeq + 1):
            print("+----", end="")
        print("+\n\t", end="")
        # print()

        if r == lenSeq + 1:
            break
        print(f"{seq[r - 1]:2} ", end="")

        for c in range(1, lenSeq + 1):

            # print(f"| {Mat[r][c]:2} ", end="")

            if LCS_Mat[r][c]:
                print(f"| {Mat[r][c]:2} ", end="")
            else:
                print(f"|    ", end="")

        print("|\n\t", end="")


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

def sumArr(Arr):

    sum = 0

    for num in Arr:
        sum = sum + num

    return(sum)


# str_seq1 = "3 3 3 3 3 3 3 3 3"
# str_seq2 = "1 1 1 6 2 2 2 6 1 1 1"
# str_seq3 = "1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3"
str_seq_list = ["3 3 3 3 3 3 3 3 3",
                "1 1 1 6 2 2 2 6 1 1 1",
                "1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3",
                "1 2 3 4 4 4 4 4 3 2 1",
                "1 2 5 -6 8 -3 2 5 -6 8 -3 2 3",
                "1 2 3 5 -6 8 -3 2 3 5 -6 8 -3 2 3"]

# seq1 = [int(num) for num in list(str_seq1.split(" "))]
# seq2 = [int(num) for num in list(str_seq2.split(" "))]
# seq3 = [int(num) for num in list(str_seq3.split(" "))]

str_seq = str_seq_list[5]

seq = [int(num) for num in list(str_seq.split(" "))]

# print(seq1)
# print(seq2)
# print(seq3)
# print()

lenSeq = len(seq)
# len_seq1 = len(seq1)
# len_seq2 = len(seq2)
# len_seq3 = len(seq3)

print(f"Sequence: {seq}")
print(f"\tSeq Len:      {lenSeq}")
print(f"\tMax Len Seq:  {lenSeq // 2}\n")

# print(f"Max Len Seq: {lenSeq} // 2 = {lenSeq // 2}\n")
# print(f"Max Len_Seq 1: {len_seq1} // 2 = {len_seq1 // 2}")
# print(f"Max Len_Seq 2: {len_seq2} // 2 = {len_seq2 // 2}")
# print(f"Max Len_Seq 3: {lenSeq} // 2 = {lenSeq // 2}")

LCS_Mat = [[0 for i in range(lenSeq + 1)] for j in range(lenSeq + 1)]

TST_Mat = [[1, 0, 0, 1],
           [0, 2, 0, 0],
           [0, 3, 4, 0],
           [0, 0, 0, 5]]

Tri_Mat = [["o" for c in range(5)] for r in range(5)]


# (0, 1)  (1, 2)  (2, 3)  (3, 4)  (4, 5)
# (0, 2)  (1, 3)  (2, 4)  (3, 5)
# (0, 3)  (1, 4)  (2, 5)
# (0, 4)  (1, 5)
# (0, 5)


"""Test diagonal fill of Mat"""
# add = 0
# for row in range(5-1, -1, -1):
#     add += 1
#     print(add)
#     for col in range(row):
#         # print(f"({col}, {col+add}) ", end=" ")
#         Tri_Mat[col][col+add] = "X"
#
#     for mRow in Tri_Mat:
#         for mCol in mRow:
#             print(mCol, end="")
#         print()
#     print()


fnd_res = 0
fnd_index = []
maxSeq = [[]]
mSCon = False
mSCnt = 0


print()

ad = 0

"""Diagonal LSC_Mat analysis"""
# for row in range(lenSeq, 0, -1):
#     ad += 1
#     for col in range(1, row):
#
#         if (seq[col-1] == seq[col+ad-1]):
#             LCS_Mat[col][col+ad] = LCS_Mat[col-1][col+ad-1] + 1
#
#             if LCS_Mat[col][col+ad] > fnd_res:
#                 fnd_index = [col, col+ad]
#             fnd_res = max(fnd_res, LCS_Mat[col][col+ad])
#
#         """Diagonal coordinates print"""
#         print(f"({col}, {col + ad}) ", end=" ")
#         LCS_Mat[col][col+ad] = 1
#     print()


"""Whole LCS_Mat print"""
# for row in LCS_Mat:
#     for col in row:
#         print(col, end=" ")
#     print()


"""Line LCS_Mat analysis"""
# for r in range(lenSeq + 1):
#     for c in range(r, lenSeq + 1):
#         if (r == 0 or c == 0 or (r == c)):
#             LCS_Mat[r][c] = 0
#
#         elif (seq[r-1] == seq[c-1]):
#             LCS_Mat[r][c] = LCS_Mat[r-1][c-1] + 1
#             # maxSeq[mSCnt].append(seq[r-1])
#             # mSCon = True
#
#             if LCS_Mat[r][c] > fnd_res:
#                 fnd_index = [r, c]
#             fnd_res = max(fnd_res, LCS_Mat[r][c])
#
#         else:
#             # if mSCon:
#             #     maxSeq.append([])
#             #     mSCnt += 1
#             #     mSCon = False
#
#             LCS_Mat[r][c] = 0


"""Whole line LCS_Mat analysis"""
for i in range(lenSeq+1):
    for j in range(lenSeq+1):
        if (i == 0 or j == 0 or (i == j)):
            LCS_Mat[i][j] = 0

        elif (seq[i-1] == seq[j-1]):
            LCS_Mat[i][j] = LCS_Mat[i-1][j-1] + 1

            if LCS_Mat[i][j] > fnd_res:
                fnd_index = [i, j]
            fnd_res = max(fnd_res, LCS_Mat[i][j])

        else:
            LCS_Mat[i][j] = 0

fnd_index = [fnd_index[0] - fnd_res, fnd_index[1] - fnd_res]
fnd_seq = seq[fnd_index[0]:fnd_index[0] + fnd_res]


print("Raw Result seq len:", fnd_res)
print("\tRaw Result seq.:", fnd_seq)
print(f"\tRaw Result seq. coords: <{fnd_index[0]}, {fnd_index[0] + fnd_res - 1}> <{fnd_index[1]}, {fnd_index[1] + fnd_res - 1}>")

print()
if (fnd_index[1] - (fnd_index[0] + fnd_res)) < 0:
    print("\n! Sequences overlap !\n")
    overlap = fnd_index[1] - (fnd_index[0] + fnd_res)
    # print(overlap)

    fnd_res += overlap
    fnd_seq = seq[fnd_index[0]:fnd_index[0] + fnd_res]

    print("Cor. Result seq len:", fnd_res)
    print("\tCor. Result seq.:", fnd_seq)
    print(f"\tCor. Result seq. coords: <{fnd_index[0]}, {fnd_index[0] + fnd_res - 1}> <{fnd_index[1]}, {fnd_index[1] + fnd_res - 1}>")

result_seq = seqMax(fnd_seq)
result = len(result_seq)
result_sum = sumArr(result_seq)

print()
print("Result length:", result)
print("\tResult sum:", result_sum)
print("\tResult seq.:", result_seq)

LCS_1Vis(seq, LCS_Mat)

# print("\n\n\t   |", end="")
# for b in range(lenSeq):
#     print(f" {seq[b]:2} |", end="")
# print("\n\t", end="")
#
# for r in range(1, lenSeq + 2):
#     print(" --", end="")
#     for b in range(1, lenSeq + 1):
#         print("+----", end="")
#     print("+\n\t", end="")
#     # print()
#
#     if r == lenSeq+1:
#         break
#     print(f"{seq[r-1]:2} ", end="")
#
#     for c in range(1, lenSeq + 1):
#
#         # print(f"| {LCS_Mat[r][c]:2} ", end="")
#
#         if LCS_Mat[r][c]:
#             print(f"| {LCS_Mat[r][c]:2} ", end="")
#         else:
#             print(f"|    ", end="")
#
#
#     print("|\n\t", end="")

