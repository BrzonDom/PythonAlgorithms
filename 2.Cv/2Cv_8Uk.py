"""
Výpočet třetí odmocniny přičítáním se zadanou přesností

    Upravte předchozí program tak, aby pracoval se zadanou přesností
    Program načte číslo y & n a nalezne třetí odmocninu z čísla y na n desetinných míst
    Upravte algoritmus, aby uměl spočítat i třetí odmocniny ze záporných čísel

"""

num = -400
acc = 5

odh = 1
odhNum = odh * odh * odh
add = 1

print(f"Finding root of number: {num}\n\t With {acc} decimal accuracy\n")

pol = 1
polStr = ""
if num < 0:
    num *= -1
    pol = -1
    polStr = "-"

for i in range(acc+1):
    while odhNum < num:
        odh += add
        odhNum = odh * odh * odh
    odh -= add
    odhNum = odh * odh * odh
    print(f"{i+1}. {polStr}{odh}^3 = {polStr}{odhNum}")
    add *= 0.1