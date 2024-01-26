"""
Lehká varianta

    Napište program dama_tah.py, který načte matici celých čísel ze souboru, jehož jméno je zadáno jako první argument programu sys.argv[1] a zjistí, zda existuje bílý kamen, který může skočit přes nějaký černý kámen. Pokud takový kámen existuje, pak vypíše tah bílého v šachových souřadnicích.

    Vstup:

        První argument programu obsahuje jméno souboru.
        Soubor obsahuje matici 8×8

        - celých čísel s tímto významem:
            0 - volné pole
            1 - bílý kámen
            2 - bílá dáma
            3 - černý kámen
            4 - černá dáma
        Pole na šachovnici odpovídají tomu, že první řádek matice představuje řadu 8, druhý řádek reprezentuje řadu 7, … , poslední řádek v souboru reprezentuje řádek 1. Sloupce jsou označeny písmeny a,…,g.

    Úkol:

        Bílý je na tahu a program najde kamen, který může skočit.
        Na šachovnici je v této úloze vždy jen jeden kamen, který může skočit.
        V tomto programu lehké varianty uvažujte pouze pohyb bílého kamene, šachovnice nebudou obsahovat bílou dámu. Tah odpovídá pravidlům České dámy (Dáma (desková hra))
            Bílý kámen se pohybuje pouze “nahoru”, tedy pouze směrem k vyšším číslům řad.
            Kameny se pohybují po úhlopříčkách na sousední volné pole.
            Kamen může skočit, pokud je sousední pole obsazené cizím kamenem nebo dámou a následující pole za obsazeným polem je volné, pak kamen může skočit na volné pole a cizí kamen je z šachovnice odstraněn.

        Pokud kamen po skoku může ještě jednou skočit, pak lze tento skok také provést a opakovat skok, dokud je možné skákat.


    Výstup:
        Program vytiskne na jeden řádek souřadnice kamenu, který skočil a všechna místa, kam skočil (míst je víc pro vícenásobný skok)
        Příklad pro výše uvedené šachovnice bude výstup programu:
            a1 c3
            a1 c3 a5
        Program v souboru dama_tah.py odevzdejte pomocí odevzdávacího systému (úloha HW05).
        Můžete předpokládat, že všechny matice jsou zadány korektně, tedy všechny řádky mají stejný počet prvků.
        Pokud se vstupní soubor jmenuje dama.txt, Váš program můžete spustit příkazem python3 dama_tah.py dama.txt.
        Soubor s šachovnicí můžete otevřít takto:

            import sys
            sachovnice = open(sys.argv[1], "rt")

"""
import copy

"""
Příklady:
    Vstup:
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 3 0 0 0 0 0 0
        1 0 0 0 0 0 0 0
    Výstup:
        a1 c3

    Vstup:
        0 0 0 0 0 0 0 3
        0 0 0 0 0 0 4 0
        0 0 0 0 0 1 0 0
        1 0 3 0 3 0 4 0
        0 3 0 0 0 0 0 0
        1 0 0 0 4 0 0 0
        0 3 0 3 0 0 0 1
        1 0 1 0 0 0 0 0
    Výstup:
        a1 c3

    Vstup:
        0 0 0 0 0 0 0 3
        0 0 0 0 0 0 4 0
        0 3 0 0 0 1 0 0
        0 0 3 0 3 0 4 0
        0 3 0 0 0 0 0 0
        1 0 0 0 4 0 0 0
        0 3 0 3 0 0 0 1
        1 0 1 0 0 0 0 0
    Výstup:
        a1 c3 a5 c7
"""


def coCL(num):
    coordLet_dict = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }
    coord = coordLet_dict[num]
    return coord


def coRN(num):
    coordNum_dict = {
        7: "1",
        6: "2",
        5: "3",
        4: "5",
        3: "4",
        2: "6",
        1: "7",
        0: "8"
    }

    coord = coordNum_dict[num]
    return coord


file_list = ["setup_L_01", "setup_L_02", "setup_L_03"]

file_name = file_list[2]
# file_name = "setup_L_01"
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt\n")


board = [[0 for i in range(8 + 2)] for j in range(8 + 2)]

inBoard = []

for line in file:
    inBoard.append(list(map(int, line.split())))
file.close()

# for row in inBoard:
#     print(f"\t{row}")
# print()

print("", end="\t")
for row in inBoard:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

# input_board = [[0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 0],
#                [0, 3, 0, 0, 0, 0, 0, 0],
#                [1, 0, 0, 0, 0, 0, 0, 0]]

# print()
#
# for i in range(9):
#     for j in range(9):
#         if (i == 0 or j == 0):
#             continue
#         print(board[i][j], end=" ")
#     print()
#
# print("\n")
#
#
# for i in range(8):
#     for j in range(8):
#         board[i + 1][j + 1] = input_board[i][j]
#         print(board[i + 1][j + 1], end=" ")
#     print()
#
# moves = []
# coord_list = []
# boarder = [0, 1, 2, 3, 4, 5, 6, 7]
# move_Cnt = 0
#
# for r in range(8):
#     for c in range(8):
#         if inBoard[r][c] == 1:
#             coord_list.append(coCL(c) + coRN(r))
#             moves.append([r, c])
#
#             while (True):
#                 if (moves[move_Cnt][0] - 1) in boarder and (moves[move_Cnt][1] - 1) in boarder:
#                     if inBoard[moves[move_Cnt][0] - 1][moves[move_Cnt][1] - 1] == 0:
#                         moves.append([moves[move_Cnt][0] - 1, moves[move_Cnt][1] - 1])
#                         coord_list.append(coCL(moves[move_Cnt][1] - 1) + coRN(moves[move_Cnt][0] - 1))
#                         move_Cnt += 1
#                         continue
#
#                 if (moves[move_Cnt][0] - 1) in boarder and (moves[move_Cnt][1] + 1) in boarder:
#                     if inBoard[moves[move_Cnt][0] - 1][moves[move_Cnt][1] + 1] == 0:
#                         moves.append([moves[move_Cnt][0] - 1, moves[move_Cnt][1] + 1])
#                         coord_list.append(coCL(moves[move_Cnt][1] + 1) + coRN(moves[move_Cnt][0] - 1))
#                         move_Cnt += 1
#                         continue
#
#                 if (moves[move_Cnt][0] - 2) in boarder and (moves[move_Cnt][1] - 2) in boarder:
#                     if inBoard[moves[move_Cnt][0] - 2][moves[move_Cnt][1] - 2] == 0:
#                         moves.append([moves[move_Cnt][0] - 2, moves[move_Cnt][1] - 2])
#                         coord_list.append(coCL(moves[move_Cnt][1] - 2) + coRN(moves[move_Cnt][0] - 2))
#                         move_Cnt += 1
#                         continue
#
#                 if (moves[move_Cnt][0] - 2) in boarder and (moves[move_Cnt][1] + 2) in boarder:
#                     if inBoard[moves[move_Cnt][0] - 2][moves[move_Cnt][1] + 2] == 0:
#                         moves.append([moves[move_Cnt][0] - 2, moves[move_Cnt][1] + 2])
#                         coord_list.append(coCL(moves[move_Cnt][1] + 2) + coRN(moves[move_Cnt][0] - 2))
#                         move_Cnt += 1
#                         continue
#                 break

moves_list = []
move_stack = []
moveCnt = 0

boarder = [0, 1, 2, 3, 4, 5, 6, 7]


for r in range(8):
    for c in range(8):
        if inBoard[r][c] == 1:

            notJump = True

            moves_list.append([])
            moves = moves_list[len(moves_list) - 1]

            move_stack.append([r, c])
            moves.append([r, c])

            while(len(move_stack) > 0):
                move = [move_stack[0][0], move_stack[0][1]]
                move_stack.pop(0)

                # print(f"{move_Cnt}. {move[0]} , {move[1]}")
                if notJump:
                    if (move[0] - 1) in boarder and (move[1] - 1) in boarder:
                        if inBoard[move[0] - 1][move[1] - 1] == 0:
                            moves.append([move[0] - 1, move[1] - 1])
                            move_stack.append([move[0] - 1, move[1] - 1])


                    if (move[0] - 1) in boarder and (move[1] + 1) in boarder:
                        if inBoard[move[0] - 1][move[1] + 1] == 0:
                            moves.append([move[0] - 1, move[1] + 1])
                            move_stack.append([move[0] - 1, move[1] + 1])
                notJump = False


                if (move[0] - 2) in boarder and (move[1] - 2) in boarder:
                    if inBoard[move[0] - 2][move[1] - 2] == 0 and inBoard[move[0] - 1][move[1] - 1] not in [0, 1, 2]:
                        moves.append([move[0] - 2, move[1] - 2])
                        move_stack.append([move[0] - 2, move[1] - 2])


                if (move[0] - 2) in boarder and (move[1] + 2) in boarder:
                    if inBoard[move[0] - 2][move[1] + 2] == 0 and inBoard[move[0] - 1][move[1] + 1] not in [0, 1, 2]:
                        moves.append([move[0] - 2, move[1] + 2])
                        move_stack.append([move[0] - 2, move[1] + 2])


print()

moves_all = []
moves_res = []
for m, moves in enumerate(moves_list):

    if len(moves_res) < len(moves):
        moves_res = copy.deepcopy(moves)

    print(f"{m+1}.", end=" ")

    for mov in moves:
        moves_all.append(mov)
        print(f"{coCL(mov[1])}{coRN(mov[0])}:{mov}", end=" ")
    print()
print()

print("Result moves:", end="\n\t")
for mov in moves_res:
    print(f" {coCL(mov[1])}{coRN(mov[0])}", end="    ")
print("\n", end="\t")

for mov in moves_res:
    print(f"{mov}", end=" ")
print("\n")

# coords = []
# for m, move in enumerate(moves):
#     coords.append(coCL(move[1]) + coRN(move[0]))
#     # print(f"{move} : {coords[m]}", end="")
#
#     if (m+1) % 3 == 0:
#         print(f"{m+1:3}. {move} : {coords[m]}")
#     else:
#         print(f"{m+1:3}. {move} : {coords[m]}", end="    |    ")
#
# print("\n")
#

for r in range(8):
    for c in range(8):
        # print(f"{r}{c}", end=" ")
        if inBoard[r][c] == 1:
            print("🟥", end="")
        elif [r, c] in moves_res:
            print("🟨", end="")
        elif [r, c] in moves_all:
            print("🟩", end="")
        elif inBoard[r][c] in (3, 4):
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()

# print(moves)
