"""
Lehká varianta

    V zadané množině čísel najděte číslo, které má největší společný dělitel s prvním zadaným číslem a tento největší společný dělitel vytiskněte.

    Vstup:

        první řádka obsahuje počet zadaných čísel
        ostatní řádky obsahují vždy jedno celé číslo.
    Výstup:

        největší společný dělitel s prvním číslem

    Program pro úlohu HW03 pojmenujte gcd_max.py
"""

"""
Příklady:
    Vstup:
        5
        21
        9
        8
        7
        6
    Výstup:
        7

    Vstup:
        12
        192779
        253
        263
        273
        283
        683
        693
        703
        713
        723
        733
        743
    Výstup:
        733

    Vstup:
        6
        3099
        6376
        8005
        4116505
        9980
        10000
    Výstup:
        1033
"""

# str_input = """        3099
#         6376
#         8005
#         4116505
#         9980
#         10000"""
#
# int_input = list(map(int, str_input.split()))
# print(int_input)

inNum_list = [[21, 9, 8, 7, 6],
              [192779, 253, 263, 273, 283, 683, 693, 703, 713, 723, 733, 743],
              [3099, 6376, 8005, 4116505, 9980, 10000]]

inNum = inNum_list[0]

print(f"Number input: {inNum}")