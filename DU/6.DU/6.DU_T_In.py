"""
Těžká varianta

    Napište program rectangle.py, který v matici celých čísel zadané na příkazové řádce (sys.argv[1]) najde největší souvislou podmatici libovolného rozměru, která obsahuje pouze záporné hodnoty. Příklad volání:

        python3 rectangle.py matice.txt

    Výstupem programu jsou souřadnice levého horního rohu a pravého dolního rohu podmatice. Na prvním řádku výstupu je levý horní roh ve formátu řádek sloupec, na druhém řádku pravý dolní roh. Řádky i sloupce se číslují od 0.
    Velikost podmatice je určena jejím počtem prvků.
    Snažte se, aby Váš program byl co nejefektivnější, ideálně, aby jeho časová složitost odpovídala velikosti matice. Bodové ohodnocení této úlohy bude záviset na efektivnosti (rychlosti) Vašeho algoritmu.
    Pokud existuje více řešení, vypište libovolné z nich.
    Nastudujte si nejrychlejší způsob nalezení maximálního obdélníku pod histogramem Část 1 a Část 2
    Timeout na výpočet je: 50 sekund. Toto platí i pro velké matice, které si můžete stáhnout níže. Na nich je dobře patrný rozdíl mezi lineárním algoritmem O(n), algoritmem O(n⋅log(n)) a O(n^2), kde n je počet prvků matice.


Příklad

    Matice matice.txt:

         1 -9 -2   8   6  1
         8 -1 -11 -7   6  4
        10 12 -1  -9 -12 14
         8 10 -3  -5  17  8
         6  4 10 -13 -16 19

    Výstup:

        1 2
        3 3

"""


import string


def StrArr_IntArr(str):

    res = [int(element) for element in str.split()]

    return res

def IntArr_BinMat(mat_int):

    mat_bin = [[]]

    for a, arr in enumerate(mat_int):
        for num in arr:
            if num < 0:
                mat_bin[a].append(1)
            else:
                mat_bin[a].append(0)

        if a+1 == len(mat_int):
            break
        mat_bin.append([])

    return mat_bin

def BinMat_VizMat(mat_bit):

    mat_viz = [[]]

    for r, row in enumerate(mat_bit):
        for num in row:
            if num:
                mat_viz[r].append("⬜")
            else:
                mat_viz[r].append("⬛")

        if r+1 == len(mat_bit):
            break
        mat_viz.append([])

    return mat_viz


source = "rectangle"

in_source = f"data/{source}.txt"
out_source = f"data/{source}_out.txt"
vis_source = f"data/{source}_vis.txt"

print(f"Source: {in_source}\n")

in_file = open(in_source, "r")

# out_file = open(out_source, "w")
# out_file.close()
# out_file = open(out_source, "a")
#
# vis_file = open(vis_source, "w")
# vis_file.close()
# vis_file = open(vis_source, "a")


# lineCnt = 0
# itemCnt = 0

mat_org = [[]]
mat_str = []
mat_int = []
# mat_bin = []


print("Source print:")

for line in in_file:
    print(line, end="")
    mat_str.append(line)
    # print(Str_IntArr(line))
    # mat_int.append(Str_IntArr(line))


print("\nMat_str print:")

for index in range(len(mat_str)):
    print(mat_str[index], end="")

# print("\nMat_str print:")
#
# # for row in mat_str:
# #     print(row, end="")
# print(mat_str)

# print("\nMat_int print:")

for line in mat_str:
    # print(line, end="")
    # print(Str_Spl_IntArr(line))
    mat_int.append(StrArr_IntArr(line))


print("\nMat_int print4:")

for arr in mat_int:
    for n, num in enumerate(arr):
        if n+1 == len(arr):
            print(f"{num:3}")
            break
        print(f"{num:3}", end=" ")

mat_bin = IntArr_BinMat(mat_int)

print("\nMat_bin print:")

for arr in mat_bin:
    for n, num in enumerate(arr):
        if n+1 == len(arr):
            print(num)
            break
        print(num, end=" ")


print("\nMat_bin visual:")

for arr in mat_bin:
    for num in arr:
        if num:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()
