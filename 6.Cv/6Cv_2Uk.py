"""
Prohození řádků matice

    Napište program, který načte matici a následně permutaci, která definuje prohození řádků matice. Na výstup program vytiskne matici s řádky prohozenými podle zadané permutace.

"""

matrix = []
print("Zadejte matici řádek po řádku. Když skončíte, zadejte 'end'.")
while True:
    row = input()
    if row == 'end':
        break
    matrix.append(list(map(int, row.split())))

print(matrix)

mat_list = [[[-1, -2, 3], [-3, 5, 6], [7, 8, 9]],
            [[-3, 5, 6], [-1, -2, 3], [7, 8, 9]],
            [[-5, -4, -4], [10, -3, 5], [-9, 6, -2]]]