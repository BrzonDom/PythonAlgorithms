"""
Nalezení druhého největšího prvku v poli

    Napište funkci, která vrací druhou největší hodnotu v poli a zároveň vrací index tohoto prvku
    Pro pole délky méně než 2 vrací index -1.
    Pozor: je třeba předpokládat, že v poli mohou být opět jakékoliv hodnoty (kladné, nuly, záporné)!

"""


Set = [-5, -18, 6, -14, 6, -11, 8, -3, 20, -4, 17, -17, -1, 9, -20, 19, -15, 1, 18, -8, 4, 13, -12, 2, -13, 7, -2, -9, 11, 20]

# Search = list(set(Set))
# Search.sort()
Search = Set.copy()
Search = list(set(Search))
Search.sort()

print(f"Set:    {Set}")
print(f"Search: {Search}")

Max = Search[-1]
sMax = Search[-2]

print()

print(f"Max = {Max}")
print(f"2ndMax = {sMax}")

index_list = []
index = 0

for num in Set:

    if num == sMax:
        index_list.append(index)

    index += 1

print("\n")

print(f"2ndMax: {sMax}\n\tIndex: ", end="")
for i in index_list:
    print(i, end=" ")



