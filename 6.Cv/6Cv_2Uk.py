"""
Prohození řádků matice

    Napište program, který načte matici a následně permutaci, která definuje prohození řádků matice. Na výstup program vytiskne matici s řádky prohozenými podle zadané permutace.

"""
import copy


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


"""     Input matrix    """
# matrix = []
# print("Zadejte matici řádek po řádku. Když skončíte, zadejte 'end'.")
#
# while True:
#     row = input()
#     if row == 'end':
#         break
#     matrix.append(list(map(int, row.split())))

# print(matrix)


"""     List matrix     """
mat_list = [[[-1, -2, 3],
             [-3, 5, 6],
             [7, 8, 9],
             [2, 5, 6]],

            [[-3, 5, 6],
             [-1, -2, 3],
             [7, 8, 9]],

            [[-5, -4, -4],
             [10, -3, 5],
             [-9, 6, -2]]]

"""     Print all of mat_list   """
# for mat in mat_list:
#     print(f"Mat.{mat_list.index(mat)+1}:", end="\n\t")
#     for row in mat:
#         for col in row:
#             print(f"{col:2}", end=" ")
#         print("", end="\n\t")
#     print()

mat = mat_list[0]
row = len(mat)
col = len(mat[0])

"""     Print mat   """
print(f"{mat_list.index(mat)+1}.Mat {row}x{col}:", end="\n\t")
for line in mat:
    for itm in line:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()


"""     What rows to switch     """
row_swap = [0, 3]

print(f"To swap:")
print(f"\trow {row_swap[0]} : {mat[row_swap[0]]}")
print(f"\trow {row_swap[1]} : {mat[row_swap[1]]}")

perMat = [[0 for c in range(row)] for r in range(row)]

"""     Create an identity matrix   """
# print("Identity matrix:")
for r in range(row):
    for c in range(row):
        if r == c:
            perMat[r][c] = 1

        """     Print an identity matrix   """
    #     print(perMat[r][c], end=" ")
    # print()

"""     Create a permutation matrix   """
swaped = [copy.deepcopy(perMat[row_swap[0]]), copy.deepcopy(perMat[row_swap[1]])]

perMat[row_swap[1]] = swaped[0]
perMat[row_swap[0]] = swaped[1]

"""     Print a permutation matrix   """
print()
# print("Permutation matrix:")
for line in perMat:
    for itm in line:
        print(f"{itm:2}", end=" ")
    print()

print("*")

for line in mat:
    for itm in line:
        print(f"{itm:2}", end=" ")
    print()

print("=")

swapMat = matMult(perMat, mat)

for line in swapMat:
    for itm in line:
        print(f"{itm:2}", end=" ")
    print()