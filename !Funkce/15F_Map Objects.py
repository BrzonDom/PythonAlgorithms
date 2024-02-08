import copy

class State:
    def __init__(self, state, action = None, parent = None):
        self.state = copy.deepcopy(state)
        self.parent = parent
        self.action = action


# def func(start, end):
#
#     cur = start
#     i = 0
#     while cur.state <= end.state:
#         cur.state += i
#         cur.action = i
#
#         if cur.state == end.state:
#             path_action = []
#
#             return

def printState(start):
    print("\tState:", start.state)
    print("\tParent:", start.parent.state)
    print("\tAction:", start.action)

num = 0
for i in range(10):
    num += i
    print(i, ":", num)
print()

start = State(0)
end = State(45)
#
# # tstFun(end)
# # print(end.state)
#
# cur = State(start.state, 2, start)
# print(cur.state)
# cur.state += 2
# print(cur.state)
# print(start.state)
# print(cur.parent.action)

next = State(start.state, 0, start)
i = 1
while next.state <= end.state:
    cur = State(next.state+i, i, next)
    print(f"{i}.")
    printState(cur)

    if cur.state == end.state:
        print("\nDONE")
        break
    i += 1
    next = copy.deepcopy(cur)

trans = cur
path = [trans.action]

while trans.action != None:
    path.append(trans.parent.action)
    trans = trans.parent

print()
print(path)