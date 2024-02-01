import copy

def right(board):
    for r in range(len(board)):
        for c in range(len(board[r])-1):
            if board[r][c] == 0:
                board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
                return board

    return board

def left(board):
    for r in range(len(board)):
        for c in range(1, len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r][c-1] = board[r][c-1], board[r][c]
                return board

    return board

def up(board):
    for r in range(1, len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r-1][c] = board[r-1][c], board[r][c]
                return board

    return board

def down(board):
    for r in range(len(board)-1):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
                return board

    return board

org_board = [[8, 5, 6], [4, 0, 3], [1, 2, 7]]
board = copy.deepcopy(org_board)

print("Original board:")
print()

for row in board:
    for col in row:
        print(col, end=" ")
    print()
print()

print("Right:", end="\n\t")
board = right(board)

for row in board:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

board = copy.deepcopy(org_board)

print("Left:", end="\n\t")
board = left(board)

for row in board:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

board = copy.deepcopy(org_board)

print("Up:", end="\n\t")
board = up(board)

for row in board:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

board = copy.deepcopy(org_board)

print("Down:", end="\n\t")
board = down(board)

for row in board:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()