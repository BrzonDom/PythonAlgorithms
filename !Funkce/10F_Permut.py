"""
Permutace

    Výpis všech permutací

    Řešení rekurzí
"""

def prtPerm(prefix, items):

    if len(items) == 0:
        print(prefix, end=" ")
        # print(prefix)

    for i in range(len(items)):
        prtPerm(prefix + items[i], items[:i] + items[i+1:])


def perm(prefix, items):

    if len(items) == 0:
        # print(prefix, end=" ")
        perm_list.append(prefix)

    for i in range(len(items)):
        perm(prefix + items[i], items[:i] + items[i+1:])


items = ['A', 'B', 'C', 'D']
# items = ['🟩', '🟨', '🟧', '🟥']
# items = ['a', 'b', 'c']

perm_list = []

print("Permutation", end="\n\t")
perm("", items)

# print(perm_list)

for i, per in enumerate(perm_list):
    print(per, end="  ")

    if (i+1) % 6 == 0:
        print("", end="\n\t")
# prtPerm("", items)