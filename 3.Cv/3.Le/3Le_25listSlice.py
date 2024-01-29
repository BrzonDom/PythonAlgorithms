"""
List slices

    a[i:j] vrací pole od pozice i do pozice j (kromě j)
    a[i:] pole od pozice i do konce
    a[:j] pole od začátku do pozice j (kromě j)
    a[:] kopie pole

    Výsledek řezu pole je pole
    Rezy polí fungují podobně jako u řetězců

"""

# a = [1, 0, 3, "a", "!", 12, 0]
#
# print(a[3:])
# print(a[:])
# print(a[:-3])
# print(a[3:-3])
# print(a[3:4])
# print(a[2:5])
# print(a[1:-1])
# print(a[4:4])

# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"List: {list}\n")

print(f"\tlist[3 :   ] = {list[3:]}")
print(f"\tlist[  :   ] = {list[:]}")
print(f"\tlist[  : -3] = {list[:-3]}")
print(f"\tlist[3 : -3] = {list[3:-3]}")
print(f"\tlist[3 :  4] = {list[3:4]}")
print(f"\tlist[2 :  5] = {list[2:5]}")
print(f"\tlist[1 : -1] = {list[1:-1]}")
print(f"\tlist[4 :  4] = {list[4:4]}")


