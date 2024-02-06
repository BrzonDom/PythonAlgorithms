"""
Metoda půlení intervalu hledá řešení obecné rovnice f(x)=0, kdy známe dva body x1 a x2 takové, že f(x1)<0 a f(x2)>0.

    Algoritmus rozpůlí interval mezi body x_1 a x_2,
    tedy nalezne bod x′=x_1+x_22 a pokud je f(x′)<0
    pak nahradí bod x1 bodem x′, jinak nahradí bod x2 bodem x′.

    Výše uvedený krok se opakuje dokud není |x1−x2|<ϵ, kde ϵ je požadovaná přesnost.

    V případě hledání třetí odmocniny z čísla y:

        f(x)=x3−y

    Pokud f(x)=0,

        tak x3−y=0, což lze zapsat jako x3=y a tedy x=3√y

    Napište program, který nalezne třetí odmocninu zadaného čísla y
    na 8 desetinných míst

    (výpočet ukončíte pokud |x1−x2|<0.000000001).

    Na počátku zvolte x1=0 a x2=y pro kladná y>1, x1=y a x2=0 pro záporná y<−1, a x1=−1 a x2=1 v ostatních případech.

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