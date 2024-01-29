import copy
import math
from PIL import Image, ImageDraw

# Uzitecne funkce a tridy pro praci s hexagonalnim gridem

"""

Vytvoreni prazneho gridu o velikosti 10x10:


b = Board(10)

# alternativa: nacteni ze souboru
b = Board(0)
b.loadBoard("soubor.txt")    


# prochazeni radku/sloupce:

for p in b.board:
   for q in b.board[q]:
      print("bunka", b.board[p][q] )


# zjisteni, jestli je nejaka bunka uvnitr:

p = 20
q = 10

if b.inBoard(p,q):
    print("Bunka je uvnitr")
else:    
    print("bunka je venku")

# ulozeni do png, bunky budou obarveny dle jejich hodnoty (0 = bila)


#provedene nejake obarveni, napriklad bunky, pro ktere neexistuje p+1 soused
for p in b.board:
    for q in b.board[p]:
        if not b.inBoard(p+1, q):  #pokud nema souseda p+11
             b.board[p][q] = 3

b.saveImage("soubor.png")  

"""


def loadStones(filename):
    f = open(filename, "r")
    stones = []
    for line in f:
        coords = list(map(int, line.rstrip().split()))
        if len(coords) > 0:
            stones.append([])
            for i in range(len(coords) // 2):
                x = coords[2 * i]
                y = coords[2 * i + 1]
                stones[-1].append([x, y])
    return stones;


class Board:
    def __init__(self, size=0):
        self.size = size
        self.board = {}

        # create empty board as a dictionary
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

    def rotateRight(self, p, q):
        pp = -q
        qq = p + q
        return pp, qq

    def rotateLeft(self, p, q):
        pp = p + q
        qq = -p
        return pp, qq

    def saveImage(self, filename):
        """ draw actual board to png
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

    def loadBoard(self, filename):
        board = {}
        fread = open(filename, "rt")
        size = -1
        for line in fread:
            p, q, value = list(map(int, line.strip().split()))
            size = max(size, q)
            if p not in board:
                board[p] = {}
            board[p][q] = value
        fread.close()
        self.board = board
        self.size = size + 1

# board = Board(size)
# for p in board.board:
#    if p.inBoard(p,0):
#        p.board[p][0] = 1
# board.saveImage("deska.png")

# b = Board(4)

file_list = ["PrL_1", "PrL_2", "DU8_PrL_1", "DU8_PrL_2"]

file_name = file_list[0]
# file_name = "eboard-7089"
file_path = "data\\" + file_name + ".txt"


# b = Board(0)
# Stones = b.loadBoard(file_path)
# print(Stones)
# Size = b.size
# print(f"Size: {Size}")

fin_board = {-4: {8: 0, 9: 0}, -3: {6: 0, 7: 0, 8: 0, 9: 0}, -2: {4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, -1: {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, 0: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, 1: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0}, 2: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 0}, 3: {0: 0, 1: 0, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 3, 8: 0, 9: 0}, 4: {0: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 0, 7: 0, 8: 0, 9: 0}, 5: {0: 0, 1: 0, 2: 0, 3: 3, 4: 0, 5: 3, 6: 0, 7: 0, 8: 0, 9: 0}, 6: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}, 7: {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}, 8: {0: 0, 1: 0, 2: 0, 3: 0}, 9: {0: 0, 1: 0}}
size = 10
# print(fin_board[3][5])

b = Board(size)
# board_dict = b.board
# print(board_dict)
#
b.board = fin_board
# print(b.board)

# Stone_list = loadStones(file_path)
# print(Stone_list)

b.saveImage(f"{file_name}_fin.png")