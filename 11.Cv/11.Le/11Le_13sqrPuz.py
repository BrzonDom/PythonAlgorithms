import copy
from queue import Queue

"""
    !!   PseudoCode   !!
"""

class State:
    def __init__(self, state, action = None, parent = None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.action = action

    def expand(self):
        result = []
        return result

    def isGoal(self):
        return False

    def __repr__(self):
        return str(self.state)


def BFS(start, goal):
    q = Queue()
    q.put(start)

    known = {}
    known[str(start)] = True

    while not q.empty():

        actual = q.get()
        if actual == goal:
            path = traverse(actual)
            return path[::-1]

        for child in actual.expand():
            if not str(child) in known:
                known[str(child)] = True
                q.put(child)
    return []

Start = [[8, 5, 6], [4, 0, 3], [1, 2, 7]]
Goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]



