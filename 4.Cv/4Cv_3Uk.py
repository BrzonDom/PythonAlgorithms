"""
Nalezení maxima

    Napište funkci, která vrací největší hodnotu v poli a zároveň vrací index tohoto prvku
    Pro pole nulové délky vrací index -1.
    Pozor: je třeba předpokládat, že v poli mohou být jakékoliv hodnoty (kladné, nuly, záporné)!

"""


def my_findMax(Set):

    if len(Set) == 0:
        return -1

    index_list = []
    index = 0
    Max = Set[0]

    for num in Set:

        if num > Max:
            Max = num
            index_list = [index]

        elif num == Max:
            index_list.append(index)

        index += 1

    print(f"Max: {Max}\n\tIndex: ", end="")
    for i in index_list:
        print(i, end=" ")

    return [num, index_list]




Set = [-20, -19, -5, -2, -1, 20, 5, 6, 7, 20, 9, 12, 16, 19, 8]

Max = max(Set)

index_list = []
index = 0

for num in Set:
    if Max == num:
        index_list.append(index)
    index += 1

print(f"Max: {Max}\n\tIndex: ", end="")
for i in index_list:
    print(i, end=" ")

print("\n")

my_findMax(Set)


