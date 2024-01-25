
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
colB = len(matB)

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

if colA == rowB:

    rowC = rowA
    colC = colB

    matC = [[0 for col in range(colC)] for row in range(rowC)]

    for r in range(rowC):
        for c in range(colC):
            add = 0
            for d in range(colA):
                add += matA[r][d] * matB[d][c]

            matC[r][c] = add
            print(f"{matC[r][c]:2}", end=" ")
        print()
