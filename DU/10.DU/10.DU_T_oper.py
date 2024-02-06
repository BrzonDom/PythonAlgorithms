from board import *

import copy

def isIn(row, col, size):
    return (col >= 0) and (col < size) and (row >= -(col // 2)) and (row < (size - col // 2))


file_list = ["PrT_1", "PrT_2", "PrT_3", "PrL_1", "PrL_2", "PrL_3", "eboard-5002.txt", "eboard-5412", "eboard-6759", "eboard-7089", "eboard-7141", "eboard-7639", "eboard-8904"]

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

inOut_board = Board(size)
inOut_board.board = value_dict

inOut_board.saveImage(f"{file_name}_in.png")

# set_board = Board(0)
# set_pieces = set_board.loadBoard(file_path)
#
# set_board.saveImage(f"{file_name}_out.png")
pieces_cnt = 0

for line in data_list:
    if line[2] == 2:
        ant_coord = [line[0], line[1]]
    elif line[2] == 1:
        pieces_cnt += 1


print(f"Ant coordinates: {ant_coord[0]}:{ant_coord[1]}")
# print(ant_coord)
print()
# print(value_dict[3][5])

moves = [[0,-1], [1, -1], [1, 0],
         [0, 1], [-1, 1],
         [-1, 0], [0, -1], [1, -1]]


# for m in range(1, len(moves)-1):
#     print(f"{m}. {moves[m]}")
# print()

next_list = []
stackNext = [ant_coord]
neighb_list = []

while len(stackNext) > 0:

    curRow = stackNext[-1][0]
    curCol = stackNext[-1][1]

    stackNext.pop()

    for m in range(1, len(moves)-1):
        row = curRow + moves[m][0]
        col = curCol + moves[m][1]

        if isIn(row, col, size):
            if value_dict[row][col] == 0:

                tstRow = [curRow + moves[m+1][0], curRow + moves[m-1][0]]
                tstCol = [curCol + moves[m+1][1], curCol + moves[m-1][1]]

                if isIn(tstRow[0], tstCol[0], size) and isIn(tstRow[1], tstCol[1], size):
                    hasSpc = hasNei = False

                    if value_dict[tstRow[0]][tstCol[0]] == 0 or value_dict[tstRow[1]][tstCol[1]] == 0:
                        hasSpc = True

                    if value_dict[tstRow[0]][tstCol[0]] == 1 or value_dict[tstRow[1]][tstCol[1]] == 1:
                        hasNei = True

                    if hasSpc and hasNei:
                        if not [row, col] in next_list:
                            stackNext.append([row, col])
                            next_list.append([row, col])

print(next_list)

        # for i in range(2):
        #     if isIn(tstRow[i], tstCol[i], size):
        #         if value_dict[tstRow[i]]

        # if isIn(row, col, size):
        #     if value_dict[row][col] == 0:


# for m in range(1, len(moves)-1):
#     row = ant_coord[0] + moves[m][0]
#     col = ant_coord[1] + moves[m][1]
#
#     if isIn(row, col, size):
#
#         if value_dict[row][col] == 0:
#             neiRow = [ant_coord[0] + moves[m-1][0], ant_coord[0] + moves[m+1][0]]
#             neiCol = [ant_coord[1] + moves[m-1][1], ant_coord[1] + moves[m+1][1]]
#
#             if value_dict[neiRow[0]][neiCol[0]] == 1 or value_dict[neiRow[1]][neiCol[1]]:
#                 stackNext.append([row, col])
#
#         elif value_dict[row][col] == 1:
#             neighb_list.append([row, col])


# fin_dict = copy.deepcopy(value_dict)
#
# for next in stackNext:
#     fin_dict[next[0]][next[1]] = 3
#
# inOut_board.expBoard = fin_dict
# inOut_board.saveImage(f"{file_name}_out.png")
#
# print(neighb_list)
# print(stackNext)

# for m in range(1, len(moves)-1):



# neighbour_list = []
#
#
# for move in moves:
#     # if [hopper_coord[0]+move[0], hopper_coord[1]+move[1]] in border:
#     row = ant_coord[0] + move[0]
#     col = ant_coord[1] + move[1]
#     isOut = False
#     # print(f"Direction: {move}")
#
#     if isIn(row, col, size):
#
#         # row = hopper_coord[0]+move[0]
#         # col = hopper_coord[1]+move[1]
#
#         if value_dict[row][col] == 1:
#             neighbour_list.append([row, col])
#         else:
#
#
#         if isIn(row, col, size):
#             print(f"Jump in direction of [{row}, {col}] not possible due to lack of space")
#
#         # else:
#             while value_dict[row][col] != 0 and not isOut:
#
#                 row += move[0]
#                 col += move[1]
#
#                 if not isIn(row, col, size):
#                     print(f"Jump in direction of [{row}, {col}] not possible due to lack of space")
#                     isOut = True
#                     break
#
#             if not isOut:
#                 next_list.append([row, col])
#                 print(f"Jump to {next_list[-1]} possible")
#
#
#
#             # while value_dict[row][col] != 0 and isIn(row, col, size):
#             #
#             #     if [row-move[0], col-move[1]] != hopper_coord:
#             #         next_list.append([row, col])
#             #         print(f"{move} to [{row}, {col}] possible")
#             #     else:
#             #         print("No jump")
#
#     else:
#         print(f"{move} not possible because out of border")
#
# print()
#
# # for i in range(len(move_list)-1):
# #     print(f"{move_list[i]} -> {move_list[i+1]}")
#
# # if len(neighbour_list) >= 2:
# # #     print(next_list)
# # #
# # # elif len(neighbour_list) == 2:
# # #     split = True
# #
# #     for i in range(len(neighbour_list)-1):
# #         # if (-1 <= (neighbour_list[i][0] - neighbour_list[i+1][0]) <= 1) and (-1 <= (neighbour_list[i][1] - neighbour_list[i+1][1]) <= 1):
# #         if [neighbour_list[i][0]-neighbour_list[i+1][0], neighbour_list[i][1]-neighbour_list[i+1][1]] in move_list:
# #             print(next_list)
# #             # split = False
# #         else:
# #             print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")
# #
# #     # if split:
# #     #     print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")
# #
# # else:
# #     print(f"Moves not possible since it would split the hive")
#
# split = False
#
# # if len(neighbour_list) != 1 and len(neighbour_list) != 6:
# #
# #     for i in range(len(neighbour_list)):
# #         split = True
# #         for j in range(len(neighbour_list)):
# #             if split:
# #                 if i == j:
# #                     continue
# #                 elif [neighbour_list[i][0] - neighbour_list[j][0], neighbour_list[i][1]-neighbour_list[j][1]] in move_list:
# #                     split = False
#
# # split = False
# # print("Check split")
# #
# # for check in neighbour_list:
# #     if split:
# #         break
# #
# #     for comp in neighbour_list:
# #         split = True
# #         print(comp)
# #         if comp == check:
# #             continue
# #         elif [check[0]-comp[0], check[1]-comp[1]] in move_list:
# #             split = False
# #             break
# #             # print("NOT")
# #             # split = True
# #
# # print(f"Split: {split}")
#
#
# # for i in range(len(neighbour_list)-1):
# #     # if (-1 <= (neighbour_list[i][0] - neighbour_list[i+1][0]) <= 1) and (-1 <= (neighbour_list[i][1] - neighbour_list[i+1][1]) <= 1):
# #     if not [neighbour_list[i][0]-neighbour_list[i+1][0], neighbour_list[i][1]-neighbour_list[i+1][1]] in move_list:
# #         split = True
# #
# #         if split:
# #             if [neighbour_list[i-1][0]-neighbour_list[i][0], neighbour_list[i-1][1]-neighbour_list[i][1]] in move_list:
# #                 split = False
#
#         # print(next_list)
#         # split = False
#     # else:
#     #     print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")
#
# splitStack = [neighbour_list[0]]
# splitCheck = []
#
# while len(splitStack) > 0:
#
#     curRow = splitStack[-1][0]
#     curCol = splitStack[-1][1]
#
#     splitStack.pop()
#
#     # if [curRow, curCol] not in splitCheck:
#     #     splitCheck.append([curRow, curCol])
#     # splitStack.pop()
#
#     for move in moves:
#         row = curRow + move[0]
#         col = curCol + move[1]
#
#         if isIn(row, col, size):
#             if value_dict[row][col] == 1 and [row, col] not in splitCheck:
#                 splitCheck.append([row, col])
#                 splitStack.append([row, col])
#
#
# print(f"Split Check {len(splitCheck)}/{pieces_cnt}:")
# print(splitCheck)
#
#
#
# if split:
#     print(f"Moves not possible since it would split the hive, neighbours aren't next to each other")
# else:
#     print(next_list)