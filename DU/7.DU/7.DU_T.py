"""
Těžká varianta

    Napište program compose.py, který si ze standardního vstupu přečte sekvenci kladných čísel X a dvě čísla s1 a s2 a najde
        sekvenci čísel A z čísel X, jejíž součet je roven s1 a
        sekvenci čísel B z čísel X, která nejsou v A, a jejichž součet je roven s2.

    Vstup:

        První řádek obsahuje X jako sekvenci celých kladných čísel oddělených mezerou.
        Druhý řádek obsahuje s1 s2 ve formátu dvou celých kladných čísel oddělených mezerou.

    Úkol:

        Program rozdělí X
            na čísla, jejichž součet je roven s1 a
            na čísla, jenž ještě nebyla použita a jejichž součet je roven s2.

        Pro součty můžete využít každé číslo z X maximálně jednou. Pokud je v X některé číslo vícekrát, můžete pro součty použít každý jeho výskyt.
        Pokud by existovalo více řešení zadaného problému, vypište pouze jedno řešení. Je jedno které.
        Zadání nemusí mít řešení.

    Výstup:

        Pokud existuje řešení:
            Dvě řádky čísel oddělených mezerou a seřazených na každé řádce podle velikosti od největšího po nejmenší. Součet čísel na prvním řádku bude roven s1, součet čísel na druhém řádku bude roven s2.

        Pokud neexistuje řešení:
            Výstupem programu bude NEEXISTUJE

"""


def combination(numbers, amount):
    if amount == 0:
        """     Base case for amount 0      """
        return [[]]
    if not numbers:
        """     Base case for no numbers    """

        return []

    """     List of all combinations adding to amount   """
    result = []

    for i in range(len(numbers)):
        """     Loops through all numbers   """
        num = numbers[i]

        """     Remaining numbers, excluding current and previous numbers   """
        remNumbers = numbers[i + 1:]

        for comb in combination(remNumbers, amount - num):
            """     Recursively calls combination function      """

            result.append([num] + comb)

    return result


in_num_list = [[26, 41, 18, 1, 15, 21, 19, 11],
               [286, 946, 80, 195, 106, 51, 186, 150, 63, 45, 310, 91],
               [995, 1799, 59, 1, 20, 124, 306, 471, 186, 431, 400, 497, 485],
               [813, 809, 126, 281, 78, 302, 471, 255, 204, 98, 453, 4, 269],
               [1718, 2499, 440, 1196, 1478, 405, 874, 652, 217, 1488, 136, 1137, 407, 796, 1208, 411, 1602, 1498, 453, 1085, 1016, 596, 308, 931, 975, 1226, 1562]]

in_num = in_num_list[0]

numbers = in_num[2:]
amount = in_num[:2]

print(f"First Amount:  {amount[0]}")
print(f"Second Amount: {amount[1]}")
print(f"List of numbers: {numbers}")
print()
# result = []

result = combination(numbers, amount[0])
print(result)

if result:
    for num in result[0]:
        # print(num)
        numbers.remove(num)

    result = combination(numbers, amount[1])
    print(result)
