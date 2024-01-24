"""
Lehká varianta

    Napište program two_same.py, který načte dvě řádky pole celých čísel ze standardního vstupu a v nich najde nejdelší podposloupnost, která se vyskytuje v první řádce i v druhé řádce

    Vstup:
        Dvě řádky standardního vstupu, každá obsahující posloupnost celých čísel oddělených mezerou
        Pole na vstupu obsahuje vždy alespoň jedno číslo, jednotlivé řádky mohou obsahovat každá jiný počet čísel

    Úkol

        Program najde v zadaných polích dvě nejdelší souvislé podposloupnosti čísel, které jsou shodné v první posloupnosti i v druhé posloupnosti
        Podposloupnosti jsou shodné, když x-tý prvek první podposloupnosti se rovná x-tému prvku druhé podposloupnosti pro všechna x od prvního prvku až do posledního prvku podposloupností
        Můžete předpokládat, že v polích je jenom jedna dvojice nejdelších shodných posloupností
        Podposloupnost i posloupnost může mít i jen jeden prvek
        Vždy existuje alespoň dvojice dvou shodných čísel z první a druhé posloupnosti, tedy dvě podposloupnosti o jednom čísle

    Výstup

        program vytiskne tři čísla: délku nalezených podposloupností, index prvního prvku v první posloupnosti a index prvního prvku v druhé posloupnosti
            Indexy prvních prvků počítáme jako indexy v zadaných polích od 0
            Délka je počet prvků posloupnosti
        Tedy posloupnosti 3 1 2 4 5 a 3 4 1 2 4 4 5 obsahují oběstejnou podposloupnost 1 2 4 délky 3 od pozice 1 (první posloupnost) a od pozice 2 (druhá posloupnost).

    Program v souboru two_same.py odevzdejte pomocí odevzdávacího systému (úloha HW04).

"""

"""
Příklady:
    Vstup:
        1 2 3 3 3 3 3 3 3 3 5 6
        3 3 3 1 3 3 3 3 3 3 3 3
    Výstup:
        8 2 4
    
    Vstup:
        10
        1 2 3 10 3 2 1
    Výstup:
        1 0 3
        
    Vstup:
        1 2 3 4
        1 2 3 4
    Výstup:
        4 0 0
        

"""

str_seq11 = "1 2 3 3 3 3 3 3 3 3 5 6"
str_seq12 = "3 3 3 1 3 3 3 3 3 3 3 3"

seq11 = [int(num) for num in list(str_seq11.split(" "))]
seq12 = [int(num) for num in list(str_seq12.split(" "))]

len_seq11 = len(seq11)
len_seq12 = len(seq12)

LCS_Mat = [[0 for i in range(len_seq11+1)] for j in range(len_seq12+1)]

for row in LCS_Mat:
    print(row)

# print(LCS_Mat)

result = 0
res_index = []


for i in range(len_seq11+1):
    for j in range(len_seq12+1):
        if (i == 0 or j == 0):
            LCS_Mat[i][j] = 0
        elif (seq11[i-1] == seq12[j-1]):
            LCS_Mat[i][j] = LCS_Mat[i-1][j-1] + 1
            if LCS_Mat[i][j] > result:
                res_index = [i, j]
            result = max(result, LCS_Mat[i][j])
        else:
            LCS_Mat[i][j] = 0

print()

for i in range(len_seq11+1):
    for j in range(len_seq12+1):
        print(LCS_Mat[i][j], end=" ")
    print()

print()
print(result)
res_index[0] -= result
res_index[1] -= result
print(res_index)

print()
print(f"Sequence lenght: {result}")
print(f"\t\tStart index: {res_index[0]}\n\t\tEnd index:   {res_index[1]}")