

def infix(ex):

    res = ""
    # opStack = Stack()
    op_lst = []
    i = 0

    while i < len(ex):
        deb = ex[i]

        if ex[i] in "0123456789":
            while i < len(ex) and ex[i] in "0123456789":
                res += ex[i]
                i += 1
            res += " "
            continue

        if ex[i] == '(':
            # opStack.push(ex[i])
            op_lst.append(ex[i])

        elif ex[i] == ')':
            # op = opStack.pop()
            # op_lst.pop()
            op = op_lst.pop()

            while op != '(':
                res += op + " "
                # op = opStack.pop()
                # op_lst.pop()
                op = op_lst.pop()

        else:
            while len(op_lst) and not prec(ex[i], op_lst[-1]):
                # res += opStack.pop() + " "
                # op_lst.pop()
                res += op_lst.pop() + " "

            # opStack.push(ex[i])
            op_lst.append(ex[i])
        i += 1

    while len(op_lst):
        # res += opStack.pop() + " "
        # op_lst.pop()
        res += op_lst.pop() + " "

    return res


def prec(a, b):
    return ((a in "*/") and (b in "+-") or (b == "("))


exp_lst = [" 3 + 4 ",
           " 3 * 4 - 2 ",
           " 3 * (4 - 2) ",
           " (62 -32) *5/9 "]

for exp in exp_lst:
    print(exp, " = ", infix(exp))


# for i in range(len(exp_lst)):
#     print(f"{exp_lst[i]}")
