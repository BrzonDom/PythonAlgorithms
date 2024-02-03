"""
Těžká varianta

    Napište program text_numbers.py, který převádí čísla mezi slovní a číselnou reprezentací.

        Vstup: řetězec ze standardního vstupu

            Tento řetězec buď obsahuje číslo v desítkové soustavě nebo číslo zapsané anglicky slovy, např.

            twohundredfiftyseventhousandthreehundredseventyfive

        Výstup: řetězec na standardní výstup

            tento řetězec obsahuje vstup převedený do opačného zápisu, tj. text na číslo, a číslo na text.
            pokud výstup není ani číslo, ani platný slovní popis, pak je výstup ERROR

    Všechna čísla jsou pouze celá čísla v rozsahu 1 až 999.999.
    Pro textovou reprezentaci čísel použijte pouze následující spojení:
        one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand.
    Vypisujte i úvodní jedničku, tj. pro vstup 1000 vypište onethousand, podobně pro 120 se očekává výstup onehundredtwenty

    Poznámka
        Snažte se napsat program s využitím pole, nebo asociativního pole na co nejmenší počet řádek.

"""

import copy


def toStr(numb):

    numStr = ""

    exp = 100000
    if exp < numb:
        rest = numb % exp
        base = (numb - rest) // exp

        numb = copy.deepcopy(rest)

        print(f"{wrd_dict[base]}hundered", end="")
        numStr += f"{wrd_dict[base]}hundered"

    exp = 1000
    if exp < numb:
        rest = numb % exp
        base = (numb - rest) // exp

        numb = copy.deepcopy(rest)

        if base in wrd_dict:
            print(f"{wrd_dict[base]}thousand")
            numStr += f"{wrd_dict[base]}thousand"

        else:
            rest = base % 10
            baseTh = (base - rest)

            print(f"{wrd_dict[baseTh]}{wrd_dict[rest]}thousand", end="")
            numStr += f"{wrd_dict[baseTh]}{wrd_dict[rest]}thousand"

    exp = 100
    if exp < numb:
        rest = numb % exp
        base = (numb - rest) // exp

        numb = copy.deepcopy(rest)

        print(f"{wrd_dict[base]}hundered", end="")
        numStr += f"{wrd_dict[base]}hundered"

        if rest in wrd_dict:
            print(f"{wrd_dict[rest]}")
            numStr += f"{wrd_dict[rest]}"

        else:
            rest = numb % 10
            base = (numb - rest)

            print(f"{wrd_dict[base]}{wrd_dict[rest]}")
            numStr += f"{wrd_dict[base]}{wrd_dict[rest]}"

    return numStr


wrd_dict = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eighty",
    90 : "ninety",
    100 : "hundred",
    1000 : "thousand"
}


num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
             "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

one_num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen_num_words = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ty_num_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
dec_num_words = ["hundred", "thousand"]

numb = 143

numStr = str(numb)


wrd_lst = []

print(f"Number: {numb}")
print()

exp = 100000
if exp < numb:
    rest = numb % exp
    base = (numb - rest) // exp

    print(f"{wrd_dict[base]}hundered", end="")
    numb = copy.deepcopy(rest)

exp = 1000
if exp < numb:
    rest = numb % exp
    base = (numb - rest) // exp

    numb = copy.deepcopy(rest)

    if base in wrd_dict:
        print(f"{wrd_dict[base]}thousand")

    else:
        rest = base % 10
        baseTh = (base - rest)
        print(f"{wrd_dict[baseTh]}{wrd_dict[rest]}thousand", end="")

exp = 100
if exp < numb:
    rest = numb % exp
    base = (numb - rest) // exp

    numb = copy.deepcopy(rest)
    print(f"{wrd_dict[base]}hundered", end="")

    if rest in wrd_dict:
        print(f"{wrd_dict[rest]}")

    else:
        rest = numb % 10
        base = (numb - rest)

        print(f"{wrd_dict[base]}{wrd_dict[rest]}", end="")

