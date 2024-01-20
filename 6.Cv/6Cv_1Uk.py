"""
Life

    Hru Life navrhl v roce 1970 matematik John Horton Conway.
    Historie , Coding challenge
    Pravidla hry jsou jednoduchá:
        pokud jsou v okolí jedné buňky živé právě 3 buňky, pak v této buňce život vznikne (nebo zůstane)
        pokud je buňka živá a v jejím okolí jsou právě 2 živé buňky, pak tato buňka bude žít i nadále
        v ostatních případech buňka zahyne buď na osamění, nebo přemnoženost
    Uvažujte osmiokolí: 8 sousedních buněk.
    Uvažujte uzavřený svět, tedy sousední políčko pro první pole řádku je poslední pole řádku, sousední pole pro první řádek je poslední řádek

    Napište program, který bude simulovat 40 kroků hry life pro toto počáteční pole:
        a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    Vygenerování prázdného pole
        [[0]*len(a[0]) for i in a]

    Pro lepší zobrazení udělejte po každém kroku pauzu
        import time
        time.sleep(0.5)

    Také můžete vylepšit zobrazení tak, že místo 1 budete tisknout X a místo 0 mezeru
        ''.join('X' if i!=0 else ' ' for i in x)

"""

def showMat(Mat):

    print("", end="\n\t")

    for row in Mat:
        for col in row:
            if col == 0:
                print("⬜", end="")
            elif col == 1:
                print("⬛", end="")
            elif col == 2:
                print("🟥", end="")
        print("", end="\n\t")



a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

field = [
    [[0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],

     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 1, 1, 1, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 1, 0, 1, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 1, 1, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 1, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],

     [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0]],
        ]

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


rows = len(a)
cols = len(a[0])

print(f"Rows:    {rows}")
print(f"Columns: {cols}")

# for t in range(40):
#     field[t+1] = field[t]
#     for r in range(rows):
#         for c in range(cols):
#
#             sum = 0
#             if (r == 0) and (c == 0):
#                 if field[t][r+1][c]:
#                     sum += 1
#                 if field[t][r][c+1]:
#                     sum += 1
#                 if field[t][r+1][c+1]:
#                     sum += 1
#
#
#
            # field[t][r-1][c-1]
            # field[t][r][c-1]
            # field[t][r+1][c-1]
            #
            # field[t][r-1][c]
            # field[t][r+1][c]
            #
            # field[t][r-1][c+1]
            # field[t][r][c+1]
            # field[t][r+1][c+1]




for t in range(40):
    print(f"Turn {t+1}:\n", end="\t")
    field.append([[0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],

                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],
                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0],

                  [0,    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,    0]])


    for r in range(1, rows+1):
        for c in range(1, cols+1):
            if field[t][r][c] == 0:
                print("⬜", end="")
            elif field[t][r][c] == 1:
                print("🟥", end="")

            # print(field[t][r][c], end=" ")

            sur_sum = 0

            if field[t][r-1][c-1]:
                sur_sum += 1
            if field[t][r][c-1]:
                sur_sum += 1
            if field[t][r+1][c-1]:
                sur_sum += 1

            if field[t][r-1][c]:
                sur_sum += 1
            if field[t][r+1][c]:
                sur_sum += 1

            if field[t][r-1][c+1]:
                sur_sum += 1
            if field[t][r][c+1]:
                sur_sum += 1
            if field[t][r+1][c+1]:
                sur_sum += 1

            if sur_sum == 3:
                field[t+1][r][c] = 1
            elif sur_sum == 2 and field[t][r][c]:
                field[t+1][r][c] = 1
            else:
                field[t+1][r][c] = 0

        print("\n\t", end="")
    print("\n", end="")


# print(field[0])



