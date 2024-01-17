"""
Součet třetích mocnin, test odevzdávacího systému

    Stáhněte si k sobě program soucet.py

        a=int(input())
        k=int(input())

        sum=0

        for i in range(1,a+1,1):
            sum+=i**k

        print(sum)

    Přejmenujte program na cubic_sum.py a upravte jej tak, aby počítal součet třetích mocnin
        Sum from k=0 to n of k^3

    Dále upravte program tak, aby zkontroloval, zda se součet třetích mocnin rovná
        Sum from k=0 to n of k^3 == (n(n+1)/2)^2

    Program vytiskne na jednu řádku součet třetích mocnin, na další řádku vytiskne výsledek podle vzorečku
    Vytištěné výsledky musí být celá čísla.
    Program odevzdejte odevzdávacím systémem (úloha HW00).
"""

# a=int(input())
# k=int(input())
#
# sum=0
#
# for i in range(1,a+1,1):
#     sum+=i**k
#
# print(sum)


# n = int(input())
# add = 0
#
# for i in range(n+1):
#     add += (i**3)
#
# print(add)
# vzor = int(((n*(n+1))/2)**2)
# print(vzor)


import sys

n = int(sys.argv[1])
add = 0

for i in range(n+1):
    add += (i**3)

vzor = int(((n*(n+1))/2)**2)

if add == vzor: print("ANO")
else: print("NE")