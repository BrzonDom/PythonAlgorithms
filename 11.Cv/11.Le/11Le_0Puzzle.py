import copy
from queue import Queue

"""
Symbols:
    ⏪⏫⏩⏬
    ◀ ▶ ▲ ▼
"""

neighb_dict = {}

class State:
    def __init__(self, state, action = None, parent = None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.action = action

    def nextState(self):
        nextBoards = []

        valid, next = right(self.state)
        if valid:
            nextBoards.append(State(next, "▶", self))

        valid, next = left(self.state)
        if valid:
            nextBoards.append(State(next, "◀", self))

        valid, next = up(self.state)
        if valid:
            nextBoards.append(State(next, "▲", self))

        valid, next = down(self.state)
        if valid:
            nextBoards.append(State(next, "▼", self))

        return nextBoards

    # def goodMove(self):
    #
    #     for r in range(len(self.state)):
    #         for c in range(len(self.state[0])):
    #             if self.state[r][c] == 0:


def BFS(orgSta, slvSta):

    queue = Queue()
    queue.put(orgSta)

    visited = {}
    visited[str(orgSta.state)] = True

    while not queue.empty():

        curSta = queue.get()

        if curSta.state == slvSta.state:
            path_moves = [curSta.action]
            path_boards = [curSta.state]
            #
            # # curSta = curSta.parent
            # # path_moves.append(curSta.action)
            # # path_boards.append(curSta.state)
            #
            while curSta.action != None:
                path_moves.append(curSta.parent.action)
                path_boards.append(curSta.parent.state)
                curSta = curSta.parent

            print("SOLVED")
            return path_boards[::-1], path_moves[::-1]

        for next in State.nextState(curSta):
            if not str(next.state) in visited:
                visited[str(next.state)] = True
                queue.put(next)

    print("NOT SOLVED")
    return


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
                return True, board

    return False, board

def left(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(len(board)):
        for c in range(1, len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r][c-1] = board[r][c-1], board[r][c]
                return True, board

    return False, board

def up(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(1, len(board)):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r-1][c] = board[r-1][c], board[r][c]
                return True, board

    return False, board

def down(orgBoard):
    board = copy.deepcopy(orgBoard)

    for r in range(len(board)-1):
        for c in range(len(board[r])):
            if board[r][c] == 0:
                board[r][c], board[r+1][c] = board[r+1][c], board[r][c]
                return True, board

    return False, board

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

# print("\tMoves\n")
# print("Right:", end="\n\t")
# board = right(board)[1]
#
# for row in board:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()
#
# board = copy.deepcopy(org_board)
#
# print("Left:", end="\n\t")
# board = left(board)[1]
#
# for row in board:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()
#
# board = copy.deepcopy(org_board)
#
# print("Up:", end="\n\t")
# board = up(board)[1]
#
# for row in board:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()
#
# board = copy.deepcopy(org_board)
#
# print("Down:", end="\n\t")
# board = down(board)[1]
#
# for row in board:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()

board = copy.deepcopy(org_board)

print()

# other_board = left(board)
# print(board)
# print(other_board)

# print(orgState.state)
#
# for next in State.nextState(orgState):
#     print("\t", next.action, next.state)
# print()

# finState = BFS(orgState, slvtState)

# for _ in range(3):
#     print(finState.action, end="\n\t")
#     for row in finState.state:
#         for col in row:
#             print(col, end=" ")
#         print("\n", end="\t")
#     print()
#     finState = finState.parent

orgState = State(org_board)
slvState = State(slv_board)

path_board, path_move = BFS(orgState, slvState)
print()
#
for p, path in enumerate(path_board):
    print(path_move[p], end="\n\t")
    for row in path:
        for col in row:
            print(col, end=" ")
        print("\n", end="\t")
    print()
