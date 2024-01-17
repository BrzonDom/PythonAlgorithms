"""
Vstup programu

    Váš program často potřebuje zadat nějakou vstupní hodnotu.
    Standardní vstup programu je z terminálu funkce input:
    a = int(input())
    b = float(input(“Zadejte realne cislo:”))
    c = input(“Zadej cokoliv”)
    První dva příklady přetypují zadaný vstup na číslo celé, nebo reálné. To není vždy možné, třeba pokud zadáte chybně číslo 1a2. Jak tuto situaci ošetřit se dozvíte později.
    Zatím předpokládejte korektně zadané vstupy.
    Další možností je předat data jako argumenty příkazové řádky:

        import sys         # načtení modulu pro použití funkcí a proměnných modulu sys
        a = int(sys.argv[1])
        print("Zadana hodnota:")
        print(a)


    Příklad použití: python3 jmenoPythonProgramu.py 45
    Program vypíše argument: 45
"""

import sys  # načtení modulu pro použití funkcí a proměnných modulu sys

a = int(sys.argv[1])
print("Zadana hodnota:")
print(a)