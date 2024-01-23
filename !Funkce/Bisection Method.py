"""
Metoda půlení intervalu hledá řešení obecné rovnice f(x) = 0, kdy známe dva body x_1 a x_2 takové, že f(x_1) < 0 a f(x_2) > 0.
    - Algoritmus rozpůlí interval mezi body x_1 a x_2, tedy nalezne bod x′ = (x_1 + x_2) / 2 a pokud je f(x′) < 0 pak nahradí bod x_1 bodem x′, jinak nahradí bod x_2 bodem x′.
    - Výše uvedený krok se opakuje dokud není |x_1 − x_2| < e, kde e je požadovaná přesnost.

V případě hledání třetí odmocniny z čísla y:
    - f(x) = x^3 − y
    - Pokud f(x)=0, tak x3−y=0, což lze zapsat jako x3=y a tedy x=3√y
"""

def f(x):
    fnkc = (x - 1)**2 - 4
    return(fnkc)

def interval(a, b):
    if f(a) < 0 and f(b) > 0:
        return [a, b]
    elif f(a) > 0 and f(b) < 0:
        return [b, a]
    else:
        return ["error", "error"]

def bisec_metod(a, b, e):

    while abs(a - b) > e:
        c = (a + b) / 2

        if (f(c) < 0):
            a = c
        elif (f(c) > 0):
            b = c

    return [a, b]


a0 = 10
    # f(a) < 0
b0 = 0
    # f(b) > 0
e = 0.001

a = interval(a0, b0)[0]
b = interval(a0, b0)[1]
print(f"\na = {a}\nb = {b}\ne = {e}\n")

c = (a + b) / 2


# while (abs(f(a)) > 0.1 or abs(f(b)) > 0.1):

while (abs(a - b) > e):
    c = (a + b) / 2

    if (f(c) < 0):
        a = c
    elif (f(c) > 0):
        b = c

print(f"a: {a}\t f(a): {f(a)}\nb: {b}\t f(b): {f(b)}")

a = 0
b = 10

print(f"\n\na = {a}\nb = {b}\ne = {e}\n")

bisec_metod(a, b, e)
a = bisec_metod(a, b, e)[0]
b = bisec_metod(a, b, e)[1]

print(f"a: {a}\t f(a): {f(a)}\nb: {b}\t f(b): {f(b)}")