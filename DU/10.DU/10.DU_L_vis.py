
# from expBoard import *
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


file_list = ["PrL_1", "PrL_2", "PrL_3", "eboard-5002", "eboard-5412", "eboard-6759", "eboard-7089", "eboard-7141", "eboard-7639", "eboard-8904"]

file_name = file_list[2]
# file_name = "eboard-7296"
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt\n")


data_list = []
value_dict = {}
border = []

row_size = 0
col_size = 0
line_cnt = 1
val_line = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for str_line in file:
    # print(str_line, end="")
    if str_line[0] in val_line:
    #     line_cnt += 1
    # else:
        line = list(map(int, str_line.split()))
        # print(f"{line[0]}:{line[1]}")

        border.append([line[0], line[1]])
        data_list.append(line)
        # print(line)
        # graph[[line[0], line[1]]] = line[2]

        row_size = max(row_size, line[0])
        col_size = max(col_size, line[1])

file.close()

size = row_size + 1

print(f"Total Size: {size*size}")
print(f"\tSize: {size}")
print(f"\tRow:  {row_size}")
print(f"\tCol:  {col_size}")
print()


for row, col, val in data_list:

    if row not in value_dict:
        value_dict[row] = {}
    value_dict[row][col] = val

    # print(f"[{row:2} : {col:2} = {val}]")

# in_board = myBoard(size)
# in_board.expBoard = value_dict
# in_board.saveImage(f"{file_name}_in.png")

pieces_cnt = 0

for line in data_list:
    if line[2] == 2:
        hooper_coord = [line[0], line[1]]
    elif line[2] == 1:
        pieces_cnt += 1

print()
print(f"Grasshoper coordinates: {hooper_coord[0]}:{hooper_coord[1]}")
print(hooper_coord)
# print(value_dict[3][5])

move_list = [[1, -1], [1, 0],
             [0, 1], [-1, 1],
             [-1, 0], [0, -1]]
next_list = []

for move in move_list:
    print(move)

print()

neighbour_list = []


for move in move_list:
    # if [hooper_coord[0]+move[0], hooper_coord[1]+move[1]] in border:
    row = hooper_coord[0] + move[0]
    col = hooper_coord[1] + move[1]
    isOut = False
    # print(f"Direction: {move}")

    if isIn(row, col, size):

        # row = hooper_coord[0]+move[0]
        # col = hooper_coord[1]+move[1]

        if value_dict[row][col] == 1:
            neighbour_list.append([row, col])
            row += move[0]
            col += move[1]

        else:
            print(f"Jump in direction of [{row}, {col}] not possible")
            isOut = True

        if isIn(row, col, size):
            print(f"Jump in direction of [{row}, {col}] not possible due to lack of space")

        # else:
            while value_dict[row][col] != 0 and not isOut:

                row += move[0]
                col += move[1]

                if not isIn(row, col, size):
                    print(f"Jump in direction of [{row}, {col}] not possible due to lack of space")
                    isOut = True
                    break

            if not isOut:
                next_list.append([row, col])
                print(f"Jump to {next_list[-1]} possible")



            # while value_dict[row][col] != 0 and isIn(row, col, size):
            #
            #     if [row-move[0], col-move[1]] != hooper_coord:
            #         next_list.append([row, col])
            #         print(f"{move} to [{row}, {col}] possible")
            #     else:
            #         print("No jump")

    else:
        print(f"{move} not possible because out of border")

print()

split = False

splitStack = [neighbour_list[0]]
splitCheck = []

while len(splitStack) > 0:

    curRow = splitStack[-1][0]
    curCol = splitStack[-1][1]

    splitStack.pop()

    # if [curRow, curCol] not in splitCheck:
    #     splitCheck.append([curRow, curCol])
    # splitStack.pop()

    for move in move_list:
        row = curRow + move[0]
        col = curCol + move[1]

        if isIn(row, col, size):
            if value_dict[row][col] == 1 and [row, col] not in splitCheck:
                splitCheck.append([row, col])
                splitStack.append([row, col])


print(f"Split Check {len(splitCheck)}/{pieces_cnt}:")
print(splitCheck)



if split:
    print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")
else:
    print(next_list)


    fin_dict = copy.deepcopy(value_dict)
    # print(fin_dict)

    for next in next_list:
        fin_dict[next[0]][next[1]] = 3

    # print(fin_dict)

    # fin_board = Board(0)
    # fin_board.loadBoard(file_path)


    inOut_board = myBoard(size)
    inOut_board.board = value_dict
    inOut_board.saveImage(f"visual\\{file_name}_in.png")

    inOut_board.board = fin_dict

    inOut_board.saveImage(f"visual\\{file_name}_out.png")