"""
Nalezení maxima

    Napište funkci, která vrací největší hodnotu v poli a zároveň vrací index tohoto prvku
    Pro pole nulové délky vrací index -1.
    Pozor: je třeba předpokládat, že v poli mohou být jakékoliv hodnoty (kladné, nuly, záporné)!

"""


def my_findMax(Set):

    if len(Set) == 0:
        print("Set of numbers not given")
        return False, []

    index = []
    Max = Set[0]

    for n, num in enumerate(Set):

        if num > Max:
            Max = num
            index = [n]

        elif num == Max:
            index.append(n)

    print(f"Max: {Max}\n\tIndex: ", end="")
    for i in index:
        print(i, end=" ")

    return num, index



Set = [-20, -19, -5, -2, -1, 20, 5, 6, 7, 20, 9, 12, 16, 19, 8]

print(f"List of numbers: {Set}\n")

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

Max, index = my_findMax(Set)

print("\n")

if type(Max) != bool:
    print(f"Maximum: {Max}")
    print(f"Found at index: ", end="")
    for i in index:
        print(i, end=" ")


