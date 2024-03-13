
# def combination(list):

def comb_Prt(prefix, items):

    print(comb, end=" ")

    for i in range(len(items)):
        comb_Prt(prefix + items[i], items[:i] + items[i + 1:])


def comb_Ind(prefix, indfix, items, item_ind):

    comb_Lst.append(prefix)
    combInd_Lst.append()

    for i in range(len(items)):
        comb_Ind(prefix + items[i], indfix, items[:i] + items[i + 1:], item_ind[:i] + item_ind[i + 1:])

def comb(prefix, items):

    comb_Lst.append(prefix)

    for i in range(len(items)):
        comb(prefix + items[i], items[:i] + items[i + 1:])


items = ['A', 'B', 'C', 'D']
items_indx = [0, 1, 2, 3]

# items = ['🟩', '🟨', '🟧', '🟥']
# items = ['a', 'b', 'c']

comb_Lst = []
combInd_Lst = []

print("Combinations", end="\n\t")
comb("", items)

# print(comb_Lst)

for i, cmb in enumerate(comb_Lst):
    print(cmb, end="  ")

    if (i+1) % 6 == 0:
        print("", end="\n\t")



