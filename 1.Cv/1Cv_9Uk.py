"""
Větvení programu

    Pokud potřebujeme vykonat část programu jen při splnění určitých podmínek, použijeme příkaz if. Jeho nejdednodušší tvar je:

        if podmínka:
           kód

    V tomto případě se nejdříve vyhodnotí podmínka a je-li splněna, je vykonán příslušný kód. Pokud podmínka splněna není, kód se nevykoná.

    Příklad: vytiskni “sudé číslo” pokud proměnná a
    obsahuje sudé číslo.

        if (a % 2) == 0:
           print("sude cislo")

    Obecnější tvar větvení je

        if podmínka1:
           kód1
        elif podmínka2:
           kód1
        else:
           kód2

    V tomto případě lze použít vícero bloků elif.

    Příklad: pokud je v proměnné a záporné číslo, vytiskni “zaporne”, jinak vypis jestli je číslo v proměnné a liché nebo sudé.

        a = 4
        if a < 0:
            print("zaporne")
        elif (a % 2) == 0:
            print("sude")
        else:
            print("liche")

    Bez elif bychom museli odsazovat tímto způsobem:

        a = 4
        if a < 0:
            print("zaporne")
        else:
            if (a % 2) == 0:
                print("sude")
            else:
                print("liche")

"""

a = 4

if (a % 2) == 0:
    print("sude cislo")

if a < 0:
    print("zaporne")
elif (a % 2) == 0:
    print("sude")
else:
    print("liche")

if a < 0:
    print("zaporne")
else:
    if (a % 2) == 0:
        print("sude")
    else:
        print("liche")