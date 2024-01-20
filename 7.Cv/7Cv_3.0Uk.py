"""
Rychlejší výpočet Fibonacciho posloupnosti

    Předchozí řešení je pomalé pro výpočet větších n. Důvodem je, že při rekurzivním volání dochází často k opakovanému výpočtu stejných členů posloupnosti.

    Řešením je zapamatovat si již vypočítané hodnoty a ty použít:

        Funkce fib(n) si nejprve zjistí, jestli už je znám výsledek pro n

        Pokud ano, vrátí ho

        Pokud ne, vypočítá hodnotu posloupnosti pro n a uloží ho do seznamu známých hodnot

        Známé hodnoty lze ukládat např. v globálním poli hint[]

    Napište funkci fibFast(n) pro zrychlený výpočet Fibonacciho posloupnosti

        Porovnejte časy výpočtu fib(100) a fibFast(100)

        Jak byste lépe alokovali pole hint?

"""

def fibRec(n):
   if n <= 1:
       # print(f"F({n}) = {n}")
       return n
   else:
       # print(f"F({n}) = F({n-1}) + F({n-2})")
       return(fibRec(n-1) + fibRec(n-2))

fib_dic = {
    0 : 0,
    1 : 1
}

fib_num = 0
n = 6

print("Fibonacci sequence function:")
print(f"\tF({n}) = {fibRec(n)}")
print()

for num in range(1, n+1):
    if num < 2:
        fib_num += num
    else:
        if num in fib_dic:
            fib_num += fib_dic[num]
        else:
            fib_dic[num] = fib_dic[num-1] + fib_dic[num-2]



print("Fibonacci dictionary:")
for key in fib_dic:
    print(f"\tF({key}) = {fib_dic[key]}")
