"""
Napište program root.py který metodou půlení intervalu spočítá kořen polynomu 5-tého stupně
    a_5⋅x^5 + a_4⋅x^4 + a_3⋅x^3 + a_2⋅x^2 + a_1⋅x + a_0

Vstup:
    šest řádek, obsahující postupně koeficienty a5 až a0. Koeficient a5 je na první řádce, a0 na poslední řádce.

Výstup:
    jedno reálné číslo, které je kořenem zadaného polynomu.

Pro výpočet použijte metodu půlení intervalu.
Výsledek nalezněte s přesností na 9 desetinných míst (výpočet ukončíte pokud |x1−x2|<0.0000000001).
Pro prvotní nastavení krajních mezí víte že:
    - kořen x∈(−10,10)
Použití jakékoliv knihovní funkce (např. math.log) není dovoleno, program volající cizí funkce nebude hodnocen.
"""

"""
Příklady:
    Vstup:
        4
        -12
        1
        -30
        11
        -14

    Výstup:
        3.5
"""

# import sys

def f(a_, x):

        # a_5⋅x^5 + a_4⋅x^4 + a_3⋅x^3 + a_2⋅x^2 + a_1⋅x + a_0
    fnkc = a_[5] * (x**5) + a_[4] * (x**4) + a_[3] * (x**3) + a_[2] * (x**2) + a_[1] * x + a_[0]

    return (fnkc)

def inter(a_, x1, x2):

    if f(a_, x1) < 0 and f(a_, x2) > 0:
        return [x1, x2]
    elif f(a_, x1) > 0 and f(a_, x2) < 0:
        return [x2, x1]
    # else:
    #     # print("Error v rozmezení intervalu")
    #     sys.exit()

def bisec_metod(a_, a, b, e):

    while abs(a - b) > e:
        c = (a + b) / 2

        if (f(a_, c) < 0):
            a = c
        elif (f(a_, c) > 0):
            b = c

    return [a, b]


        # 4, -12, 1, -30, 11, -14
    # a_koef = [-14, 11, -30, 1, -12, 4]

a_koef = []
for i in range(6):
    a_koef.append(int(input()))
a_koef.reverse()

#     # print("a koeficienty:", end="\n\t")
#     # for i in a_koef:
#     #     print(i, end=" ")
#
#     # print()
# x1 = -10
# x2 = 10
#
# a = inter(a_koef, x1, x2)[0]
# b = inter(a_koef, x1, x2)[1]
# e = 0.0000000001
#
#     # print(f"\na = {a}\nb = {b}\ne = {e}\n")
#
# k_a = bisec_metod(a_koef, a, b, e)[0]
# k_b = bisec_metod(a_koef, a, b, e)[1]
#
#     # print(f"k_a: {k_a}\t f(k_a): {f(a_koef, k_a)}\nk_b: {k_b}\t f(k_b): {f(a_koef, k_b)}\n")
#     # print(f"k_a rounded: {round(k_a, 1)}\nk_b rounded: {round(k_b,1)}")
#
# if round(k_a, 1) == round(k_b, 1):
#     print(round(k_a, 1))

"""----Simplified----"""

a = -10
b = 10
e = 0.0000000001

while abs(a - b) > e:
    c = (a + b) / 2

    if (f(a_koef, c) < 0):
        a = c
    else:
        b = c

print(round(a, 9))
