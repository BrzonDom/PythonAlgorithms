
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

file_list = ["PrL_1", "PrL_2", "PrL_3", "PrL_4"]

file_name = file_list[2]
file_folder = file_name + "_vis"

fileOpen = "visual\\" + file_name + ".txt"
print(f"File: {file_name}.txt")

size = 3

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
print()

print("Before shift:")
for stone in stones_In:
    print("\t", stone)
print()

print("After shift:")
for stone in stones:
    print("\t", stone)
# print(stone)

print()

stoneCnt = 0
posCnt = 0

for stone in stones:
    stoneCnt += 1
    posCnt = 0

    for p in board:
        for q in board[p]:

            if canPlace(board, [p, q], stone, size):
                posCnt += 1
                for block in stone:
                    pB = p + block[0]
                    qB = q + block[1]
                    board[pB][qB] = stoneCnt

                inOut_board = myBoard(size)
                inOut_board.board = board
                inOut_board.saveImage(f"visual\\{file_folder}\\{file_name}.{stoneCnt}_{posCnt}.png")

                print(board)
                for pp in board:
                    for qp in board[pp]:
                        print(board[pp][qp], end=" ")
                    print()
                print()
                for block in stone:
                    pB = p + block[0]
                    qB = q + block[1]
                    board[pB][qB] = 0