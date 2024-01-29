
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

def BimMat_VizMat(mat_bit):

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


size = 1
mCnt = 1

rM = len(Mat)
cM = len(Mat[0])

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
mat_const = [[1, 2, 0, 0, 0],
             [0, 0, 4, 0, 0],
             [0, 6, 0, 7, 0],
             [0, 0, 8, 9, 0],
             [1, 0, 5, 0, 0]]

mat = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]]

mat_tst = [[0, 1, 1, 0, 1],
           [1, 1, 0, 1, 0],
           [0, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1]]

mat_viz = BimMat_VizMat(mat_tst)


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

for m in range(5):
    for s in range(m):
        mat[s][m] = 1
        mat[m][s] = 1

    mat[m][m] = 1

    print(f"\n{m+1}.Mat:")
    for row in mat:
        print(row)
    mat = clear_mat(mat)

# print("🔳🔲⬛⬜")



print("\n\n")
for row in mat_tst:
    for num in row:
        print(num, end=" ")
    print()

print()

for row in mat_viz:
    for char in row:
        print(char, end="")
    print()

siz = 1
rcM = len(mat_tst[0])
for i in range(1, rcM+1):
    print(f" {i}", end="")
run = True
matCnt = 1

size_list = []
ban_coor = []
start_coor = []
end_coor = []

for r, row in enumerate(mat_tst):
    rcM = len(mat_tst[r])
    for c, num in enumerate(row):
        if mat_tst[r][c]:
            print(f"\n\n{matCnt}.Mat.: [{r},{c}] => ", end="")
            # start_coor.append([r, c])
            mat_viz[r][c] = "🟥"

            run = True

            while(run):
                if r+siz >= rcM or c+siz >= rcM:
                    run = False

                if run:
                    if not mat_tst[r+siz][c+siz]:
                        ban_coor.append([r+siz-1, c+siz])
                        ban_coor.append([r+siz, c+siz-1])
                        run = False
                    elif [r, c] in ban_coor:
                        run = False

                if run:
                    for i in range(siz+1):
                        if not (mat_tst[r+i][c+siz] and mat_tst[r+siz][c+i]):
                            run = False

                if not run:
                    print(f"[{r+siz-1},{c+siz-1}]\n\t\t\tSize: {siz*siz}\n")
                    # mat_viz[r+siz-1][c+siz-1] = "🟥"
                    for line in mat_viz:
                        for char in line:
                            print(char, end="")
                        print()
                    mat_viz = BimMat_VizMat(mat_tst)

                    size_list.append(siz*siz)
                    start_coor.append([r, c])
                    end_coor.append([r+siz-1, c+siz-1])

                    siz = 1
                    matCnt += 1

                else:
                    for i in range(1, siz+1):
                        for j in range(i):
                            mat_viz[r+i][c+j] = "🟥"
                            mat_viz[r+j][c+i] = "🟥"
                    mat_viz[r+siz][c+siz] = "🟥"
                    siz += 1


print("\n\nBanned coordinates:")
print(ban_coor)

print("\n\nResult:")
res_pos = size_list.index(max(size_list))

print(f"\tSize:  {size_list[res_pos]}")
print(f"\tStart: {start_coor[res_pos][0]} {start_coor[res_pos][1]}")
print(f"\tEnd:   {end_coor[res_pos][0]} {start_coor[res_pos][1]}")

print("\nViz:")

res_coor = find_res_co(start_coor[res_pos], end_coor[res_pos])
print(res_coor)
print()

for r, row in enumerate(mat_viz):
    for c, num in enumerate(row):

        if [r, c] in res_coor:
            print("🟥", end="")

        # if [r, c] == start_coor[res_pos]:
        #     print("🟨", end="")
        #
        # elif [r, c] == end_coor[res_pos]:
        #     print("🟥", end="")

        # elif [r, c] in res_coor:
        #     # if [r, c] == start_coor[res_pos]:
        #     #     print("🟨", end="")
        #     #
        #     # elif [r, c] == end_coor[res_pos]:
        #     #     print("🟥", end="")
        #
        #     print("🟧", end="")
        #     # else: print("🟧", end="")
        else:
            print(mat_viz[r][c], end="")
    print()






