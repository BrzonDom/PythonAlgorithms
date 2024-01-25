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


def maximum(Mat, col):

    Max = abs(Mat[0][col])
    index = 0

    for row in range(1, len(Mat)):

        if Max < abs(Mat[row][col]):
            Max = abs(Mat[row][col])
            index = row

    return index


# def swap_rows(Mat, col):




Mat = [[12, -7,  3, 26],
       [ 4,  5, -6, -5],
       [-7,  8,  9, 21]]

rows = len(Mat)
cols = len(Mat[0])

print(f"Rows:    {rows}")
print(f"Columns: {cols}")

"""     Print matrix    """
print("Mat:", end="\n\t")
for row in Mat:
    for col in row:
        print(f"{col:2}", end=" ")
    print("", end="\n\t")
print()

"""     Manual maximum of a column  """

"""     Loop through all columns    """
for c in range(cols):
    index = 0

    """     Loop through all rows
                to find Max     """
    for r in range(rows):
        # print(Mat[r][c], end=" ")


        if r == 0:
            """     1. instance = initial values
                        Skips 1.loop    """

            Max = abs(Mat[0][c])
            row_Max = 0

        elif (abs(Mat[r][c]) > Max):
            """     Find the max of the column      """

            Max = abs(Mat[r][c])
            row_Max = index

        index += 1

    """     Print max values of the column    """
    print(f"Col {c}: Max = {Max} on row = {row_Max}")
print()

"""     Function maximum of a column    """

"""     Loop through all columns    """
for c in range(cols):

    """     Find maximum of the column      """
    r = maximum(Mat, c)

    """     Print max values of the column      """
    print(f"Col {c}: Max = {Mat[r][c]} on Row {r}")


