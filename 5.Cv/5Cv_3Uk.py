"""
Násobení vektoru a matice

    Napište funkci multiVecMat(v,m), která vypočte součin vektoru v∈R^N a matice m∈R^(N×N).
    Pokud nesouhlasí rozměry matice a vektoru, pak funkce vrací None.

    Vypočtete výsledek násobení m⋅v:
        m=[[0,0,1],[0,1,0],[1,0,0]]
        v=[2, 4, 6]

"""


MatA = [[1, 2], [3, 4]]
MatB = [[5, 6], [7, 8]]

rowA = len(MatA)
colA = len(MatA[0])
rowB = len(MatB)
colB = len(MatB[0])

for r in range(rowA):
    for c in range(colA):
        print(MatA[r][c], end=" ")
    print()

print("*")

for r in range(rowB):
    for c in range(colB):
        print(MatB[r][c], end=" ")
    print()

print("=")

add = 0
MatC = [[0, 0], [0, 0]]


for r in range(rowA):
    for c in range(colA):
        add = 0
        for a in range(colB):
            add += MatA[r][a] * MatB[a][c]
        MatC[r][c] = add
        print(MatC[r][c], end=" ")
    print()


# def multiVecMat(v, m):
#
#     colV = len(v)
#     rowM = len(m)
#     colM = len(m[0])
#
#     print(f"colV: {colV}")
#     print(f"rowM: {rowM}")
#
#     for r in range(rowM):
#         for c in range(colV):
#             add = 0
#
#             for a in range(colM):
#

m=[[0,0,1],
   [0,1,0],
   [1,0,0]]

v=[2, 4, 6]

# multiVecMat(v, m)


