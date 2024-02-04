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

import copy


def inBoard(coord):

    return 0 <= coord <= 7


def nextMoves(tile, noJump, prevTiles):

    if noJump:
        if inBoard(tile[0] - 1) and inBoard(tile[1] - 1):
            if board[tile[0] - 1][tile[1] - 1] == 0:
                # moves.append([tile[0] - 1, tile[1] - 1])
                # move_que.append([tile[0] - 1, tile[1] - 1])

                newTiles = copy.deepcopy(prevTiles)
                newTiles.append([tile[0] - 1, tile[1] - 1])

                nextMoves([tile[0] - 1, tile[1] - 1], False, newTiles)

        if inBoard(tile[0] - 1) and inBoard(tile[1] + 1):
            if board[tile[0] - 1][tile[1] + 1] == 0:
                # moves.append([tile[0] - 1, tile[1] + 1])
                # move_que.append([tile[0] - 1, tile[1] + 1])
                newTiles = copy.deepcopy(prevTiles)
                newTiles.append([tile[0] - 1, tile[1] + 1])

                nextMoves([tile[0] - 1, tile[1] + 1], False, newTiles)
    noJump = False

    if inBoard(tile[0] - 2) and inBoard(tile[1] - 2):
        if board[tile[0] - 2][tile[1] - 2] == 0 and board[tile[0] - 1][tile[1] - 1] not in [0, 1, 2]:
            # moves.append([tile[0] - 2, tile[1] - 2])
            # move_que.append([tile[0] - 2, tile[1] - 2])

            newTiles = copy.deepcopy(prevTiles)
            newTiles.append([tile[0] - 2, tile[1] - 2])

            nextMoves([tile[0] - 2, tile[1] - 2], False, newTiles)

    if inBoard(tile[0] - 2) and inBoard(tile[1] + 2):
        if board[tile[0] - 2][tile[1] + 2] == 0 and board[tile[0] - 1][tile[1] + 1] not in [0, 1, 2]:
            # moves.append([tile[0] - 2, tile[1] + 2])
            # move_que.append([tile[0] - 2, tile[1] + 2])

            newTiles = copy.deepcopy(prevTiles)
            newTiles.append([tile[0] - 2, tile[1] + 2])

            nextMoves([tile[0] - 2, tile[1] - 2], False, newTiles)

    moves_lst.append(prevTiles)



def coCon(coord):

    return coCL[coord[1]] + coRN[coord[0]]



"""     dictionary for coordinates
    column to letter    """
coCL = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

"""     dictionary for coordinates
    row to number   """
coRN = {
    7: "1",
    6: "2",
    5: "3",
    4: "5",
    3: "4",
    2: "6",
    1: "7",
    0: "8"
}



file_list = ["setup_L_01", "setup_L_02", "setup_L_03",
             "setup_myL_04", "setup_myL_05", "setup_myL_06"]

inOp = 5

file_name = file_list[inOp]
# file_name = "setup_L_01"
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt\n")


"""     Expanded expBoard      """
# expBoard = [[0 for i in range(8 + 2)] for j in range(8 + 2)]

board = []

for line in file:
    board.append(list(map(int, line.split())))
file.close()

for row in board:
    print(f"\t{row}")
print("\n")

# print("", end="\t")
# for row in expBoard:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()


moves_lst = []
# moves_tile = []
# tileCnt = 0

# move_que = []
# moveCnt = 0

# boarder = [0, 1, 2, 3, 4, 5, 6, 7]


for r in range(8):
    for c in range(8):
        if board[r][c] == 1:
            """     Found white piece   """

            """     Bool-val to ensure 
                not repeating a sliding move     """
            # notJump = True
            # moves_tile.append([[r, c]])
            tile = [r, c]

            # def nextMoves(tile, noJump, prevTiles):
            nextMoves(tile, True, [tile])

# for moves in moves_lst:
#     print(moves)


moves_res = []
moves_all = []
moves_strt = []
tileStrt = []
tileCnt = 0

print("Paths found:")

for moves_pth in moves_lst:

    if len(moves_res) < len(moves_pth):
        moves_res = copy.deepcopy(moves_pth)

    for m, moves in enumerate(moves_pth):

        if not m:
            if tileStrt != moves:
                tileStrt = copy.deepcopy(moves)
                moves_strt.append(tileStrt)
                print(f"\n\tFor tile: {coCon(moves)} {moves}")
            print("\t\t", end="\t\t\t")
        elif moves:

            """
                {m+1} = Num. of found white piece
                {coCL[moves[0][1]]}{coRN[moves[0][0]]} = Starting expBoard coordinates
                {moves[0]} = Starting matrix coordinates
            """
            print(f"{coCon(moves)} {moves}", end="  ")

        if moves not in moves_all:
            moves_all.append(moves)

    print()
# print(moves_res)

print("Result:")
resMovPrt = ""

print(f"\tStart tile: {coCL[moves_res[0][0]]}{coRN[moves_res[0][1]]} {moves_res[0]}")
print(f"\t\t\t{len(moves_res)-1} Moves: ", end="")
for moves in moves_res[1:]:
    # print(f"{coCL[mov[1]]}{coRN[mov[0]]} {moves_res[0]}", end="  ")

    resMovPrt += f"{coCon(moves)} {moves} ,  "

if resMovPrt:
    print(resMovPrt[:-2])
print("\n")
