"""
Těžká varianta

    Nejdříve si přečtěte zadání lehké úlohy.
    Napište program dama_max.py, který načte matici celých čísel ze souboru, jehož jméno je zadáno jako první argument programu sys.argv[1] a najde kamen (obyčejný kamen, nebo dámu) která může provést nejdelší skok. Délku skoku určuje nejdříve počet kamenů černého, které při skoku zajme. V přípedě, že dva různé skoky zajmou stejný počet černých kamenů pak o délce skoku záleží na počtu políček, které kamen při braní urazí.
    Pokud existují skoky se stejnou délkou, vytiskněte libovolný z nich.
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

        Bílý je na tahu a program najde kamen, který provede nejdelší skok.
        Uvažujte všechna pravidla České dámy (Dáma (desková hra))
            Oproti lehké variantě přidáme pohyb dámy. Dáma se pohybuje úhlopříčně libovolným směrem.
            Dáma může skočit, pokud jsoou na diagonále volná pole a hned za nimi sousední pole obsazené cizím kamenem nebo dámou a následující pole za obsazeným polem je volné, pak dáma může skočit na libovolné volné pole za cizím kamen.
            Cizí kamen (nebo kameny) se odstraní, až když tah dámy skončí. Cizí kamen lze přeskočit při jednom tahu pouze jednou.
            Jak bylo uvedeno výše, délka skoku závisí nejvíce na počtu braných kamenů, v případě shody v počtu braných kamenů rozhoduje počet polí, která dáma, nebo kamen musel překonat (i když to vede k nevýhodné situaci pro bílého).
            V následujících obrázcích jsou černě značeny nejdelší skoky, modře skoky kratší:


    Výstup:
            Program vytiskne na jeden řádek souřadnice kamenu, který skočil a všechna místa, kam skočil (míst je víc pro vícenásobný skok)
        Program v souboru dama_max.py odevzdejte pomocí odevzdávacího systému (úloha HW05).
        Můžete předpokládat, že všechny matice jsou zadány korektně, tedy všechny řádky mají stejný počet prvků a obsahují pouze celá čísla od 0 do 4.

"""

import copy


def inBoard(coord):

    return 0 <= coord <= 7


def nextMoves(tile, prevTiles):

    if inBoard(tile[0] - 2) and inBoard(tile[1] - 2):
        if board[tile[0] - 2][tile[1] - 2] == 0 and board[tile[0] - 1][tile[1] - 1] not in [0, 1, 2]:
            # moves.append([tile[0] - 2, tile[1] - 2])
            # move_que.append([tile[0] - 2, tile[1] - 2])

            newTiles = copy.deepcopy(prevTiles)
            newTiles.append([tile[0] - 2, tile[1] - 2])

            nextMoves([tile[0] - 2, tile[1] - 2], newTiles)

    if inBoard(tile[0] - 2) and inBoard(tile[1] + 2):
        if board[tile[0] - 2][tile[1] + 2] == 0 and board[tile[0] - 1][tile[1] + 1] not in [0, 1, 2]:
            # moves.append([tile[0] - 2, tile[1] + 2])
            # move_que.append([tile[0] - 2, tile[1] + 2])

            newTiles = copy.deepcopy(prevTiles)
            newTiles.append([tile[0] - 2, tile[1] + 2])

            nextMoves([tile[0] - 2, tile[1] + 2], newTiles)

    moves_lst.append(prevTiles)

def prtRes(resLst, addRes):
    resMovPrt = ""

    print(f"\tStart tile: {coCon(resLst[0])} {resLst[0]}")
    print(f"\t\t\t{len(resLst) - 1} Moves: ", end="")

    for moves in resLst[1:]:
        # print(f"{coCL[mov[1]]}{coRN[mov[0]]} {moves_res[0]}", end="  ")

        resMovPrt += f"{coCon(moves)} {moves} ,  "

        if addRes:
            if moves not in moves_res:
                moves_res.append(moves)

    if resMovPrt:
        print(resMovPrt[:-3])
    print("\n")


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



file_list = ["setup_T_01", "setup_T_02", "setup_T_03"]

inOp = 0

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

print("! Checkers with ONLY jumping allowed !\n")

print("\tInput board:\n")

print("", end="\t\t")
for row in board:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t\t")
print()


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
            nextMoves(tile, [tile])

# for moves in moves_lst:
#     print(moves)


moves_res = []
moves_otRes = []
moves_all = []
moves_strt = []
tileStrt = []
tileCnt = 0
resCnt = 1

print("Paths found:")

for moves_pth in moves_lst:

    if len(moves_res) < len(moves_pth):
        moves_res = copy.deepcopy(moves_pth)
        moves_otRes = []
        resCnt = 1

    elif len(moves_res) == len(moves_pth):
        resCnt += 1
        moves_otRes.append(copy.deepcopy(moves_pth))

    for m, moves in enumerate(moves_pth):

        if not m:
            if tileStrt != moves:
                tileStrt = copy.deepcopy(moves)

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
print("\n")


print("Result:\n")

prtRes(moves_res, False)

if moves_otRes:
    print(f"{resCnt-1} other results:\n")
    for otRes in moves_otRes:
        prtRes(otRes, True)


print("", end="   ")
for i in range(8):
    print(coCL[i], end=" ")
print()

for r in range(8):
    print(8 - r, end=" ")
    for c in range(8):
        # print(f"{r}{c}", end=" ")
        if board[r][c] == 1:
            print("🟥", end="")
        elif [r, c] in moves_res:
            print("🟨", end="")
        elif [r, c] in moves_all:
            print("🟩", end="")
        elif board[r][c] in (3, 4):
            print("⬛", end="")
        else:
            print("⬜", end="")
    print()
print()

print("Explanatory note:")
print("\t⬜ = empty tile")
print("\t🟥 = your pieces")
print("\t⬛ = opponent's pieces")
print("\t🟩 = possible moves")
print("\t🟨 = path of longest possible move")