"""
Cykly

Základní druhy cyklů

    for cyklus - procházení seznamu hodnot
    while cyklus - opakuj cyklus dokud platí podmínka - příští týden

For cyklus

    for cyklus standardně prochází zadaný seznam hodnot
    for cyklus je založen na proměnné, která prochází seznam hodnot a pro každou hodnotu ze seznamu provede blok instrukcí

        for proměnná in seznam:
          blok instrukcí

        for k in range(1, 20, 1):
            print(k)

        for i in "abcd":
          print(i)

        for i in (1, 10, 2, 8):
          print(i)


    Pro standardní procházení nějakého rozmezí je kontrukce range(start, cíl, krok), případně jednodušší verze range(cíl), kdy start je automaticky 0 a krok je nastaven na 1, nebo range(start, cíl), kdy krok je roven 1.
    Lze vytvořit i for cyklus, který má dynamicky měnící se seznam hodnot, případně vrací nekonečně krát stejné/rozdílné hodnoty. V tomto případě se pak jedná spíše o while cyklus a vám doporučujeme vzhledem k přehlednosti implementovat takový program jako while cyklus.
    POZOR: pokud měníte proměnnou cyklu v těle cyklu, nemá to vliv na její hodnotu v dalším cyklu, tedy:

        for i in range(10):
          print(i)
          i = i -1

    změna i v tomto případě, nemá vliv na provádění cyklu.

    Výsledkem tohoto cyklu jsou mocniny dvojky:

        for i in range(10):
          i = 2**i
          print(i)

"""

for k in range(1, 20, 1):
    print(k, end=" ")
print()

for i in "abcd":
    print(i, end=" ")
print()

for i in (1, 10, 2, 8):
    print(i, end=" ")
print()

for i in range(10):
  i = 2**i
  print(i, end=" ")