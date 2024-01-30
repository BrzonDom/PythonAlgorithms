import copy

solBoard = []

def solve(board, piec_lst):

    if not piec_lst:
        if board not in solBoard:
            solBoard.append(copy.deepcopy(board))
            for row in board:
                for col in row:
                    print(col, end=" ")
                print()
            print()

    for row in range(len(board)):
        for col in range(len(board[0])):

            for piece in piec_lst:
                if canPlace(board, [row, col], piece):

                    for block in piece:
                        rB = row + block[0]
                        cB = col + block[1]
                        board[rB][cB] = pieces.index(piece) + 1

                    new_piec_list = copy.deepcopy(piec_lst)
                    new_piec_list.remove(piece)

                    solve(board, new_piec_list)

                    for block in piece:
                        rB = row + block[0]
                        cB = col + block[1]
                        board[rB][cB] = 0


    # for piece in piec_lst:

        # for r in board:
        #     for c in board:


def isIn(board, coord):

    rwCo = coord[0]
    clCo = coord[1]

    rows = len(board)
    cols = len(board[0])

    if rwCo in range(rows) and clCo in range(cols):
        return True
    else:
        return False


def canPlace(board, coord, piece):

    rwCo = coord[0]
    clCo = coord[1]

    for block in piece:
        rwBl = rwCo + block[0]
        clBl = clCo + block[1]

        if isIn(board, [rwBl, clBl]):
            if board[rwBl][clBl] != 0:
                return False
        else:
            return False

    return True


"""
⬜⬛
🔲🔳
🟩🟨🟧🟥🟪🟦🟫
"""

size = 3

board = [[0 for c in range(size)] for r in range(size)]

rowBor = len(board)
colBor = len(board[0])

for row in board:
    print(row)

pieces = [[[0, 0], [0, 1], [1, 1]], [[0, 0]], [[0, 0], [1, 0], [2, 0]], [[0, 0], [0, 1]]]
# pieces = [[[0, 0], [0, 1], [1, 1]], [[0, 0]]]

print()

# for piece in pieces:
#     for row in range(rowBor):
#         for col in range(colBor):
#             if [row, col] in piece:
#                 print("⬛", end="")
#         print()
#     print()

# for piece in pieces:
#
#
#
#     for block in piece:
#         print(block, end=" ")
#         # print(block[0], block[1], end=" ")
#     print()

# if canPlace(board, [0,1], pieces[0]):
#     print(True)
# else:
#     print(False)


# for piece in pieces:
#
#     caseBoard = [[0 for c in range(colBor)] for r in range(rowBor)]
#
#     for r in range(len(board)):
#         for c in range(len(board[0])):
#
#             for block in piece:
#                 rBl = r + block[0]
#                 cBl = c + block[1]
#
#                 blcFit = isIn(caseBoard, [rBl, cBl])
#
#                 if not blcFit:
#                     break
#
#             if blcFit:
#                 print()

solve(board, pieces)


"""     All positions for pieces     """

# for row in range(len(board)):
#     for col in range(len(board[0])):
#
#         for piece in pieces:
#
#             if canPlace(board,[row, col], piece):
#                 for block in piece:
#                     rowB = row + block[0]
#                     colB = col + block[1]
#                     board[rowB][colB] = 1
#
#                 for r in range(len(board)):
#                     for c in range(len(board[0])):
#                         if board[r][c]:
#                             print("🟥", end="")
#                             board[r][c] = 0
#                         else:
#                             print("⬜", end="")
#                     print()
#                 print()

print(solBoard)