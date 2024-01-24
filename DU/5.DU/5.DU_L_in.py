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


def coL(num):
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


def coN(num):
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


#
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 8
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 7
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 6
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 5
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 4
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 3
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 2
# print("+---+---+---+---+---+---+---+---+")
# print("|   |   |   |   |   |   |   |   |") # 1
# print("+---+---+---+---+---+---+---+---+")
#     #    a   b   c   d   e   f   g   h

# coN = {
#     7 : "1",
#     6 : "2",
#     5 : "3",
#     4 : "5",
#     3 : "4",
#     2 : "6",
#     1 : "7",
#     0 : "8" }
# #
# coL = {
#     0 : "a",
#     1 : "b",
#     2 : "c",
#     3 : "d",
#     4 : "e",
#     5 : "f",
#     6 : "g",
#     7 : "h" }

board = [[0 for i in range(8 + 2)] for j in range(8 + 2)]

# for i in range(10):
#     for j in range(10):
#         if (i == 0 or j == 0 or i == 10 or j == 10):


input_board = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 3, 0, 0, 0, 0, 0, 0],
               [1, 0, 0, 0, 0, 0, 0, 0]]

# print()

# for i in range(9):
#     for j in range(9):
#         if (i == 0 or j == 0):
#             continue
#         print(board[i][j], end=" ")
#     print()
#
# print("\n")


for i in range(8):
    for j in range(8):
        board[i + 1][j + 1] = input_board[i][j]
        print(board[i + 1][j + 1], end=" ")
    print()

moves = []
coord_list = []
boarder = [0, 1, 2, 3, 4, 5, 6, 7]
move_Cnt = 0

for r in range(8):
    for c in range(8):
        if input_board[r][c] == 1:
            coord_list.append(coL(c) + coN(r))
            moves.append([r, c])

            while (True):
                if (moves[move_Cnt][0] - 1) in boarder and (moves[move_Cnt][1] - 1) in boarder:
                    if input_board[moves[move_Cnt][0] - 1][moves[move_Cnt][1] - 1] == 0:
                        moves.append([moves[move_Cnt][0] - 1, moves[move_Cnt][1] - 1])
                        coord_list.append(coL(moves[move_Cnt][1] - 1) + coN(moves[move_Cnt][0] - 1))
                        move_Cnt += 1
                        continue

                if (moves[move_Cnt][0] - 1) in boarder and (moves[move_Cnt][1] + 1) in boarder:
                    if input_board[moves[move_Cnt][0] - 1][moves[move_Cnt][1] + 1] == 0:
                        moves.append([moves[move_Cnt][0] - 1, moves[move_Cnt][1] + 1])
                        coord_list.append(coL(moves[move_Cnt][1] + 1) + coN(moves[move_Cnt][0] - 1))
                        move_Cnt += 1
                        continue

                if (moves[move_Cnt][0] - 2) in boarder and (moves[move_Cnt][1] - 2) in boarder:
                    if input_board[moves[move_Cnt][0] - 2][moves[move_Cnt][1] - 2] == 0:
                        moves.append([moves[move_Cnt][0] - 2, moves[move_Cnt][1] - 2])
                        coord_list.append(coL(moves[move_Cnt][1] - 2) + coN(moves[move_Cnt][0] - 2))
                        move_Cnt += 1
                        continue

                if (moves[move_Cnt][0] - 2) in boarder and (moves[move_Cnt][1] + 2) in boarder:
                    if input_board[moves[move_Cnt][0] - 2][moves[move_Cnt][1] + 2] == 0:
                        moves.append([moves[move_Cnt][0] - 2, moves[move_Cnt][1] + 2])
                        coord_list.append(coL(moves[move_Cnt][1] + 2) + coN(moves[move_Cnt][0] - 2))
                        move_Cnt += 1
                        continue
                break

            # if (r-1) in boarder and (c-1) in boarder:
            #     if not

            # if (r == 0):
            #     continue
            # # elif (c == 0):
            # #     if input_board[r+1][c+1] == 0:

# print(moves)
"""
legal move checks



"""