
def postfix(ex):

    stack = []

    for arg in ex.split():
        if arg == '+':
            stack.append(stack.pop() + stack.pop())
        elif arg == '-':
            stack.append(-stack.pop() + stack.pop())
        elif arg == '*':
            stack.append(stack.pop() * stack.pop())
        elif arg == '/':
            sec = stack.pop()
            frs = stack.pop()

            stack.append(frs / sec)
        else:
            stack.append(float(arg))

    return stack.pop()

exp_lst = ["3 4 +",
           "3 4 -",
           "3 4 *",
           "3 4 /",
           "3 4 * 2 -",
           "3 4 2 - *"]

i = 0


print(f"{i+1}.Exp:\n\t\t3 + 4 = evalExp(3 4 +) = {postfix(exp_lst[i])}")
i += 1
print(f"{i+1}.Exp:\n\t\t3 - 4 = evalExp(3 4 -) = {postfix(exp_lst[i])}")
i += 1
print(f"{i+1}.Exp:\n\t\t3 * 4 = evalExp(3 4 *) = {postfix(exp_lst[i])}")
i += 1
print(f"{i+1}.Exp:\n\t\t3 / 4 = evalExp(3 4 /) = {postfix(exp_lst[i])}")
i += 1
print(f"{i+1}.Exp:\n\t\t3 * 4 - 2 = evalExp(3 4 * 2 -) = {postfix(exp_lst[i])}")
i += 1
print(f"{i+1}.Exp:\n\t\t3 * (4 - 2) = evalExp(3 4 2 - *) = {postfix(exp_lst[i])}")