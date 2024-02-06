"""
Narovnání

    Uvažujme pole, které může obsahovat jako prvky další pole, např.:

        a = [1, 2, [3, [4, 5], 6, [7]], [8, 9], 10]

    Napište funkci flatten, která vytvoří jedno pole, které bude obsahovat všechny prvky z pole a vložené do tohoto pole.
    Výsledkem funkce

        flatten(a) : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    K testu prvku, zda je pole (list), použijte funkci type:

        if type(x) is list:

"""
import copy


def flatten(listList):
    if len(listList) == 0:
        return listList

    if type(listList[0]) == list:
    # if isinstance(list_of_lists[0], list):

        return flatten(listList[0]) + flatten(listList[1:])

    return listList[:1] + flatten(listList[1:])


# def flat(listList):



a = [1, 2, [3, [4, 5], 6, [7]], [8, 9], 10]
a_flat = []

# row = len(a)
# print(row)

# for itm in a:
#     print(itm, end=", ")
# print("\n")


print(f"Original list: {a}")
print(f"Flatten list:  {flatten(a)}")
# print(flatten(a))