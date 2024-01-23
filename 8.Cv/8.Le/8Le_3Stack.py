
"""
Stack
"""

stack = []

stack.append("first")
stack.append("second")
stack.append("third")
stack.append(4)
stack.append(5)
stack.append(6)

while len(stack) > 0:
    print(stack.pop())
