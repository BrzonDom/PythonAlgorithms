"""
While cykl

    Napište program, který udělá to samé co opakování for cyklů pomocí while cyklu:
        - vytiskněte čísla 10 až 500 po deseti
        - vytiskněte čísla -20 až -600 po dvaceti
"""

num = 10
add = 10

while num <= 500:
    print(num)
    num += add

print()

num = -20
add = -20

while num >= -600:
    print(num)
    num += add