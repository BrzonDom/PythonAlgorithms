"""
Dokonalá čísla

    Dokonalé číslo je takové číslo, které je součtem všech svých dělitelů (kromě sebe samotného samozřejmě).
    Například číslo 6 je dokonalé, neboť 6 = 1 + 2 + 3, kde 1,2,3 jsou dělitelé čísla 6.
    Napište program, který vypíše všechna dokonalá čísla od 1 do 10000.

"""

dokNum_list = []
dokNum_divList = []

for num in range(1, 500):
    # print(f"Num: {num}")

    div_list = []
    for div in range(1, num):
        if num % div == 0:
            div_list.append(div)
    # print(div_list)
    div_add = 0
    for div in div_list:
        div_add += div

    # print(f"div_add = {div_add}\n")

    if div_add == num:
        dokNum_list.append(num)
        dokNum_divList.append(div_list)

print(f"Dokonalé čísla: ", end="")
print(dokNum_list)
print("\n\t", end="")

for dokNum in range(len(dokNum_list)):
    for dokNum_div in dokNum_divList[dokNum]:
        if dokNum_div == dokNum_divList[dokNum][-1]:
            print(f"{dokNum_div} =", end=" ")
        else:
            print(f"{dokNum_div} +", end=" ")
    print(dokNum_list[dokNum], end="\n\t")




