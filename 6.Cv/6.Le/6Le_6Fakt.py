"""
Rekurze: Faktoriál

    Přímá definice:      n! = n · (n − 1) · (n − 2) · ... · 2 · 1
    Rekurzivní definice: n! = n · (n − 1)!

    Základní (bázový) případ: 0! = 1! = 1
    Základní případ slouží jako ukončovací podmínka
"""

def fact(n):

    """     Basic case      """
    if n == 0 or n == 1:
        return 1

    return n * fact(n-1)

nMax = 6
fN = 1

print("Factorial:")

for n in range(nMax):

    fN = 1

    print(f"\t!n = !{n} = ", end="")
    for i in range(n):
        fN *= (i+1)

        if i != n-1:
            print(f"{i+1}", end=" * ")
        else:
            # print(f"{i + 1} = {fN}")
            print(f"{i+1}", end=" = ")

    print(f"{fN}")

    print(f"\t!n = !{n} = {fact(n)}")
    print()