"""
For cyklus

    For cyklus

        for cyklus standardně prochází zadaný seznam hodnot
        for cyklus je založen na proměnné, která prochází seznam hodnot a pro každou hodnotu ze seznamu provede blok instrukcí

            for proměnná in seznam:
              blok instrukcí

            for i in "abcd":
              print(i)

            for i in (1, 10, 2, 8):
              print(i)

        Pro standardní procházení nějakého rozmezí:
            range(start, cíl, krok),
            range(cíl), kdy start je automaticky 0 a krok je nastaven na 1,
            range(start, cíl), kdy krok je 1.
        Lze vytvořit i for cyklus, který má dynamicky měnící se seznam hodnot, případně vrací nekonečně krát stejné/rozdílné hodnoty. V tomto případě se pak jedná spíše o while cyklus a vám doporučujeme vzhledem k přehlednosti implementovat takový program jako while cyklus.

    Instrukce break a continue

        Uvnitř bloku instrukcí mohou být příkazy break a continue.
        Příkaz break znamená, že se okamžitě ukončí vykonávání bloku instrukcí a ukončí se i cyklus, který tento blok instrukcí obsahuje.
        Příkaz continue znamená, že
            se ukončí provádění bloku instrukcí a provede se vyhodnocení podmínky (u while cyklu)
            se přejde na novou hodnotu (u for cyklu) a pokud je to možné pokračuje se v provádění bloku instrukcí.
        POZOR u vnořených cyklů nemají příkazy break/continue vliv na vnější cyklus.

            for i in "abcd":
              if i == "c":
                break
              print(i)

            for i in "abcd":
              if i == "c":
                continue
              print(i)

"""

print("Break:")

for i in "abcd":
    if i == "c":
        break
    print(i)

print()

print("Continue:")

for i in "abcd":
    if i == "c":
        continue
    print(i)