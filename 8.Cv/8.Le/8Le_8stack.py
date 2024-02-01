
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

print("From last to first")
while len(stack) > 0:
    print("\t" + str(stack.pop()))
print()


stack.append("first")
stack.append("second")
stack.append("third")
stack.append(4)
stack.append(5)
stack.append(6)

print("From first to last")
while len(stack) > 0:
    print("\t" + str(stack.pop(0)))
print()