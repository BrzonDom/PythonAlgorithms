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

# items = ['a', 'b', 'c', 'd']
items = ['a', 'b', 'c']

print("Permutation", end="\n\t")
prtPerm("", items)