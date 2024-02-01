"""
Lehká varianta: Babylonská věž (zjednodušená)

    Babylonská věž (hlavolam): hlavolam obsahující celkem 35 kuliček o 6 různých barvách (5 barev má 6 kuliček, 1 barva má pouze 5), které jsou uspořádány v 6×6 poli. Cílem hlavolamu je srovnat kuličky tak, aby každý sloupec obsahoval pouze kuličky jedné barvy a nebo prázdné místo.

        Chybějící kulička umožňuje přesun sousední kuličky na prázdné místo.
        Věž je cyklická v horizontálním směru. To znamená, že lze rotovat celým řádkem. To umožňuje posunutí vlevo či vpravo všech kuliček v jednom řádku.

    Babylonská věž (v ALP):

        Stejný problém, avšak ne pro věž o rozměrech 6×6, ale menší a také nečtvercové.
        Reprezentována 2D maticí.
        Kuličky jedné barvy mají stejný odstín. Není třeba je ve sloupci třídit dle odstínu jako tomu je u některých verzí Babylonské věže.

    Úkol:

        Napište program babylon.py, který najde řešení zmenšené Babylónské věže v nejmenším počtu kroků.

    Vstup:

        Babylonská věž reprezentována 2D maticí o rozměrech M x N, které reprezentují:
            M: počet kuliček jedné barvy,
            N: počet barev.
        Hodnoty v matici reprezentují barvy kuliček na dané pozici takto:
            0: prázdné místo,
            1, 2, …, N: barva kuličky.
        Matice bude programu předána v argumentu programu, využijte tedy sys.argv[1].
        Příklad věže 3×3 (tedy 3 barvy, každá po 3 kuličkách, krom barvy 3, která má kuličky pouze 2):

        1 2 3
        1 2 0
        2 1 3


    Povolené akce:

        Pro zjednodušení v ALP je v každém stavu věže (neboli uspořádání kuliček) možné využít pouze těchto 4 akcí:
            Rotace řádku vpravo: posun všech kuliček n-tého řádku o 1 doprava.
                Značení: r n 1 (rotace řádku s indexem n o 1 vpravo)
            Rotace řádku vlevo: posun všech kuliček n-tého řádku o 1 doleva.
                Značení: r n -1 (rotace řádku s indexem n o 1 vlevo)
            Přesun kuličky nahoru do prázdného místa.
                Značení: m -1 (posun kuličky pod prázdným místem nahoru)
                Pozor: lze aplikovat pouze pokud prázdné místo není ve spodní řadě
            Přesun kuličky dolů do prázdného místa.
                Značení: m 1 (posun kuličky nad prázdným místem dolů)
                Pozor: lze aplikovat pouze pokud prázdné místo není v horní řadě

"""


def right(tower, row):
    tower[row] = tower[row][-1:] + tower[row][:-1]
    return tower


def left(tower, row):
    tower[row] = tower[row][1:] + tower[row][:1]
    return tower


def up(tower):
    # for row in tower[:-1]:
    #     for col in row:
    #         if col == 0:

    for r in range(len(tower)-1):
        for c in range(len(tower[0])):
            if tower[r][c] == 0:
                tower[r][c], tower[r+1][c] = tower[r+1][c], tower[r][c]
                return tower
    return tower


def down(tower):
    for r in range(1, len(tower)):
        for c in range(len(tower[0])):
            if tower[r][c] == 0:
                tower[r][c], tower[r-1][c] = tower[r-1][c], tower[r][c]
                return tower
    return tower



tower = [[1, 2, 3],
         [1, 2, 0],
         [2, 1, 3]]

print("Options:")
print("\t'd' for Right")
print("\t'a' for Left")
print("\t'w' for Up")
print("\t's' for Down")
print("\t'q' to quit")
print()

print("Original tower:")


for row in tower:
    for col in row:
        print(col, end=" ")
    print()
print()


# print("Right:", end="\n\t")
#
# tower = right(tower, 1)
#
# for row in tower:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()
#
# print("Left:", end="\n\t")
#
# tower = left(tower, 1)
#
# for row in tower:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()
#
# print("Up:", end="\n\t")
#
# tower = up(tower)
#
# for row in tower:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()
#
# print("Down:", end="\n\t")
#
# tower = down(tower)
#
# for row in tower:
#     for col in row:
#         print(col, end=" ")
#     print("", end="\n\t")
# print()

# move = input()

# if move == "d":
#     print("Right")
# elif move == "a":
#     print("Left")
# elif move == "w":
#     print("Up")
# elif move == "s":
#     print("Down")
# else:
#     print("Wrong move")

move = "x"

while(move != "q"):

    print("Move: ", end="")
    move = input()

    if move == "d":
        # print("Right")
        print("\tRow: ", end="")
        move = int(input())
        right(tower, move)
    elif move == "a":
        # print("Left")
        print("\tRow: ", end="")
        move = int(input())
        left(tower, move)
    elif move == "w":
        # print("Up")
        up(tower)
    elif move == "s":
        down(tower)
        # print("Down")
    else:
        continue


    for row in tower:
        for col in row:
            print(col, end=" ")
        print("", end="\n")
    print()

