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

# mat_list = []