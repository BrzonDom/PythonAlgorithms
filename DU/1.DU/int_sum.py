"""
Napište program int_sum.py, který v posloupnosti čísel najde podposloupnost, která má největší součet.

Vstup:
    - jedna řádka ze standarního vstupu
    - řádka obsahuje posloupnost celých čísel x_1,...,x_n oddělených mezerou
    - pro načtení a převedení vstupu na pole celých čísel můžete použít příkaz
        nums = list(map(int, input().split()))

Výstup: D S, kde D je délka a S je součet nalezené podposloupnosti

Poznámka:
    - Pole na vstupu obsahuje vždy alespoň jedno číslo.
    - Podposloupnost s jedním číslem je také podposloupnost s délkou 1. Podposloupnost musí mít alespoň jedno číslo.
    - Posloupnost obsahuje i záporná čísla.
    - Snažte se najít co nejrychlejší algoritmus, který by fungoval i pro dlouhé sekvence o 20000 prvcích rychle (nejlépe do 1s).
    - Snažte se analyzovat, co musí pro podposloupnost s největším součtem platit a zkusit procházet prvky vstupní posloupnosti pouze jednou.
    - Příklad:
        podposloupnost s největším součtem v posloupnosti 3 1 -6 2 4 1 -3 2 -5 4 -5 je 2 4 1, jenž má největší možný součet 7. Výstupem programu bude délka podposloupnosti a její součet, tedy 3 7
"""

"""
Příklady:

    Vstup:
       1 2 3 4 5 6
    Výstup:
        6 21

    Vstup:
        -2 -1 -3 -4 -5 -6
    Výstup:
        1 -1

    Vstup:
        1 2 5 -10 8 -3 2 1 -1 2 -2 5 -16 8 -10 2 3
    Výstup:
        8 12
"""

# In1 = 2
# In2 = -3

In1 = int(input())
In2 = int(input())

Res = 0

if (In1 <= In2):
    Rng = range(In1, In2+1)
    Last = In2
elif (In1 > In2):
    Rng = range(In2, In1+1)
    Last = In1

for i in Rng:
    Res += (i**4)

# print("Vstup:")
# print(str(In1))
# print(str(In2))
    # print("\t" + str(In1))
    # print("\t" + str(In2))
# print("Výstup:")
print(str(Res))
    # print("\t" + str(Res))

# print("\n")

# print("Range:", end=" ")
# for i in Rng:
#     print(i, end=" ")
#
# print("")
# print("Expresion:", end=" ")
# for i in Rng:
#     if (i == Last):
#         Str = "({})^4 = {}"
#         print(Str.format(i, Res))
#     else:
#         Str = "({})^4 +"
#         print(Str.format(i), end=" ")