"""
Vypočtěte třetí odmocninu kladného čísla y, zadaného jako vstup Vašeho programu následujícím postupem:

    - Přičítejte k proměnné v číslo 1 dokud je třetí mocnina této proměnné menší než y
    - Přičítejte k proměnné v číslo 0.1 dokud je třetí mocnina této proměnné menší než y
    - Přičítejte k proměnné v číslo 0.01 dokud je třetí mocnina této proměnné menší než y
    - Proměnná v obsahuje odmocninu čísla y s přesností na dvě desetinná čísla

"""

num = 400
odh = 1
odhNum = odh * odh * odh
add = 1

for i in range(3):
    while odhNum < num:
        odh += add
        odhNum = odh * odh * odh
    odh -= add
    odhNum = odh * odh * odh
    print(f"{i+1}. {odh}^3 = {odhNum}")
    add *= 0.1

