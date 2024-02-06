
def Str_IntArr(str):

    intArr = [0]

    numCnt = 0
    pol = 1

    for char in str:

        if char == ' ':

            numCnt += 1
            pol = 1

            intArr.append(0)

        elif char == '-':

            pol = -1

        elif ('0' <= char) & (char <= '9'):

            intArr[numCnt] = intArr[numCnt] * 10 + pol * int(char)

        else:
        # elif (char == '\n'):
            continue

    return intArr


def Str_MapIntArr(str):
    int_lst = list(map(int, str.split()))

    # int_lst = []
    # int_lst.append(list(map(int, str.split())))

    print(int_lst)
    return int_lst


str = "1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3"

str_mat = ["28 6 -12 -4 10 -44 -46 -38 -80 -28 18",
           "20 -18 24 30 -76 16 -78 -54 -12 -74 14",
           "38 36 36 26 -36 -20 -10 -8 -14 38 -50",
           "30 -80 2 12 38 -50 -20 -34 -30 -10 -66"]

intArr = [0]

num = numCnt = 0
pol = 1

# for char in str:
#     if (char == ' '):
#         numCnt += 1
#         pol = 1
#         IntArr.append(0)
#     elif (char == '-'):
#         pol = -1
#     elif ('0' <= char) & (char <= '9'):
#         IntArr[numCnt] = IntArr[numCnt] * 10 + pol * int(char)
#     else:
#         # elif (char == '\n'):
#         continue


# for i in range(9):
#     print(f"{numCnt}. ", end='')
#     IntArr[numCnt] = 1
#     numCnt += 1
#     IntArr.append(0)
#
# print(IntArr)


for char in str:
    if (char == ' ') | (char == '\n'):
        # print(f"{numCnt}. ", end='')
        # if (pol == -1):
        #     print("-", end='')
        # print(num)

        numCnt += 1
        num = 0
        pol = 1
        if char != '\n':
            intArr.append(0)
        # print()

    elif char == '-':
        pol = -1
        # print("-", end='')

    elif ('0' <= char) & (char <= '9'):
        intArr[numCnt] = 10 * intArr[numCnt] + pol * int(char)
        # num = num * 10 + pol * int(char)
        # print(char, end='')

    else:
        print("\n\nEnd")

print("Basic function written in operator code\n")

print("Str:")
print("\t", intArr)
print("\t", Str_IntArr(str))
print()

res = Str_IntArr(str)
for i in res:
    print(f"{i}", end=' ')


print("\n\nStr_mat:")

print("\t", str_mat)
print()

for s in str_mat:
    print(Str_IntArr(s))
print()

for s in str_mat:
    res = Str_IntArr(s)
    for i in res:
        print(f"{i}", end=' ')
    print()

print()