def checkPars(x):
    left = "({["
    right = ")}]"
    stack = []
    for c in x:
        if c in left:
            stack.append(c)
        else:
            for i in range(len(right)):
                if c == right[i]:
                    #we expect left[i] in stack
                    if len(stack)==0:
                        return False
                    lastLeft = stack.pop()
                    if lastLeft != left[i]:
                        return False
    return len(stack) == 0

chck_lst = [" a*(a+b) ",
            " (1+(a+b))+(2-3) ",
            " 1*(a+b ",
            " )a+b( "]


for i in range(len(chck_lst)):
    print(chck_lst[i], " : ", checkPars(chck_lst[i]))