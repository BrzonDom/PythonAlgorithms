"""
Lehká varianta

    Napište program select.py, který si ze standardního vstupu přečte sekvenci kladných čísel X a číslo s a najde čísla v X, jejichž součet je roven s.

    Vstup:

        První řádek obsahuje celá kladná čísla oddělená mezerou. Tato čísla reprezentují množinu čísel X.
        Druhý řádek obsahuje jedno celé kladné číslo s.

    Úkol:

        Program nalezne čísla z X, jejichž součet je roven s.
        Pro součet můžete využít každé číslo z X maximálně jednou. Pokud je v X některé číslo vícekrát, můžete pro součet použít každý jeho výskyt.
        Pokud by existovalo více řešení zadaného problému, vypište pouze jedno řešení. Je jedno které.
        Můžete se spolehnout na to, že ze zadaného X lze s získat vždy.

    Výstup:

        Výstupem programu je výpis čísel z X, jejichž součet je roven s. Čísla jsou vypsána na jeden řádek od největšího k nejmenšímu. Čísla jsou oddělená mezerou.

    Nápověda:

        Projděte si přednášku 6) Rekurze a nechte se inspirovat problémem Mince.
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
        remNumbers = numbers[i+1:]

        for comb in combination(remNumbers, amount-num):
            """     Recursively calls combination function      """

            result.append([num] + comb)

    return result


in_num_list = [[23, 1, 6, 3, 10, 20, 15],
           [81, 15, 10, 51, 34, 51, 26, 15, 43],
           [78, 44, 34, 16, 18, 55, 25, 42]]

in_num = in_num_list[0]

numbers = in_num[1:]
amount = in_num[0]

print(f"Amount: {amount}")
print(f"List of numbers: {numbers}")
print()
# result = []

print(combination(numbers, amount))