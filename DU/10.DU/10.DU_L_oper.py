
from board import *

def isIn(row, col, size):
    return (col >= 0) and (col < size) and (row >= -(col // 2)) and (row < (size - col // 2))


file_list = ["PrL_1", "PrL_2", "PrL_3", "eboard-5002.txt", "eboard-5412", "eboard-6759", "eboard-7089", "eboard-7141", "eboard-7639", "eboard-8904"]

file_name = file_list[0]
# file_name = "eboard-7296"
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt\n")



graph = []


"""     Read file input     """
# line = file.readline()
# print(line)
#
# res = list(map(int, line.split()))
# print(res)

data_list = []
value_dict = {}
border = []

row_size = 0
col_size = 0
line_cnt = 1
val_line = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for str_line in file:
    # print(str_line, end="")
    """     Check if input is valid     """
    if str_line[0] in val_line:
    #     line_cnt += 1
    # else:
        line = list(map(int, str_line.split()))
        # print(f"{line[0]}:{line[1]}")

        """     Store input board of coords     """
        border.append([line[0], line[1]])
        """     Store input board with values   """
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

    """     Make graph(dictionary) out of data  """
    if row not in value_dict:
        value_dict[row] = {}
    value_dict[row][col] = val

    # print(f"[{row:2} : {col:2} = {val}]")

"""     For visual board print  """
# set_board = Board(0)
# set_pieces = set_board.loadBoard(file_path)
# set_board.saveImage(f"{file_name}_out.png")

pieces_cnt = 0

for line in data_list:

    if line[2] == 2:
        """     Find the coordinates of grasshopper    """
        hopper_coord = [line[0], line[1]]
    elif line[2] == 1:
        """     Count the number of other pieces    """
        pieces_cnt += 1

print()
print(f"Grasshopper coordinates: {hopper_coord[0]}:{hopper_coord[1]}")
print(hopper_coord)
# print(value_dict[3][5])

"""     List of possible moves on hex-grid  """
move_list = [[1, -1], [1, 0],
             [0, 1], [-1, 1],
             [-1, 0], [0, -1]]
next_list = []

for move in move_list:
    print(move)
print()

neighbour_list = []

for move in move_list:
    # if [hopper_coord[0]+move[0], hopper_coord[1]+move[1]] in border:
    row = hopper_coord[0] + move[0]
    col = hopper_coord[1] + move[1]

    """     Bool-val to check if the jump is possible   """
    isOut = False
    # print(f"Direction: {move}")

    if isIn(row, col, size):

        # row = hopper_coord[0]+move[0]
        # col = hopper_coord[1]+move[1]

        if value_dict[row][col] == 1:
            neighbour_list.append([row, col])
            row += move[0]
            col += move[1]

        else:
            print(f"Jump in direction of [{row}, {col}] not possible")
            isOut = True

        if isIn(row, col, size):
            # print(f"Jump in direction of [{row}, {col}] is possible")

        # else:
            while value_dict[row][col] != 0 and not isOut:
                """     While loop to travel to the end of pieces   
                            Breaks either when out of board or lands on empty tile  """

                row += move[0]
                col += move[1]

                if not isIn(row, col, size):
                    print(f"Jump in direction of [{row}, {col}] not possible due to lack of space")
                    isOut = True
                    break

            if not isOut:
                """     If hopper got to an empty tile  """
                next_list.append([row, col])
                print(f"Jump to {next_list[-1]} possible")

    else:
        print(f"{move} not possible because out of border")
print()


split = False

# if len(neighbour_list) != 1 and len(neighbour_list) != 6:
#
#     for i in range(len(neighbour_list)):
#         split = True
#         for j in range(len(neighbour_list)):
#             if split:
#                 if i == j:
#                     continue
#                 elif [neighbour_list[i][0] - neighbour_list[j][0], neighbour_list[i][1]-neighbour_list[j][1]] in move_list:
#                     split = False

# split = False
# print("Check split")
#
# for check in neighbour_list:
#     if split:
#         break
#
#     for comp in neighbour_list:
#         split = True
#         print(comp)
#         if comp == check:
#             continue
#         elif [check[0]-comp[0], check[1]-comp[1]] in move_list:
#             split = False
#             break
#             # print("NOT")
#             # split = True
#
# print(f"Split: {split}")


# for i in range(len(neighbour_list)-1):
#     # if (-1 <= (neighbour_list[i][0] - neighbour_list[i+1][0]) <= 1) and (-1 <= (neighbour_list[i][1] - neighbour_list[i+1][1]) <= 1):
#     if not [neighbour_list[i][0]-neighbour_list[i+1][0], neighbour_list[i][1]-neighbour_list[i+1][1]] in move_list:
#         split = True
#
#         if split:
#             if [neighbour_list[i-1][0]-neighbour_list[i][0], neighbour_list[i-1][1]-neighbour_list[i][1]] in move_list:
#                 split = False

        # print(next_list)
        # split = False
    # else:
    #     print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")

splitStack = [neighbour_list[0]]
splitCheck = []

while len(splitStack) > 0:
    """     While-loop of flood fill
                to check if jump split the hive     """

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

split = bool(len(splitCheck) == pieces_cnt)
print(split)


if not split:
    print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")
else:
    print(next_list)