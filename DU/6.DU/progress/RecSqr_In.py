import time

class mat_data:
    def __init__(self, co0, co1, siz):
        self.co0 = co0
        self.co1 = co1
        self.siz = siz

Mat = [[0, 1, 1, 0, 1],
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]

def clear_mat(mat):

    mat_ret = [[0 for col in range(len(mat[0]))] for row in range(len(mat))]
    return mat_ret


def StrArr_IntArr(str):

    res = [int(element) for element in str.split()]

    return res

def IntArr_BinMat(mat_int):

    mat_bin = [[]]

    for a, arr in enumerate(mat_int):
        for num in arr:
            if num < 0:
                mat_bin[a].append(1)
            else:
                mat_bin[a].append(0)

        if a+1 == len(mat_int):
            break
        mat_bin.append([])

    return mat_bin


def BinMat_VizMat(mat_bit):

    mat_viz = [[]]

    for r, row in enumerate(mat_bit):
        for num in row:
            if num:
                mat_viz[r].append("⬜")
            else:
                mat_viz[r].append("⬛")

        if r + 1 == len(mat_bit):
            break
        mat_viz.append([])

    return mat_viz

    # for r, row in enumerate(mat):
    #     for c, num in enumerate(row):
    #         print(num, end=" ")
    #         mat_ret[r][c] = 0
    #     print()
    #
    # print()
    #
    # for row in mat:
    #     for num in row:
    #         print(num, end=" ")
    #     print()

    # return mat


def find_res_co(st_co, en_co):

    res_coor = []

    for r in range(st_co[0], en_co[0]+1):
        for c in range(st_co[1], en_co[1]+1):
            res_coor.append([r, c])

    return res_coor



# for r in range(rM-1):
#     for c in range(cM-1):
#         if Mat[r][c]:
#             print(f"{mCnt}: {r},{c} > ", end="")
#             # print("[ ]",end="")
#             if Mat[r][c+1] and Mat[r+1][c] and Mat[r+1][c+1]:
#                 size += 1
#             else:
#                 print(f"{r+size-1},{c+size-1} size: {size}")
#                 size = 1
#                 mCnt += 1

            #     continue
            # if not Mat[r+1][c]:
            #     continue
            # if not Mat[r+1][c+1]:

            # size += 1
            # for s in range(size):
            #     if not Mat[r][c+s]:
            #         break
            # for s in range(size):
            #     if not Mat[r+s][c]:
            #         break



# for r in range(5):
#     for c in range(5):


# for m in range(5):
#     print("[ ]", end="")
#     for r in range(m):
#         print("[ ]", end="")
#     print()
#     for c in range(m):
#         print("[ ]", end="")
#     for l in range(m):
#         print("[ ]\n")

    # print()

# mat_const = [[1, 2, 0, 0, 0],
#              [0, 0, 4, 0, 0],
#              [0, 6, 0, 7, 0],
#              [0, 0, 8, 9, 0],
#              [1, 0, 5, 0, 0]]

# mat = [[0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]]
#
# mat_tst = [[0, 1, 1, 0, 1],
#            [1, 1, 0, 1, 0],
#            [0, 1, 1, 1, 0],
#            [1, 1, 1, 1, 0],
#            [1, 1, 1, 1, 1]]

start_time = time.time()

source = "smat_1"
in_source = f"data/{source}.txt"
print(f"Source: {in_source}\n")

in_file = open(in_source, "r")

# mat_str = []
mat_int = []


print("\nmat_str print:")
# for line in in_file:
#     # print(line, end="")
#     mat_str.append(line)
#     # print(Str_IntArr(line))
#     # mat_int.append(Str_IntArr(line))

print("\n\nmat_int print:")
for line in in_file:
    # print(line, end="")
    # print(Str_Spl_IntArr(line))
    mat_int.append(StrArr_IntArr(line))


print("\n\nmat_bin print:")
mat_bin = IntArr_BinMat(mat_int)

# for r, row in enumerate(mat_bin):
#     R_len = len(row)
#     print(f"{r+1:4} {R_len:4}: ", end="")
#     for num in row:
#         print(num, end=" ")
#     print()


# print("\n\nmat_viz print:")


# mat_const = clear_mat(mat_const)
#
# print(mat_const)

# for m in range(5):
#     for r in range(m):
#         mat[r][m] = 1
#     for c in range(m):
#         mat[m][c] = 1
#
#     mat[m][m] = 1
#
#     print(f"\n{m+1}.Mat:")
#     for row in mat:
#         print(row)
#     mat = clear_mat(mat)

# for m in range(5):
#     for s in range(m):
#         mat[s][m] = 1
#         mat[m][s] = 1
#
#     mat[m][m] = 1
#
#     print(f"\n{m+1}.Mat:")
#     for row in mat:
#         print(row)
#     mat = clear_mat(mat)

# print("🔳🔲⬛⬜")


# print("\n\n")
# for row in mat_tst:
#     for num in row:
#         print(num, end=" ")
#     print()
#
# print()

# mat_viz = BinMat_VizMat(mat_bin)
# #
# for row in mat_viz:
#     for char in row:
#         print(char, end="")
#     print()

siz = maxSiz = 1
rcM = len(mat_bin[0])
# for i in range(1, rcM+1):
#     print(f" {i}", end="")
run = True
skip = False
# matCnt = 1

# cnt = len(mat_bin) * len(mat_bin[0])
# print(f"Cnt: {cnt}")

# size_list = []
# ban_coor = []
start_coor = [0, 0]
end_coor = [0, 0]

# for r, row in enumerate(mat_bin):
for r in range(len(mat_bin)):

    # if maxSiz > cnt + siz:
    #     break
        # print(f"{r:4}", end=" ")
    # for c, num in enumerate(row):
    for c in range(len(mat_bin[r])):
        # cnt -= 1
        # if maxSiz > (cnt + siz):
        #     break
        if skip:
            skip = False
            continue

        if mat_bin[r][c]:
            # print(f"\n\n{matCnt}.Mat.: [{r},{c}] => ", end="")
            # start_coor.append([r, c])
            # mat_viz[r][c] = "🟥"


            # if [r, c] in ban_coor:
            #     # ban_coor.remove([r, c])
            #     print(f"{matCnt}Cont")
            # else:
            #     run = True

            run = True



            while(run):
                if r+siz >= rcM or c+siz >= rcM:
                    run = False

                if run and (not mat_bin[r+siz][c+siz]):
                    # ban_coor.append([r + siz - 1, c + siz])
                    # ban_coor.append([r + siz, c + siz - 1])
                    skip = True
                    run = False

                    # if not mat_bin[r+siz][c+siz]:
                    #     ban_coor.append([r+siz-1, c+siz])
                    #     ban_coor.append([r+siz, c+siz-1])
                    #     run = False
                    # elif [r, c] in ban_coor:
                    #     ban_coor.remove([r, c])
                    #     run = False

                if run:
                    for i in range(siz+1):
                        if not (mat_bin[r+i][c+siz] and mat_bin[r+siz][c+i]):
                            run = False
                            break

                if not run:
                    # print(f"[{r+siz-1},{c+siz-1}]\n\t\t\tSize: {siz*siz}\n")

                    # for line in mat_viz:
                    #     for char in line:
                    #         print(char, end="")
                    #     print()
                    # mat_viz = BinMat_VizMat(mat_bin)

                    if siz > maxSiz:
                        maxSiz = siz
                        start_coor = [r, c]
                        end_coor = [r+siz-1, c+siz-1]


                    # size_list.append(siz*siz)
                    # start_coor.append([r, c])
                    # end_coor.append([r+siz-1, c+siz-1])
                    siz = 1
                    # matCnt += 1

                else:
                    # for i in range(1, siz+1):
                    #     for j in range(i):
                    #         mat_viz[r+i][c+j] = "🟥"
                    #         mat_viz[r+j][c+i] = "🟥"
                    # mat_viz[r+siz][c+siz] = "🟥"
                    siz += 1
        # else:
        #     continue
        # break


# print("\n\nBanned coordinates:")
# print(ban_coor)

print("\n\nResult:")
# res_pos = size_list.index(max(size_list))
print(f"\tSize:  {maxSiz*maxSiz}")
print(f"\tStart: {start_coor[0]} {start_coor[1]}")
print(f"\tEnd:   {end_coor[0]} {end_coor[1]}")

print(f"\n{time.time() - start_time}")

# print(f"\tSize:  {size_list[res_pos]}")
# print(f"\tStart: {start_coor[res_pos][0]} {start_coor[res_pos][1]}")
# print(f"\tEnd:   {end_coor[res_pos][0]} {start_coor[res_pos][1]}")

# print("\nViz:")

res_coor = find_res_co(start_coor, end_coor)
# print(res_coor)
print("\n\n")

for r in range(start_coor[0], end_coor[0]+1):
    for c in range(start_coor[1], end_coor[0]+1):
        print(mat_int[r][c], end=" ")
    print()


print("\n\n\n")

# # for r, row in enumerate(mat_viz):
# for r, row in enumerate(mat_bin):
#     for c, num in enumerate(row):
#
#         if [r, c] in res_coor:
#             print("🟥", end="")
#
#         # if [r, c] == start_coor[res_pos]:
#         #     print("🟨", end="")
#         #
#         # elif [r, c] == end_coor[res_pos]:
#         #     print("🟥", end="")
#
#         # elif [r, c] in res_coor:
#         #     # if [r, c] == start_coor[res_pos]:
#         #     #     print("🟨", end="")
#         #     #
#         #     # elif [r, c] == end_coor[res_pos]:
#         #     #     print("🟥", end="")
#         #
#         #     print("🟧", end="")
#         #     # else: print("🟧", end="")
#         # else:
#         #     print(mat_viz[r][c], end="")
#         elif num:
#             print("⬜", end="")
#         else:
#             print("⬛", end="")
#     print()

