"""
Rekurze: Umocňování

    Přímá definice:       x^n = ∏^n x = x_1 · x_2 · ... · x_n
    Rekurzivní definice:  x^n = x · x^(n-1)

    Základní (bázový) případ: x^0 = 1
"""

def expon_iter(x, n):

    res = 1

    for _ in range(n):
        res = res * x

    return res

def expon_recur(x, n):

    if n == 0:
        return 1

    return x * expon_recur(x, n-1)

print("Exponentiation")
x = 10
n = 0
print(f"\tx^n = {x}^{n} = {expon_iter(x, n)}")
print(f"\tx^n = {x}^{n} = {expon_recur(x, n)}")

x = 2
n = 10
print(f"\tx^n = {x}^{n} = {expon_iter(x, n)}")
print(f"\tx^n = {x}^{n} = {expon_recur(x, n)}")

x = 2**(0.5)
n = 2
print(f"\tx^n = {x}^{n} = {expon_iter(x, n)}")
print(f"\tx^n = {x}^{n} = {expon_recur(x, n)}")