
class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size()==0

    def push(self, item):
        self.items+=[item]

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

# stack = Stack()
# lstFun = []
# lstSum = []
#
# # print(f"a: {ord('a')}")
# # print(f"z: {ord('z')}")
# #
# # for indx in range(ord('a'), ord('g')):
# #     print(f"'{chr(indx)}', ", end="")
#
# in_itms = ['a', 'b', 'c', 'd', 'e', 'f']
#
# for itm in in_itms:
#     stack.push(itm)
#     lstFun.append(itm)
#     lstSum += itm
#     print("Stack:", stack.items)
#     print("lstFun:", lstFun)
#     print("lstSum:", lstSum)
#
# #
# # print()
# # print("stack peek ")
#
# for itm in range(len(in_itms)):
#     stack.pop()
#     lstFun.pop()
#     lstSum = lstSum[:-1]
#     print("Stack:", stack.items)
#     print("lstFun:", lstFun)
#     print("lstSum:", lstSum)