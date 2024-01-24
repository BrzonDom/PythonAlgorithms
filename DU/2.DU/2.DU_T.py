"""
Napište program subtraction.py, který od sebe odečte dvě reálná čísla zadané v binární číselné soustavě

Vstup:
    dvě řádky standardního vstupu, každá řádka obsahuje desetinné číslo v binární číselné soustavě ve tvaru 1.0101e-101

Výstup:
    rozdíl čísel v binární soustavě nebo ERROR pokud nebyly vstupy zadané korektně.

Řešení spočtěte přesně, nepoužívejte převod na reálné číslo v Pythonu, které může provést zaokrouhlení.

Správný formát desetinného čísla:
    - nenulové číslo začíná znaky '1.' (nebo záporné číslo znaky '-1.'), po kterých může následovat desetinná část čísla složená ze znaků '0' a '1', dále může následovat znak 'e' po kterém může následovat znak '-' a dále musí následovat celé číslo v binární formě reprezentující exponent.
    - nulové číslo je reprezentováno pouze znakem '0'

Řešení vypište ve stejném tvaru, jake je vstupní tvar desetinného čísla. Navíc nevypisujte zbytečné 0 před znakem “e”, případně na konci čísla, kde se “e” nevyskytuje:
    špatně   1.010e100
    správně  1.01e100
"""

"""
Příklady:
    Vstup:
        1.01e11
        1.01e11
    Výstup:
        0
    
    Vstup:
        1.1101e-1011
        1.1
    Výstup:
       -1.011111111100011
        
    Vstup:
        1.1101
        1.101e-1
    Výstup:
        1.
        
    Vstup:
        -1.1101e11
        1.101e-1
    Výstup:
        -1.1110101e11 
"""

def binNumSort(inBinNum):
    BinNum = ["","",""]

    if inBinNum[0] == "-":
        BinNum[0] = "-"
        inBinNum = inBinNum[1:]

    BinNum[1] = inBinNum.split(".")[0]
    BinNum[2] = inBinNum.split(".")[1]

    if "e" in inBinNum:
        BinNum.append("")
        BinNum[3] = BinNum[2].split("e")[1]
        BinNum[2] = BinNum[2].split("e")[0]

    return BinNum

def binNumExp(BinNum):
    if len(BinNum) < 4:
        return BinNum
    else:
        exp = int(BinNum[3], 2)

        if exp > 0:
            for i in range(exp):
                BinNum[1] = BinNum[1] + BinNum[2][0]
                BinNum[2] = BinNum[2][1:]

                if len(BinNum[2]) < 1:
                    BinNum[2] = "0"
        else:
            for i in range(abs(exp)):
                BinNum[2] = BinNum[1][-1] + BinNum[2]
                BinNum[1] = BinNum[1][1:]

                if len(BinNum[1]) < 1:
                    BinNum[1] = "0"

        return BinNum


# binNum = [0, 0]
    # binNum[0] = input();
    # binNum[1] = input();

# inBinNum1 = input()
# inBinNum2 = input()

inBinNum1 = "-1.1101e-11"
inBinNum2 = "1.1101e11"

BinNum1 = binNumSort(inBinNum1)
BinNum2 = binNumSort(inBinNum2)

print(f"inBinNum1: {inBinNum1}")
print(f"\tWhole: {BinNum1[0]}{BinNum1[1]}")
print(f"\tFrac: {BinNum1[2]}")
if len(BinNum1) > 3:
    print(f"\tExpo: {BinNum1[3]}")


print()
print(f"inBinNum2: {inBinNum2}")
print(f"\tWhole: {BinNum2[0]}{BinNum2[1]}")
print(f"\tFrac: {BinNum2[2]}")
if len(BinNum2) > 3:
    print(f"\tExpo: {BinNum2[3]}")


print()

BinNum1 = binNumExp(BinNum1)
print(f"{BinNum1[0]}{BinNum1[1]}.{BinNum1[2]}")
BinNum2 = binNumExp(BinNum2)
print(f"{BinNum2[0]}{BinNum2[1]}.{BinNum2[2]}")

# print(f"{polNum1}{binNum1[0]}.{binNum1[1]}")
# print(f"{polNum2}{binNum2[0]}.{binNum2[1]}")
