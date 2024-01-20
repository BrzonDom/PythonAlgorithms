"""
Načtení 2D pole ze souboru

    Načtení matice uložené v souboru. Na každém řádku v souboru je uložen jeden řádek matice. Čísla jsou oddělena mezerou.
    Vstupní soubor (matice.txt)

        1 2 3
        4 0 5
        7 -1 2

    Soubor matice.txt musí být “viditelný” pro váš skript (pokud ne, je třeba zadat absolutní cestu k souboru).

        pole=[]
        f=open('matice.txt','rt')
        for line in f:
            pole.append(list(map(int, line.split())))
        f.close()
        print(pole)

    Program vypíše

        [[1,2,3],[4,0,5],[7,-1,2]]
"""

file_name = "matice"
file_path = "data\\" + file_name + ".txt"

Mat = []
file = open(file_path, 'rt')

# line = list(map(int, str_line.split()))

for line in file:
    Mat.append(list(map(int, line.split())))
file.close()

print(Mat)

