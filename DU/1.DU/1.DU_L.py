"""
Napište program int_sum.py, který počítá součet mocnin posloupnosti čísel

    Vstup: dvě řádky ze standardního vstupu, které postupně obsahují celá čísla a, b

    Výstup: celé číslo, které je součtem výrazů i^4 pro všechna celá čísla i
        - pokud je a≤b od a do b (včetně)
        - pokud je a>b od b do a (včetně)

    Předpokládejte, že všechny vstupy jsou zadány korektně a vstup obsahuje dvě řádky, každá řádka obsahuje pouze jedno celé číslo.
    Výsledek musí být celé číslo.
"""

"""
Příklady:
    Vstup:
        2
        5
    Výstup:
        978
    
    Vstup:
        3
        -3
    Výstup:
        196
    
    Vstup:
        9
        9
    Výstup:
        6561
"""

In1 = 2
In2 = -3

# In1 = input()
# In2 = input()

Res = 0

if (In1 <= In2):
    Rng = range(In1, In2+1)
    Last = In2
elif (In1 > In2):
    Rng = range(In2, In1+1)
    Last = In1

for i in Rng:
    Res += (i**4)

print("Vstup:")
print("\t" + str(In1))
print("\t" + str(In2))
print("Výstup:")
print("\t" + str(Res))

print("\n")

print("Range:", end=" ")
for i in Rng:
    print(i, end=" ")

print("")
print("Expresion:", end=" ")
for i in Rng:
    if (i == Last):
        Str = "({})^4 = {}"
        print(Str.format(i, Res))
    else:
        Str = "({})^4 +"
        print(Str.format(i), end=" ")
