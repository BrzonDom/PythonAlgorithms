"""
    Tématem úlohy je napsat program tile_easy.py, který vyplní hexagonální hrací desku zadanými kameny

    Úkolem je vyplnit hrací desku o velikosti 4×4 (4-řádky, každý řádek 4 pole). Všechna řešení jsou

    Vstup programu: argumenty příkazové řádky
        první argument: velikost hrací desky (jedno celé číslo) určující jak počet řádků tak i počet sloupců
        druhý argument: jméno vstupního souboru s hracími kameny (je zaručeno, že existuje, že obsahuje alespoň jeden kamen a obsahuje správně zadané kameny)
        třetí argument: jméno výstupního souboru
    Program nalezne kombinaci kamenů na hrací desce tak, aby každé políčko bylo vyplněno právě jedním kamenem
    V lehké variantě domácí úlohy je povolena pouze translace kamenů, tedy je zakázáno kameny otáčet
    Je možné použít všechny kameny, ale není to nutné. Každý kamen se ale použije nejvýše jednou.
    Pokud je nějaký kamen použit, musí se celý vejít do hrací desky, nesmí přečnívat přes hrací desku ani se nesmí překrývat s jiným kamenem
    Program do výstupního souboru vypíše:
        právě jedno řešení - libovolné ze všech existujících řešení
            Výstup programu se zapisuje do výstupního souboru takto:
                každý řádek obsahuje tři celá čísla ve tvaru 'p q i', kde (p,q) je celočíselná souřadnice na hrací desce a 'i' je index kamene, který tuto buňku obarvuje
                kameny jsou číslovány od jedničky podle pořadí ve vstupním souboru (kamen definován na první řádce bude barvit na 1, kamen na druhá řádce obarvuje hodnotou 2 atd..)
        NOSOLUTION, pokud žádné neexistuje
            pokud řešení neexistuje, obsahuje soubor pouze jednu řádku s textem 'NOSOLUTION'
    Program odevzdejte jako tile_easy.py do HW08
    Timeout je nastaven dostatečně, pokud by Váš program měl problémy s časovým omezením, kontaktujte nás na fóru předmětu.
    Jak bude hodnoceno:
        Vyřešení hrací desky o velikosti 3×3, počet kamenů 2 až 4 (0.4b)
        Vyřešení hrací desky o velikosti 4×4, počet kamenů 3 až 5 (0.4b)
        Vyřešení hrací desky o velikosti 5×5, počet kamenů 2 až 6 (0.4b)
        Správná detekce hrací desky bez řešení (0.3b)

    Nápověda a pomocný program

        Obtížnost této úlohy spočívá jednak v tom, jak najít vhodné poskládání kamenů, které zcela pokrývá hrací desku, a také v tom, jak pracovat s hexagonálním gridem
        Pro usnadnění práce na domácí úloze si stáhněte program base.py (na konci této stránky), který vám nabízí užitečné nástroje

"""
import copy
import base

solBoard = []

def solve(board, piec_lst, piec_ind, size):

    if leftSpace(board) == 0:
        if board not in solBoard:

            solBoard.append(copy.deepcopy(board))
            print(board)
            # for row in board:
            #     for col in board[row]:
            #         print(board[row][col], end=" ")
            #     print()
            # print()

    for row in range(len(board)):
        for col in range(len(board[0])):

            for p, piece in enumerate(piec_lst):
                if canPlace(board, [row, col], piece, size):

                    new_board = copy.deepcopy(board)

                    for b, block in enumerate(piece):
                        rB = row + block[0]
                        cB = col + block[1]
                        new_board[rB][cB] = piec_ind[p]

                    # new_piec_list = copy.deepcopy(piec_lst)
                    # new_piec_list.remove(piece)
                    solve(new_board, piec_lst[:p] + piec_lst[p+1:], piec_ind[:p] + piec_ind[p+1:], size)

                    # for block in piece:
                    #     rB = row + block[0]
                    #     cB = col + block[1]
                    #     board[rB][cB] = 0


def isIn(row, col, size):
    return (col >= 0) and (col < size) and (row >= -(col // 2)) and (row < (size - col // 2))


def canPlace(board, coord, piece, size):
    rwCo = coord[0]
    clCo = coord[1]

    for block in piece:
        rwBl = rwCo + block[0]
        clBl = clCo + block[1]

        if isIn(rwBl, clBl, size):
            if board[rwBl][clBl] != 0:
                return False
        else:
            return False

    return True


def leftSpace(board):

    spaces = 0

    for row in board:
        for col in board[row]:
            if board[row][col] == 0:
                spaces += 1

    return spaces



file_name = "PrL_2"
fileOpen = "data\\" + file_name + ".txt"
fileWrite = "data\\" + file_name + "_out.txt"

size = 4
# board = base.Board(size)
# stones_In = base.loadStones(fileOpen)

print(f"File: {file_name}.txt")

file = open(fileOpen, "r")
data = []

for str_line in file:

    line = list(map(int, str_line.split()))
    print("\t", end="")
    for itm in line:
        print(itm, end=" ")
    print()
    data.append(line)

file.close()

stones_In = []

for st in range(len(data)):
    stones_In.append([])
    for stCo in range(0, len(data[st]),  2):
        # print(stCo, end=" ")
        stones_In[st].append([data[st][stCo], data[st][stCo + 1]])
        # # print(data[st][stCo], end=" ")
    # print(stones[st])

# print(stones)


board = {}
for p in range(-size, size):
    for q in range(-size, size):

        if isIn(p, q, size):
            if not p in board:
                board[p] = {}

            board[p][q] = 0

print()
print(board)
print()


stones = copy.deepcopy(stones_In)
# for stone in stones:
#     print(stone)
# print()


"""     Shift till in board     """

# pShift = True
# qShift = True

# while not [0, 0] in stone:
    # if not (pShift or qShift):
    #     break
    #
    # pShift = True
    #
    # for block in stone:
    #     rBl = block[0]
    #     cBl = block[1]
    #
    #     if not isIn(rBl-1, cBl, 5):
    #         pShift = False
    #
    # if pShift:
    #     for block in stone:
    #         block[0] -= 1
    #
    # qShift = True
    #
    # for block in stone:
    #     rBl = block[0]
    #     cBl = block[1]
    #
    #     if not isIn(rBl, cBl-1, 5):
    #         qShift = False
    #
    # if qShift:
    #     for block in stone:
    #         block[1] -= 1


"""     Shift using min path    """
for stone in stones:
    # print(stone[0], end="\n\t")
    # print(stone)

    min = stone[0][1]
    if stone[0][0] > 0:
        min += stone[0][0]

    min_co = [stone[0][0], stone[0][1]]

    for block in stone[1:]:

        sum = block[1]
        if block[0] > 0:
            sum += block[0]

        if sum < min:
            min = sum
            min_co = [block[0], block[1]]

    if min:
        for block in stone:
            block[0] -= min_co[0]
            block[1] -= min_co[1]

    # print(f"{min}, {min_co}")
    #     print(block, end=" ")
    # print()

print("Before shift:")
for stone in stones_In:
    print("\t", stone)
print()

print("After shift:")
for stone in stones:
    print("\t", stone)
# print(stone)


stones_index = []
print()
for s, stone in enumerate(stones):
    stones_index.append(s+1)
    print(f"{stones_index[-1]}:", end=" ")
    print(stone)

print()
solve(board, stones, stones_index, size)

print()
for sol in solBoard:
    for row in sol:
        for col in sol[row]:
            print(sol[row][col], end=" ")
        print()
    print()

# print(solBoard)

"""     Test leftSpace      """
# for p in range(-size, size):
#     for q in range(-size, size):
#
#         if isIn(p, q, size):
#             if not p in board:
#                 board[p] = {}
#
#             board[p][q] = 2
#
# print()
# print(board)
# board[1][2] = 0
# board[1][1] = 0
# print(board)
#
# print(leftSpace(board))

# space = 0
# for line in board:
#     # if board[line] == 0:
#     #     space += 1
#     for tile in board[line]:
#         if board[line][tile] == 0:
#             space += 1
#
#         # print(tile, end=" ")
#         # print(f"{tile} : {board[line][tile]}", end=" , ")
#     # print()


"""     Test can place      """

# # def canPlace(board, coord, piece, size):
# #     rwCo = coord[0]
# #     clCo = coord[1]
# #
# #     for block in piece:
# #         rwBl = rwCo + block[0]
# #         clBl = clCo + block[1]
# #
# #         if isIn(rwBl, clBl, size):
# #             if board[rwBl][clBl] != 0:
# #                 return False
# #         else:
# #             return False
# #
# #     return True
#
# print()
# stone = stones[1]
#
# for p in board:
#     for q in board[p]:
#
#         if canPlace(board, [p, q], stone, size):
#             for block in stone:
#                 pB = p + block[0]
#                 qB = q + block[1]
#                 board[pB][qB] = 1
#
#             print(board)
#             for pp in board:
#                 for qp in board[pp]:
#                     print(board[pp][qp], end=" ")
#                 print()
#             print()
#             for block in stone:
#                 pB = p + block[0]
#                 qB = q + block[1]
#                 board[pB][qB] = 0

    #     print(board[p][q], end=" ")
    # print()


# print(pShift)
# print(qShift)

# pShift = True
# qShift = True

# for stone in stones:
#     while pShift or qShift:
#         for block in stone:
#             rBl = block[0]
#             cBl = block[1]

            # if pShift:
            #     if isIn(rBl-1, cBl, 5):
            #         block[0] -= 1
            #     else:
            #         pShift = False
            #
            # if qShift:
            #     if isIn(rBl, cBl-1, 5):
            #         block[1] -= 1
            #     else:
            #         qShift = False
