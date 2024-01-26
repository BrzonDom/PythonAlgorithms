"""
Rekurze: Umocňování

    Přímá definice:       x^n = ∏^n x = x_1 · x_2 · ... · x_n
    Rekurzivní definice:  x^n = x · x^(n-1)

    Základní (bázový) případ: x^0 = 1
"""

def expon(x, n):

    res = 1

    for _ in range(n):
        res = res * x

    return res

print("Exponentiation")
x = 10
n = 0
print(f"\tx^n = {x}^{n} = {expon(x, n)}")

x = 2
n = 10
print(f"\tx^n = {x}^{n} = {expon(x, n)}")

x = 2**(0.5)
n = 2
print(f"\tx^n = {x}^{n} = {expon(x, n)}")