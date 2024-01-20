"""
Inicializace a kopírování 2D polí

    Projdeme si inicializaci a kopírování 1D a více-D polí. Spusťte následující kód a na konci si vytiskněte jednotlivá pole.
    Co pozorujeme?
        # Inicializace pole
        a = [0] * 5

        # Jak správně zkopírovat pole?
        b = a
        c = a[:]
        d = list(a)

        a[3] = 3
        b[0] = -5
        c[4] = 4

    Spusťte následující kód a opět si na konci vypište jednotlivá pole.
        # Inicializace 2D pole přímo
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

        # Inicializace po řádcích
        f = []
        for i in range(3):
            f.append([i] * 3)

        # Inicializace po řádcích ve zkráceném zápisu
        g = [[i] * 3 for i in range(3)]

        # Jak správně zkopírovat pole?
        b = a
        c = a[:]
        d = list(b)
        e = [ r[:] for r in a ]
        f = [ list(a[i]) for i in range(len(a))]

        a[0][0] = -1
        b[0][1] = -2
        c[0],c[1]=c[1],c[0]
        d[1][0] = -3
        e[1][1] = -4

    Pokud chceme opravdovou kopii vícedimenzionálního pole, tvz. deep copy, můžeme použít modul copy a funkci deepcopy.
    Doplňte import a kopírování do předchozí ukázky a porovnejte výsledky.
        import copy
        d = copy.deepcopy(b)

"""

# Inicializace pole
a = [0] * 5

# Jak správně zkopírovat pole?
b = a
c = a[:]
d = list(a)

a[3] = 3
b[0] = -5
c[4] = 4

print("1.Part")

print(f"\tA:", end="\t")
for itm in a:
    print(f"{itm:2}", end=" ")
print()

print(f"\tB:", end="\t")
for itm in b:
    print(f"{itm:2}", end=" ")
print()

print(f"\tC:", end="\t")
for itm in c:
    print(f"{itm:2}", end=" ")
print()


print(f"\tD:", end="\t")
for itm in d:
    print(f"{itm:2}", end=" ")
print("\n")
    # print("", end="\n\t")

print("2.Part")

# Inicializace 2D pole přímo
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Inicializace po řádcích
f = []
for i in range(3):
    f.append([i] * 3)

# Inicializace po řádcích ve zkráceném zápisu
g = [[i] * 3 for i in range(3)]

# Jak správně zkopírovat pole?
b = a
c = a[:]
d = list(b)
e = [r[:] for r in a]
f = [list(a[i]) for i in range(len(a))]

a[0][0] = -1
b[0][1] = -2
c[0], c[1] = c[1], c[0]
d[1][0] = -3
e[1][1] = -4

print(f"\tA:", end="\n\t")
for row in a:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()

print(f"\tB:", end="\n\t")
for row in b:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()

print(f"\tC:", end="\n\t")
for row in c:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()

print(f"\tD:", end="\n\t")
for row in d:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()

print(f"\tE:", end="\n\t")
for row in e:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()

print(f"\tF:", end="\n\t")
for row in f:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()

print(f"\tG:", end="\n\t")
for row in g:
    for itm in row:
        print(f"{itm:2}", end=" ")
    print("", end="\n\t")
print()