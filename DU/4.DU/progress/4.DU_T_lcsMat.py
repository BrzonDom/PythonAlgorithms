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
            # elif r == c:
            #     print(f"| ## ", end="")

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

str_seq_list = ["3 3 3 3 3 3 3 3 3",
                "1 1 1 6 2 2 2 6 1 1 1",
                "1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3",
                "1 2 3 4 4 4 4 4 3 2 1",
                "1 2 5 -6 8 -3 2 5 -6 8 -3 2 3",
                "1 2 3 5 -6 8 -3 2 3 5 -6 8 -3 2 3"]

str_seq = str_seq_list[1]

seq = [int(num) for num in list(str_seq.split(" "))]

lenSeq = len(seq)

maxLenSeq = lenSeq // 2

print(f"Sequence: {seq}")
print(f"\tSeq Len:      {lenSeq}")
print(f"\tMax Len Seq:  {lenSeq // 2}\n")


LCS_Mat = [[0 for i in range(lenSeq + 1)] for j in range(lenSeq + 1)]


"""Line LCS_Mat analysis"""
# fnd_res = 0
# fnd_index = []

# for r in range(lenSeq + 1):
#     for c in range(r, lenSeq + 1):
#         if (r == 0 or c == 0 or (r == c)):
#             LCS_Mat[r][c] = 0
#
#         elif (seq[r-1] == seq[c-1]):
#             LCS_Mat[r][c] = LCS_Mat[r-1][c-1] + 1
#
#             if LCS_Mat[r][c] > fnd_res:
#                 fnd_index = [r, c]
#             fnd_res = max(fnd_res, LCS_Mat[r][c])
#
#         else:
#             LCS_Mat[r][c] = 0


"""Diagonal LSC_Mat analysis"""
full = 0
ad = 0 - full
diaSeq = []
diaSeq_list = []

fnd_res = 0
fnd_index = []

for row in range(lenSeq + full, 0, -1):
    ad += 1
    for col in range(1, row):

        if (seq[col - 1] == seq[col + ad - 1]):
            LCS_Mat[col][col + ad] = LCS_Mat[col - 1][col + ad - 1] + 1

            diaSeq.append(seq[col - 1])
            diaSeq_list.append(copy.deepcopy(diaSeq))

            if LCS_Mat[col][col + ad] > fnd_res:
                fnd_index = [col, col + ad]
            fnd_res = max(fnd_res, LCS_Mat[col][col + ad])

        else:
            if diaSeq:
                # print(diaSeq, end=" ")
                diaSeq = []
    if diaSeq:
        # print(diaSeq, end=" ")
        diaSeq = []
        """Diagonal coordinates print"""
    #     print(f"({col}, {col + ad}) ", end=" ")
    # print()
print()


LCS_1Vis(seq, LCS_Mat)

