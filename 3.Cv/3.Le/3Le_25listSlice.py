"""
List slices

    a[i:j] vrací pole od pozice i do pozice j (kromě j)
    a[i:] pole od pozice i do konce
    a[:j] pole od začátku do pozice j (kromě j)
    a[:] kopie pole

    Výsledek řezu pole je pole
    Rezy polí fungují podobně jako u řetězců

"""

a = [1, 0, 3, "a", "!", 12, 0]

print(a[3:])
print(a[:])
print(a[:-3])
print(a[3:-3])
print(a[3:4])
print(a[2:5])
print(a[1:-1])
print(a[4:4])
