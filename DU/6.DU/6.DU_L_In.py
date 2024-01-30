"""
Lehká varianta

    Napište a odevzdejte program find_pic.py, který:
        načte vzor (matice 3×3) ze standardního vstupu,
        načte obraz (matice NxM) ze souboru a
        najde, kde se vzor vyskytuje uvnitř obrazu.
    Vstup
        Přes příkazovou řádku bude programu předána cesta k souboru s obrazem (použijte sys.argv[1])
            Soubor je matice celých kladných čísel.
            Předpokládejte, že matice je zadána korektně a že každá řádka obsahuje stejný počet celých čísel.
        Druhým vstupem je vzor zadaný ze standardního vstupu.
            Vzor, který bude program hledat, se skládá ze tří řádek čísel. Každá řádka obsahuje tři čísla 0 nebo 1. Příklad vzoru:

         1 0 1
         0 1 0
         1 0 1

    Úkol
        Vzor se v obraze vyskytuje právě jednou. Nalezněte, na které pozici se vzor v obraze vyskytuje.
        Vzor obsahuje pouze čísla 0 a 1:
            Číslo 0 znamená, že na tomto místě se v matici může vyskytovat libovolné číslo.
            Číslo 1 znamená, že na této pozici se vyskytuje stejné číslo, jako na ostatních pozicích čísla 1 ve vzoru.
        Vzor se celý musí nacházet uvnitř matice, např., nelze nalézt část vzoru na pravé straně a část vzoru na levé straně obrazu.
    Výstup
        Dvě celá čísla oddělená mezerou c r, kde c je číslo sloupce a r je číslo řádku levého horního rohu vzoru v matici.
            Pozn.: Indexy řádků i sloupců začínají od 0, první řádek v souboru je řádek číslo 0.

"""

"""
Příklady:

    Vstup:
        1 0 1
        0 1 0
        1 0 1

        1 2 1 2 3 
        1 1 2 3 1
        1 2 3 2 1
        1 1 1 1 1        
    Výstup:
        1 0

    Vstup:
        1 1 1
        1 0 1
        1 1 1

        1 4 1 2 3 3 3
        1 1 4 4 4 4 3
        1 2 3 4 4 4 4
        1 5 1 4 4 4 1
        4 4 4 3 4 4 1
        1 5 3 5 1 1 1
        4 4 4 4 4 4 4 
    Výstup:
        3 1

    Vstup:
        1 0 1
        0 0 0
        1 0 1

        1 4 1 2 3 3 3
        1 1 4 4 4 4 3
        1 2 3 4 4 4 4
        1 5 1 5 4 4 1
        4 4 4 3 4 4 1
        1 5 3 5 1 1 1
        4 4 3 4 4 4 4 
    Výstup:
        1 3
"""

file_list = ["PrL_1", "PrL_2", "PrL_3"]

file_name = file_list[0]
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt")

data = []
lineCnt = 0

for str_line in file:

    line = list(map(int, str_line.split()))
    print("\t", line)
    data.append(line)

file.close()
print()

fileIn_list = ["PrLIn_1", "PrLIn_2", "PrLIn_3"]

file_name = fileIn_list[0]
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt")

dataIn = []

for str_line in file:

    line = list(map(int, str_line.split()))
    print("\t", line)
    dataIn.append(line)

file.close()

