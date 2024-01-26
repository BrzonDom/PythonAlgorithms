"""
Hanojské věže

    Máme tři věže (označme je A,B a C), na kterých je rozmístěno n disků o různých velikostech.

    Vždy platí, že menší disk smí být položen na větší disk, ne naopak.

    Na začátku je všech n disků na věži A, přičemž jsou seřazeny podle
    velikosti (největší leží dole, nejmenší nahoře). Cílem je přemístit disky tak,
    aby všechny ležely na věži C.

    Podrobné vysvětlení řešení je ve videu
        Hanojské věže: https://www.youtube.com/watch?v=7M-FMkA4G4o
"""

towers = [[3, 2, 1], [], []]

def hanoiSol(n, A, C, B):

    if n>0:
        hanoiSol(n-1, A, B, C)
        twr = towers[A].pop()

        if (len(towers[C])) == 0 or towers[C][-1] > twr:
            towers[C].append(twr)

        else:
            print("ERROR")

        print(f"A: {towers[0]}")
        print(f"B: {towers[1]}")
        print(f"C: {towers[2]}")
        print()

        hanoiSol(n-1, B, C, A)

hanoiSol(len(towers[0]), 0, 2, 1)

#   [#||#]
#  [##||##]
# [###||###]