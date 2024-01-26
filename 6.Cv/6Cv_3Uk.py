"""
Gaussova eliminační metoda

    Gaussova eliminační metoda je metodou řešení soustavy lineárních algebraických rovnic.
    GEM lze využít pro výpočet inverzní matice nebo determinantu matice.

Krok 1: Nalezení největšího prvku ve sloupci

    Napište funkci maximum(M, i), která pro zadanou matici M a index (číslo) i najde takový
    index řádku j v rozsahu range(i, len(M)) jehož absolutní hodnota M[j][i] je maximální.
    Využijte vestavěnou funkci abs.

Krok 2: Prohození řádku

    Napište funkci swap_rows(M, i), která prohodí řádek i a řádek s indexem j = maximum(M, i), pokud i != j.

Krok 3: Úprava řádku

    Napište funkci do_line(M, i), která zavolá funkci swap_rows(M, i) a pokud:
        M[i][i] != 0:
            celý řádek i matice M vydělí hodnotou M[i][i]
            od všech řádků r v rozsahu range(i + 1, len(M)) odečte M[r][i] - násobek řádku i
            vrátí hodnotu True
        jinak vrátí False

Krok 4: Gausova eliminace

    Napište funkci GEM(M), která pro všechna i z rozsahu range(len(m)) zavolá funkci do_line(M, i)
    Pokud je návratová hodnota funkce do_line() alespoň 1x False, metoda Gauss_elim() vrací False. V opačném případě vrací True.

Příklad

    Spusťte funkci GEM() pro matici:

        m=[[12,-7,3, 26],
           [4 ,5,-6, -5],
           [-7 ,8,9, 21]]

"""
import copy

def maximumAll(Mat, col):

    Max = abs(Mat[0][col])
    index = 0

    for row in range(1, len(Mat)):

        if Max < abs(Mat[row][col]):
            Max = abs(Mat[row][col])
            index = row

    return index


def maximum(Mat, col):

    if col >= len(Mat):
        return -1

    else:
        Max = abs(Mat[col][col])
        index = col

        for row in range(col+1, len(Mat)):

            if Max < abs(Mat[row][col]):
                Max = abs(Mat[row][col])
                index = row

        return index

def swap_rows(Mat, col):

    row = maximum(Mat, col)

    if col != row:

        swap = [col, row]
        swap_row = [copy.deepcopy(Mat[col]), copy.deepcopy(Mat[row])]

        Mat[swap[1]] = swap_row[0]
        Mat[swap[0]] = swap_row[1]

    return Mat


Mat = [[12, -7,  3, 26],
       [ 4,  5, -6, -5],
       [-7,  8,  9, 21]]

rows = len(Mat)
cols = len(Mat[0])

print(f"Rows: {rows}")
print(f"Cols: {cols}")

"""     Print matrix    """

print("Mat:", end="\n\t")

for row in Mat:
    for col in row:
        print(f"{col:2}", end=" ")
    print("", end="\n\t")
print()


"""     Manual maximum of all the columns  """

print("Manu. max.All:")

for c in range(cols):
    """     Loop through all columns    """
    index = 0

    """     Loop through all rows
                to find Max     """
    for r in range(rows):
        """     Loop through all rows
                    to find Max     """
        # print(Mat[r][c], end=" ")


        if r == 0:
            """     1. instance = initial values
                        Skips 1.loop    """

            Max = abs(Mat[0][c])
            rowMax = 0

        elif (abs(Mat[r][c]) > Max):
            """     Find the max of the column      """

            Max = abs(Mat[r][c])
            rowMax = index

        index += 1

    """     Print max values of the column    """
    print(f"\tCol {c}: Max = {Max} on Row {rowMax}")
print()


"""     Function maximum of all columns    """

print("Func. max.All:")

for c in range(cols):
    """     Loop through all columns    """

    """     Find maximum of the column      """
    r = maximumAll(Mat, c)

    """     Print max values of the column      """
    print(f"\tCol {c}: Max = {Mat[r][c]} on Row {r}")
print("\n")


"""     Manual maximum of matrix columns  """

print("Manu. max.:")

for c in range(cols):
    """     Loop through all columns    """
    maxLoop = False


    for r in range(c, rows):
        """     Loop through rows under diagonal
                    to find Max     """
        # print(Mat[r][c], end=" ")
        forDebug = Mat[r][c]

        if r == c:
            """     1. instance = initial values
                        Skips 1.loop    """

            Max = abs(Mat[r][c])
            maxLoop = True
            index = c
            rowMax = c

        elif (abs(Mat[r][c]) > Max):
            """     Find the max of the column      """

            Max = abs(Mat[r][c])
            rowMax = index

        index += 1

    """     Print max values of the column    """
    if maxLoop:
        print(f"\tCol {c}: Max = {Max} on Row {rowMax}")
print()


"""     Manual swap of rows     """

print("Manu. swap.rows:")
print("\tManu. max.:")
MatSwap = copy.deepcopy(Mat)

for c in range(cols):
    """     Loop through all columns    """
    maxLoop = False

    """     Manual maximum of matrix columns  """

    for r in range(c, rows):
        """     Loop through rows under diagonal
                    to find Max     """
        # print(Mat[r][c], end=" ")
        forDebug = MatSwap[r][c]

        if r == c:
            """     1. instance = initial values
                        Skips 1.loop    """

            Max = abs(MatSwap[r][c])
            maxLoop = True
            index = c
            rowMax = c

        elif (abs(MatSwap[r][c]) > Max):
            """     Find the max of the column      """

            Max = abs(MatSwap[r][c])
            rowMax = index

        index += 1

    """     Print max values of the column    """
    if maxLoop:
        print(f"\t\tCol {c}: Max = {Max} on Row {rowMax}")

        """     Manual swap of rows     """

        if c != rowMax:
            """     Check if swap has effect    """

            swap = [c, rowMax]
            swap_row = [copy.deepcopy(MatSwap[c]), copy.deepcopy(MatSwap[rowMax])]

            """     Row swap    """
            MatSwap[swap[1]] = swap_row[0]
            MatSwap[swap[0]] = swap_row[1]

            # for line in Mat:
            #     print(line)

"""     Print final swapped matrix  """
print("\n\tManu. swap.mat.:", end="\n\t\t")

for row in MatSwap:
    for col in row:
        print(f"{col:2}", end=" ")
    print("", end="\n\t\t")
print()


"""     Function maximum of matrix columns  """

print("Func. max.:")

for c in range(cols):
    """     Loop through all columns    """

    """     Find maximum of the column      """
    r = maximum(Mat, c)

    """     Print max values of the column      """
    if r == -1:
        continue
    print(f"\tCol {c}: Max = {Mat[r][c]} on Row {r}")
print("")

"""     Function swap of rows     """

print("Func. swap.rows:")
print("\tFunc. max.:")
MatSwap = copy.deepcopy(Mat)

for c in range(cols):
    """     Loop through all columns    """

    """     Find maximum of the column      """
    r = maximum(MatSwap, c)

    """     Print max values of the column      """
    if r == -1:
        continue
    print(f"\t\tCol {c}: Max = {abs(MatSwap[r][c])} on Row {r}")

    """     Swap rows to achieve final swapped matrix    """
    MatSwap = swap_rows(MatSwap, c)

print()

"""     Print final swapped matrix  """
print("\tFunc. swap.mat.:", end="\n\t\t")
for row in MatSwap:
    for col in row:
        print(f"{col:2}", end=" ")
    print("", end="\n\t\t")
print()