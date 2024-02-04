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


def shiftToWhole(inBinNum, shift):

    if not inBinNum[2]:
        inBinNum[1] += "0" * shift

    else:
        for _ in range(shift):

            # if len(inBinNum[2]) == 0:
            if not inBinNum[2]:
                inBinNum[1] += "0"

            else:
                inBinNum[1] = inBinNum[1] + inBinNum[2][0]
                inBinNum[2] = inBinNum[2][1:]

            # if not inBinNum[2]:
            #     inBinNum[2] = "0"

    return inBinNum


def shiftToFrac(inBinNum, shift):

    for _ in range(shift):

        # if len(inBinNum[1]) == 0:
        if not inBinNum[1]:
            inBinNum[1] = "0"

        inBinNum[2] = inBinNum[1][-1] + inBinNum[2]
        inBinNum[1] = inBinNum[1][:-1]

    return inBinNum


def binNumSort(inBinNum):

    BinNum = ["", "", ""]

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
            for _ in range(exp):

                # if len(BinNum[2]) == 0:
                if not BinNum[2]:
                    BinNum[2] = "0"

                BinNum[1] = BinNum[1] + BinNum[2][0]
                BinNum[2] = BinNum[2][1:]

                # if len(BinNum[2]) < 1:
                #     BinNum[2] = "0"
        else:
            for _ in range(abs(exp)):

                BinNum[2] = BinNum[1][-1] + BinNum[2]
                BinNum[1] = BinNum[1][1:]

                # if len(BinNum[1]) < 1:
                if not BinNum[1]:
                    BinNum[1] = "0"

        return [BinNum[0], BinNum[1], BinNum[2]]


"""
Examples:
    1.001e-101₂ = 0.00001001₂ = 0.03515625₀
    1.1101e-1011₂ = 0.000000000011101₂ = 0.000885009765625₀
"""

# binNum = [0, 0]
    # binNum[0] = input();
    # binNum[1] = input();

# inBinNum1 = input()
# inBinNum2 = input()

in_binNum_lst = [["1.01e11", "1.01e11"],
                 ["1.1101e-1011", "1.1"],
                 ["1.1101", "1.101e-1"],
                 ["-1.1101e11", "1.101e-1"],
                 ["1.11011e1101", "1.001e-101"],
                 ["1.11011e", "1.001e-101"],
                 ["1.01e11", "1.1101"],
                 ["1.0111010010101e-110", "1.01110101001101e110"]]

inOp = 0

in_binNum = in_binNum_lst[inOp]

inBinNum1 = in_binNum[0]
inBinNum2 = in_binNum[1]


print("Input:")
print(f"\t1.Num: {inBinNum1}")
print(f"\t2.Num: {inBinNum2}")
print()

strNum1 = binNumSort(inBinNum1)
strNum2 = binNumSort(inBinNum2)

print(f"inBinNum1: {inBinNum1}")
print(f"\tWhole: {strNum1[0]}{strNum1[1]}")
print(f"\tFrac: {strNum1[2]}")
if len(strNum1) > 3:
    print(f"\tExpo: {strNum1[3]}")

#TODO: Edge case for wrong input

print()
print(f"inBinNum2: {inBinNum2}")
print(f"\tWhole: {strNum2[0]}{strNum2[1]}")
print(f"\tFrac: {strNum2[2]}")
if len(strNum2) > 3:
    print(f"\tExpo: {strNum2[3]}")
print()

print("Frac. expo:")
strNum1 = binNumExp(strNum1)
print(f"\t\t{strNum1[0]}{strNum1[1]}.{strNum1[2]}")
strNum2 = binNumExp(strNum2)
print(f"\t\t{strNum2[0]}{strNum2[1]}.{strNum2[2]}")
print()

# print(f"{polNum1}{binNum1[0]}.{binNum1[1]}")
# print(f"{polNum2}{binNum2[0]}.{binNum2[1]}")

expShift = max(len(strNum1[2]), len(strNum2[2]))

if expShift:
    print(f"Expo. shift: {expShift}")

    difShift = len(strNum1[2]) - len(strNum2[2])

    strNum1 = shiftToWhole(strNum1, expShift)
    strNum2 = shiftToWhole(strNum2, expShift)

    print(f"\t\t{strNum1[0]}{strNum1[1]}.{strNum1[2]}")
    print(f"\t\t{strNum2[0]}{strNum2[1]}.{strNum2[2]}")
    print()

operNum1 = int(strNum1[1], 2)
if strNum1[0]:
    operNum1 *= -1

operNum2 = int(strNum2[1], 2)
if strNum2[0]:
    operNum2 *= -1

operNum = bin(operNum1 - operNum2)
# print(type(operNum))

finStrNum = ["", "", ""]

if operNum[0] == "-":
    finStrNum[0] = "-"
    finStrNum[1] = operNum[3:]
else:
    finStrNum[1] = operNum[2:]

# print(operNum)
print("Bin subtr.:")
print(f"\t{finStrNum[0]}{finStrNum[1]}")
print()

if expShift:
    print("Expo. shift:")
    finStrNum = shiftToFrac(finStrNum, expShift)
    print(f"\t{finStrNum[0]}{finStrNum[1]}.{finStrNum[2]}")
    print()


if finStrNum[2]:
    while finStrNum[2][-1] == "0":
        finStrNum[2] = finStrNum[2][:-1]

        if not finStrNum[2]:
            break

    print("Redund. 0 remov.:")
    print(f"\t{finStrNum[0]}{finStrNum[1]}.{finStrNum[2]}")
    print()


if len(finStrNum[1]) > 1:
    print("Expo. form: ")
    expTo = len(finStrNum[1]) - 1

    finStrNum = shiftToFrac(finStrNum, expTo)

    finStrNum.append(str(bin(expTo))[2:])

    print(f"\t{finStrNum[0]}{finStrNum[1]}.{finStrNum[2]}e{finStrNum[3]}")

elif finStrNum[1] == "0" and finStrNum[2]:
    print("Expo. form: ")

    expTo = finStrNum[2].index("0")

    finStrNum = shiftToWhole(finStrNum, expTo)

    finStrNum.append("-" + str(bin(expTo))[2:])

    print(f"\t{finStrNum[0]}{finStrNum[1]}.{finStrNum[2]}e{finStrNum[3]}")



if finStrNum[1] == "0":
    print(f"Final output number: 0")

else:
    print(f"Final output number: {finStrNum[0]}{finStrNum[1]}.", end="")

    if finStrNum[2]:
        print(f"{finStrNum[2]}", end="")

    if len(finStrNum) > 3:
        print(f"e{finStrNum[3]}")


