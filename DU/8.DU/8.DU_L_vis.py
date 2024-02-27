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
import math
from PIL import Image, ImageDraw


class myBoard:
    def __init__(self, size=0):
        self.size = size
        self.board = {}

        # create empty expBoard as a dictionary
        self.b2 = {}
        for p in range(-self.size, self.size):
            for q in range(-self.size, self.size):
                if self.inBoard(p, q):
                    if not p in self.board:
                        self.board[p] = {}
                    self.board[p][q] = 0

                    if not q in self.b2:
                        self.b2[q] = {}
                    self.b2[q][p] = 0

        # this is for visualization and to synchronize colors between png/js
        self._colors = {}
        self._colors[-1] = "#fdca40"  # sunglow
        self._colors[0] = "#ffffff"  # white
        self._colors[1] = "#947bd3"  # medium purple
        self._colors[2] = "#ff0000"  # red
        self._colors[3] = "#00ff00"  # green
        self._colors[4] = "#0000ff"  # blue
        self._colors[5] = "#566246"  # ebony
        self._colors[6] = "#a7c4c2"  # opan
        self._colors[7] = "#ADACB5"  # silver metalic
        self._colors[8] = "#8C705F"  # liver chestnut
        self._colors[9] = "#FA7921"  # pumpkin
        self._colors[10] = "#566E3D"  # dark olive green


    def inBoard(self, p, q):
        """ return True if (p,q) is valid coordinate """
        return (q >= 0) and (q < self.size) and (p >= -(q // 2)) and (p < (self.size - q // 2))


    def saveImage(self, filename):
        """ draw actual expBoard to png
        """

        cellRadius = 60
        cellWidth = int(cellRadius * (3 ** 0.5))
        cellHeight = 2 * cellRadius

        width = cellWidth * self.size + cellRadius * 3
        height = cellHeight * self.size

        img = Image.new('RGB', (width, height), "white")

        draw = ImageDraw.Draw(img)

        lineColor = (50, 50, 50)

        for p in self.board:
            for q in self.board[p]:
                cx = cellRadius * (math.sqrt(3) * p + math.sqrt(3) / 2 * q) + cellRadius
                cy = cellRadius * (0 * p + 3 / 2 * q) + cellRadius

                pts = []
                for a in [30, 90, 150, 210, 270, 330]:
                    nx = cx + cellRadius * math.cos(a * math.pi / 180)
                    ny = cy + cellRadius * math.sin(a * math.pi / 180)
                    pts.append(nx)
                    pts.append(ny)
                color = "#ff00ff"  # pink is for values out of range -1,..10
                if self.board[p][q] in self._colors:
                    color = self._colors[self.board[p][q]]

                draw.polygon(pts, fill=color)
                pts.append(pts[0])
                pts.append(pts[1])
                draw.line(pts, fill="black", width=1)
                draw.text([cx - 3, cy - 3], "{} {}".format(p, q), fill="black")
        img.save(filename)


def isIn(row, col, size):
    return (col >= 0) and (col < size) and (row >= -(col // 2)) and (row < (size - col // 2))


solBoard = []


def solve(board, piec_lst, piec_ind, size):

    if leftSpace(board) == 0:
        if board not in solBoard:

            solBoard.append(copy.deepcopy(board))
            print(board)
            # for row in expBoard:
            #     for col in expBoard[row]:
            #         print(expBoard[row][col], end=" ")
            #     print()
            # print()

    for row in range(len(board)):
        for col in range(len(board[0])):

            for p, piece in enumerate(piec_lst):
                if canPlace(board, [row, col], piece, size):

                    new_board = copy.deepcopy(board)

                    for block in piece:
                        rB = row + block[0]
                        cB = col + block[1]
                        new_board[rB][cB] = piec_ind[p]

                    # new_piec_list = copy.deepcopy(piec_lst)
                    # new_piec_list.remove(piece)
                    solve(new_board, piec_lst[:p] + piec_lst[p+1:], piec_ind[:p] + piec_ind[p+1:], size)

                    # for block in piece:
                    #     rB = row + block[0]
                    #     cB = col + block[1]
                    #     expBoard[rB][cB] = 0


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


file_name = "PrL_1"
fileOpen = "data\\" + file_name + ".txt"
fileWrite = "data\\" + file_name + "_out.txt"

size = 3
# expBoard = base.Board(size)
# stones = base.loadStones(fileOpen)

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


board = {}
for p in range(-size, size):
    for q in range(-size, size):

        if isIn(p, q, size):
            if not p in board:
                board[p] = {}

            board[p][q] = 0

print()
print(board)

stones = copy.deepcopy(stones_In)

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

"""     Visual print    """
visCnt = 1

for dict in solBoard:
    print(type(dict))
    print(dict)
    print()

    inOut_board = myBoard(size)
    inOut_board.board = dict
    inOut_board.saveImage(f"visual\\{file_name}.{visCnt}_out.png")

    visCnt += 1
