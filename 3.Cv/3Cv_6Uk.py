"""
Super-dokonalá čísla

    Super-dokonalá čísla jsou zobecněním dokonalých čísel.
    Číslo n je super-dokonalé, pokud platí f(f(n))=2n, kde f(n) je součet dělitelů čísla n od 1 do n (včetně n).

    Například pro číslo 4: dělitelé jsou 1,2 a 4, tedy f(4)=1+2+4=7. Dělitelé 7 jsou 1 a 7, tedy f(7)=1+7=8, což je 2×4.
    Číslo 4 je tedy super-dokonalé.

    Napište funkci soucet_delitelu, která spočte součet dělitelů čísla n, tedy funkci f(n).

    Funkci soucet_delitelu použijte v programu, který vypíše seznam super-dokonalých čísel od 1 do 10000.
"""

supDokNum_list = []
# supDokNum_divList = []

for num in range(1, 10001):
    print(f"Num: {num}")

    div_list = []
    for div in range(1, num+1):
        if num % div == 0:
            div_list.append(div)
    print(f"\t{div_list}")
    div_add = 0
    for div in div_list:
        div_add += div

    print(f"\tdiv_add = {div_add}\n")

    nDiv_add = 0
    nDiv_list = []

    for nDiv in range(1, div_add+1):
        if div_add % nDiv == 0:
            nDiv_list.append(nDiv)
            nDiv_add += nDiv

    print(f"\t{nDiv_list}")
    print(f"\tnDiv_add = {nDiv_add}\n")

    if nDiv_add == 2*num:
        supDokNum_list.append(num)


print("Super-dokonalá čísla: ", end="")
print(supDokNum_list)
