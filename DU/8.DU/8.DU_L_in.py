"""
    Tématem úlohy je napsat program tile_easy.py, který vyplní hexagonální hrací desku zadanými kameny

    Úkolem je vyplnit hrací desku o velikosti 4×4 (4-řádky, každý řádek 4 pole). Všechna řešení jsou

    Vstup programu: argumenty příkazové řádky
        první argument: velikost hrací desky (jedno celé číslo) určující jak počet řádků tak i počet sloupců
        druhý argument: jméno vstupního souboru s hracími kameny (je zaručeno, že existuje, že obsahuje alespoň jeden kamen a obsahuje správně zadané kameny)
        třetí argument: jméno výstupního souboru
    Program nalezne kombinaci kamenů na hrací desce tak, aby každé políčko bylo vyplněno právě jedním kamenem
    V lehké variantě domácí úlohy je povolena pouze translace kamenů, tedy je zakázáno kameny otáčet
    Je možné použít všechny kameny, ale není to nutné. Každý kamen se ale použije nejvýše jednou.
    Pokud je nějaký kamen použit, musí se celý vejít do hrací desky, nesmí přečnívat přes hrací desku ani se nesmí překrývat s jiným kamenem
    Program do výstupního souboru vypíše:
        právě jedno řešení - libovolné ze všech existujících řešení
            Výstup programu se zapisuje do výstupního souboru takto:
                každý řádek obsahuje tři celá čísla ve tvaru 'p q i', kde (p,q) je celočíselná souřadnice na hrací desce a 'i' je index kamene, který tuto buňku obarvuje
                kameny jsou číslovány od jedničky podle pořadí ve vstupním souboru (kamen definován na první řádce bude barvit na 1, kamen na druhá řádce obarvuje hodnotou 2 atd..)
        NOSOLUTION, pokud žádné neexistuje
            pokud řešení neexistuje, obsahuje soubor pouze jednu řádku s textem 'NOSOLUTION'
    Program odevzdejte jako tile_easy.py do HW08
    Timeout je nastaven dostatečně, pokud by Váš program měl problémy s časovým omezením, kontaktujte nás na fóru předmětu.
    Jak bude hodnoceno:
        Vyřešení hrací desky o velikosti 3×3, počet kamenů 2 až 4 (0.4b)
        Vyřešení hrací desky o velikosti 4×4, počet kamenů 3 až 5 (0.4b)
        Vyřešení hrací desky o velikosti 5×5, počet kamenů 2 až 6 (0.4b)
        Správná detekce hrací desky bez řešení (0.3b)

    Nápověda a pomocný program

        Obtížnost této úlohy spočívá jednak v tom, jak najít vhodné poskládání kamenů, které zcela pokrývá hrací desku, a také v tom, jak pracovat s hexagonálním gridem
        Pro usnadnění práce na domácí úloze si stáhněte program base.py (na konci této stránky), který vám nabízí užitečné nástroje

"""

import base
import sys

    # nacteni vstupnich parametru z prikazove radky do promennych size, inputFile, outputFile
# size = int(sys.argv[1])
# board = base.Board(size)
# stones = base.loadStones(sys.argv[2])

# file_list = ["PrL_1", "PrL_2", "PrL_3"]
# file_name = file_list[0]

file_name = "PrL_1"
fileOpen = "data\\" + file_name + ".txt"
fileWrite = "data\\" + file_name + "_out.txt"

size = 3
board = base.Board(size)
stones = base.loadStones(fileOpen)

print(f"File: {file_name}.txt")

file = open(fileOpen, "r")
data = []

for str_line in file:

    line = list(map(int, str_line.split()))
    print("\t", line)
    data.append(line)

file.close()

stones = []

for st in range(len(data)):
    stones.append([])
    for stCo in range(0, len(data[st]),  2):
        # print(stCo, end=" ")
        stones[st].append([data[st][stCo], data[st][stCo+1]])
        # # print(data[st][stCo], end=" ")
    print(stones[st])




#     # program hledajici rozmísteni kamenu, ktery svuj vysledek zapisuje do board.board
#
#     # vytvoreni, ci otevreni vystupniho souboru do handleru f
# f = open(fileWrite, "w")
#
# # if reseni_exist:
# #     for p in board.board:
# #         for q in board.board[p]:
# #             f.write("{} {} {}\n".format(p, q, board.board[p][q]))
# # else:
# #     f.write("NOSOLUTION")
#
# f.close()