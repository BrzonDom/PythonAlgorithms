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

str_seq1 = "3 3 3 3 3 3 3 3 3"
str_seq2 = "1 1 1 6 2 2 2 6 1 1 1"
str_seq3 = "1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3"
str_seq = ["3 3 3 3 3 3 3 3 3", "1 1 1 6 2 2 2 6 1 1 1", "1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3"]

seq1 = [int(num) for num in list(str_seq1.split(" "))]
seq2 = [int(num) for num in list(str_seq2.split(" "))]
seq3 = [int(num) for num in list(str_seq3.split(" "))]

print(seq1)
print(seq2)
print(seq3)

print()

len_seq1 = len(seq1)
len_seq2 = len(seq2)
len_seq3 = len(seq3)

print(f"Len_Seq 1: {len_seq1} // 2 = {len_seq1 // 2}")
print(f"Len_Seq 2: {len_seq2} // 2 = {len_seq2 // 2}")
print(f"Len_Seq 3: {len_seq3} // 2 = {len_seq3 // 2}")

LCS_Mat = [[0 for i in range(len_seq3+1)] for j in range(len_seq3+1)]

TST_Mat = [[1, 0, 0, 1],
           [0, 2, 0, 0],
           [0, 3, 4, 0],
           [0, 0, 0, 5]]

tstLen = len(TST_Mat)

# print(LCS_Mat)

result = 0
res_index = []

for i in range(len_seq3+1):
    for j in range(len_seq3+1):
        if (i == 0 or j == 0):
            LCS_Mat[i][j] = 0
        elif (seq3[i-1] == seq3[j-1]):
            LCS_Mat[i][j] = LCS_Mat[i-1][j-1] + 1
            if LCS_Mat[i][j] > result:
                res_index = [i, j]
            result = max(result, LCS_Mat[i][j])
        else:
            LCS_Mat[i][j] = 0

# print("\n\t", end="")
# # print()
#
# for r in range(tstLen+1):
#     for b in range(tstLen):
#         print("+---", end="")
#     print("+\n\t", end="")
#
#     if r == tstLen:
#         break
#
#     for c in range(tstLen):
#         # for b in range(tstLen):
#         #     print("+---", end="")
#         # print("+")
#         print("| ", end="")
#         print(TST_Mat[r][c], end=" ")
#
#     print("|\n\t", end="")



print("\n\n\t   |", end="")
for b in range(len_seq3):
    print(f" {seq3[b]:2} |", end="")
print("\n\t", end="")

for r in range(1, len_seq3+2):
    print(" --", end="")
    for b in range(1, len_seq3+1):
        print("+----", end="")
    print("+\n\t", end="")
    # print()

    if r == len_seq3+1:
        break
    print(f"{seq3[r-1]:2} ", end="")

    for c in range(1, len_seq3+1):
        # for b in range(tstLen):
        #     print("+---", end="")
        # print("+")
        print(f"| {LCS_Mat[r][c]:2} ", end="")
        # print(LCS_Mat[r][c], end=" ")

    print("|\n\t", end="")



# for i in range(2*(len_seq3+1)):
#     for j in range(2*(len_seq3+1)):
#
#         if j == 0:
#             if i % 2 == 0:
#                 print("+", end="")
#             else:
#                 print("|", end="")
#         else:
#             if i % 2 == 0:
#                 print("---+", end="")
#             else:
#                 print("   |", end="")
#     print("\n\t", end="")

# for r in range(len_seq3+1):
#     for c in range(len_seq3+1):
#         for p in range(len_seq3+1):
#             print("+---", end="")
#         print("+")
#
#         print("| ", end="")



# for i in range(len_seq3+1):
#     for j in range(len_seq3+1):
#         if i != 0 and j != 0:
#             print(f"{LCS_Mat[i][j]:2d}", end=" ")
#     print()

# result = 0
#
#
# for i in range(len_seq3+1):
#     for j in range(i, len_seq3+1):
#         if i == j:
#             continue

