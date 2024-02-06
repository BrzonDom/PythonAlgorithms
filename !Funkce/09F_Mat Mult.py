
def matMult(matA, matB):

    rowA = len(matA)
    colA = len(matA[0])

    rowB = len(matB)
    colB = len(matB[0])

    """     Control of matrix dimensions    """
    if colA != rowB:
        return 0
    else:
        row = rowA
        col = colB

        mat = [[0 for c in range(col)] for r in range(row)]

        for r in range(row):
            for c in range(col):

                """     Dot product calculation     """
                add = 0
                for d in range(colA):
                    add += matA[r][d] * matB[d][c]

                mat[r][c] = add

                """     Final matrix print      """
            #     print(f"{mat[r][c]:2}", end=" ")
            # print()

        return mat


"""     List matrix     """
mat_list = [[[-1, -2, 3],
             [-3, 5, 6],
             [7, 8, 9]],

            [[-3, 5, 6],
             [-1, -2, 3],
             [7, 8, 9]],

            [[-5, -4, -4],
             [10, -3, 5],
             [-9, 6, -2]],

            [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]]

"""     Print all of mat_list   """
# for mat in mat_list:
#     print(f"Mat.{mat_list.index(mat)+1}:", end="\n\t")
#     for row in mat:
#         for col in row:
#             print(f"{col:2}", end=" ")
#         print("", end="\n\t")
#     print()

matA = mat_list[0]
matB = mat_list[1]

rowA = len(matA)
colA = len(matA[0])

rowB = len(matB)
colB = len(matB[0])


"""     Print matrix A * B =    """
for row in matA:
    for col in row:
        print(f"{col:2}", end=" ")
    print()

print("\t*")

for row in matB:
    for col in row:
        print(f"{col:2}", end=" ")
    print()

print("\t=")
# matC = [[0 for col in range(5)] for row in range(10)]
# for row in matC:
#     print(row)

"""     Control of matrix dimensions    """
if colA == rowB:

    rowC = rowA
    colC = colB

    matC = [[0 for col in range(colC)] for row in range(rowC)]

    for r in range(rowC):
        for c in range(colC):

            """     Dot product calculation     """
            add = 0
            for d in range(colA):
                add += matA[r][d] * matB[d][c]

            matC[r][c] = add

            """     Final matrix print      """
            print(f"{matC[r][c]:2}", end=" ")
        print()

print()
mat = matMult(matA, matB)
for row in mat:
    for col in row:
        print(f"{col:2}", end=" ")
    print()
