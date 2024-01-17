"""
Najdi a změň

    Napište funkci my_find(a,b), která v řetezci a hledá řetězec b (nepoužívejte vestavěnou funkci find).
    Pokud řetězec najde, vrátí index jeho prvního výskytu zleva.
    Pokud řetězec nenajde, vrátí -1.

    Napište funkci my_replace(a,b,c), která v řetězci a nahradí všechny výskyty řetězce b řetězcem c.
    Ve funkcích používejte pouze funkce
        len(s) - délka řetězce,
        s[i] - znak na pozici i,
        s[i:j] - podřetezec od i do j
        s[:j], s[i:] - podřetězec od počátku do j, resp. od i do konce.

"""

def my_find(Org, Sub):

    index = j = 0

    for i in range(len(Org)):

        if Org[i] == Sub[j]:
            j += 1

            if j == len(Sub):
                index = i - len(Sub) + 1
                break
        else:
            j = 0

    if index:
        print(f"Index: {index}")
        return index
    else:
        print("Substring not found!")
        return -1


def my_replace(Org, Sub, Rep):

    index = j = 0

    for i in range(len(Org)):

        if Org[i] == Sub[j]:
            j += 1

            if j == len(Sub):
                index = i - len(Sub) + 1
                break
        else:
            j = 0

    if not index:
        print("Substring not found!")
        return -1

    Edt = Org[:index] + Rep + Org[index + len(Sub):]
    print(f"Original str: {Org}")
    print(f"Edited str:   {Edt}")

    if index:
        print(f"Index: {index}")
        return index



Org_str = "HelloWorld, Test1Test2Test3, Obj.2 Obj.3 Obj.4, Another1, Another2, Another3"
Sub_str = "Obj.2 Obj.3 Obj.4"
Rep_str = "Item.1 Item.2 Item.3"
Edt_str = ""

print(f"Org_str: {Org_str}")
print(f"Sub_str: {Sub_str}")
print(f"Rep_str: {Rep_str}")

j = 0
index = 0

for i in range(len(Org_str)):

    if Org_str[i] == Sub_str[j]:
        j += 1

        if j == len(Sub_str):
            index = i - len(Sub_str) + 1
            break
    else:
        j = 0

i = 0
# for char in Org_str:
#     print(f"{i:02}. {char}")
#     i += 1


print(f"\n\nIndex: {index}")

index = j = 0

for i in range(len(Org_str)):

    if Org_str[i] == Sub_str[j]:
        j += 1

        if j == len(Sub_str):
            index = i - len(Sub_str) + 1
            break
    else:
        j = 0

for i in range(index):
    # print(f"{i:02}. {Org_str[i]}")
    Edt_str += Org_str[i]

print()
Edt_str += Rep_str

for i in range(index + len(Sub_str), len(Org_str)):
    # print(f"{i:02}. {Main_str[i]}")
    Edt_str += Org_str[i]


print()
print(f"\"{Org_str[:index]}\" + \"{Rep_str}\" + \"{Org_str[index + len(Sub_str):]}\"")
print()

print(f"Main_str: {Org_str}")
print(f"Edt_str:  {Edt_str}")

print("\n")

index_return = my_find(Org_str, Sub_str)
print(f"Returned index value: {index_return}")

print()

index_return = my_find(Org_str, "Lala")
print(f"Returned index value: {index_return}")

print()

index_return = my_replace(Org_str, Sub_str, Rep_str)
print(f"Returned index value: {index_return}")

print()

index_return = my_replace(Org_str, "Lala", Rep_str)
print(f"Returned index value: {index_return}")