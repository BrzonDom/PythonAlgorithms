"""
Cykly

    Základní druhy cyklů

        for cyklus - procházení seznamu hodnot
        while cyklus - opakuj cyklus dokud platí podmínka

    Základní druhy cyklů

        for cyklus - procházení seznamu hodnot
        while cyklus - opakuj cyklus dokud platí podmínka

    While cyklus

        while cyklus je založen na podmínce, která se vždy na začátku cyklu testuje a pokud je splněna vykoná se zadaný blok instrukcí

    while podmínka:
        blok instrukcí

    Zajímavost
        Lze dokázat, že nelze sestrojit program, který by rozhodl, zda jiný program skončí či nikoliv.
        Člověk může dokázat, že daný while cyklus skončí
        Pokud důkaz chybí, není jisté, zda program s while cyklem skončí

            n = int(input())
            while n > 1:
              if n % 2 == 0:
                n = n // 2
              else:
                n = 3 * n + 1
"""

# n = int(input())
n = 12

while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1