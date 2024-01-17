"""
Výpočty v Pythonu

    Vytvořte program pocitani.py, který načte dvě čísla z příkazové řádky a vytiskne jejich součet, rozdíl, součin, podíl
    Pro načtení čísel použijte konstrukci

        import sys
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print(a+b)
        print(a-b)
        print(a*b)
        print(a/b)

    Zadejte vstupy (10, 20), (100.0, 120.0) a (55.5, 0). Jaké jsou výstupy?
"""

import sys

# a = float(sys.argv[1])
# b = float(sys.argv[2])
#
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

a_list = [10, 100.0, 55.5]
b_list = [20, 120.0, 0]

for a, b in zip(a_list, b_list):
    print(f"{a} + {b} = {a+b}")
    print(f"{a} - {b} = {a-b}")
    print(f"{a} * {b} = {a*b}")
    if b != 0:
        print(f"{a} / {b} = {a/b}")
    print()