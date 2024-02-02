import copy
from queue import Queue

"""⏪⏫⏩⏬"""

neighb_dict = {}

class State:
    def __init__(self, state, action = None, parent = None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.action = action

    def nextState(self):
        nextBoards = []

        next = right(self.state)
        if self.state != next:
            nextBoards.append(State(next, "⏩", self.state))

        next = left(self.state)
        if self.state != next:
            nextBoards.append(State(next, "⏪", self.state))

        next = up(self.state)
        if self.state != next:
            nextBoards.append(State(next, "⏫", self.state))

        next = down(self.state)
        if self.state != next:
            nextBoards.append(State(next, "⏬", self.state))

        return nextBoards

    # def goodMove(self):
    #
    #     for r in range(len(self.state)):
    #         for c in range(len(self.state[0])):
    #             if self.state[r][c] == 0:


# def moves(orgBoard):
#
#     neghbBoard = []
#
#     if orgBoard != right(orgBoard):
#         neghbBoard.append(right(orgBoard))
#
#     if orgBoard != left(orgBoard):
#         neghbBoard.append(left(orgBoard))
#
#     if orgBoard != up(orgBoard):
#         neghbBoard.append(up(orgBoard))
#
#     if orgBoard != down(orgBoard):
#         neghbBoard.append(down(orgBoard))
#
#     return neghbBoard


def right(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(len(board)):
        for c in range(len(board[r])-1):
            if board[r][c] == 0:
                board[r][c], board[r][c+1] = board[r][c+1], board[r][c]
                return board

    return board

def left(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(len(board)):
        for c in range(1, len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r][c-1] = board[r][c-1], board[r][c]
                return board

    return board

def up(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(1, len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r-1][c] = board[r-1][c], board[r][c]
                return board

    return board

def down(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(len(board)-1):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
                return board

    return board

org_board = [[8, 5, 6], [4, 0, 3], [1, 2, 7]]
board = copy.deepcopy(org_board)

print("Original board:", end="\n\t")

for row in org_board:
    for col in row:
        print(col, end=" ")
    print("", end="\n\t")
print()

print("Solved board:", end="\n\t")
slv_board = copy.deepcopy(org_board)

iOrd = 0
row = len(slv_board)
col = len(slv_board[0])

for r in range(row):
    for c in range(col):
        iOrd += 1

        if iOrd == (row * col):
            slv_board[r][c] = 0
        else:
            slv_board[r][c] = iOrd

        print(slv_board[r][c], end=" ")
    print("", end="\n\t")
print()

print("\tMoves\n")
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

board = copy.deepcopy(org_board)

print()

# other_board = left(board)
# print(board)
# print(other_board)

orgState = State(org_board)
print(orgState.state)

for next in State.nextState(orgState):
    print("\t", next.action, next.state)