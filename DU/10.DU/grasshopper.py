import sys

file_path = sys.argv[1]

def isIn(row, col, size):
    return (col >= 0) and (col < size) and (row >= -(col // 2)) and (row < (size - col // 2))


# file_list = ["PrL_1", "PrL_2", "PrL_3"]
#
# file_name = "eboard-7296"
# file_path = "data\\" + file_name + ".txt"
#
# file = open(file_path, "r")
# print(f"File: {file_name}.txt\n")

file = open(file_path, "r")

data_list = []
value_dict = {}
# border = []

row_size = 0
col_size = 0

val_line = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for str_line in file:
    # print(str_line, end="")

    if str_line[0] in val_line:
        line = list(map(int, str_line.split()))
        # print(f"{line[0]}:{line[1]}")

        # border.append([line[0], line[1]])
        data_list.append(line)
        # print(line)

        row_size = max(row_size, line[0])
        col_size = max(col_size, line[1])

file.close()

size = row_size + 1

# print(f"Total Size: {size*size}")
# print(f"\tSize: {size}")
# print(f"\tRow:  {row_size}")
# print(f"\tCol:  {col_size}")
# print()


for row, col, val in data_list:

    if row not in value_dict:
        value_dict[row] = {}
    value_dict[row][col] = val

    # print(f"[{row:2} : {col:2} = {val}]")

# set_board = Board(0)
# set_pieces = set_board.loadBoard(file_path)
#
# set_board.saveImage(f"{file_name}_out.png")

pieces_cnt = 0

for line in data_list:
    if line[2] == 2:
        hooper_coord = [line[0], line[1]]
    elif line[2] == 1:
        pieces_cnt += 1

# print()
# print(f"Grasshoper coordinates: {hooper_coord[0]}:{hooper_coord[1]}")
# print(hooper_coord)
# print(value_dict[3][5])

move_list = [[1, -1], [1, 0],
             [0, 1], [-1, 1],
             [-1, 0], [0, -1]]

next_list = []

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
            # print(f"Jump in direction of [{row}, {col}] not possible")
            isOut = True

        if isIn(row, col, size):

            while value_dict[row][col] != 0:

                row += move[0]
                col += move[1]

                if not isIn(row, col, size):
                    # print(f"Jump in direction of [{row}, {col}] not possible due to lack of space")
                    isOut = True
                    break

            if not isOut:
                next_list.append([row, col])
                # print(f"Jump to {next_list[-1]} possible")



        # while value_dict[row][col] != 0 and isIn(row, col, size):
        #
        #     if [row-move[0], col-move[1]] != hooper_coord:
        #         next_list.append([row, col])
        #         print(f"{move} to [{row}, {col}] possible")
        #     else:
        #         print("No jump")

    # else:
    #     # print(f"{move} not possible because out of border")

# for i in range(len(move_list)-1):
#     print(f"{move_list[i]} -> {move_list[i+1]}")

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



if len(splitCheck) != pieces_cnt:
    print([])
else:
    next_list.sort()
    print(next_list)


