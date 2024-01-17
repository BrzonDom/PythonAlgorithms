"""
Absolutní hodnota

    Napište funkci s jedním argumentem, která vrací absolutní hodnotu tohoto argumentu

"""
import math

def absVal(num):
    return abs(num)

def absValMin(num):
    if num < 0:
        num *= -1
        return num
    else:
        return num

def absValSqr(num):
    num *= num
    num = math.sqrt(num)
    return num

num_List = [6.62, -14.56, 9.99, -7.59, 10.2, -9.92, -12.82, -5.11, 7.66, -12.44]

for num in num_List:
    print(f"For num: {num}")
    print(f"\tAbsVal:    {absVal(num)}")
    print(f"\tAbsValMin: {absValMin(num)}")
    print(f"\tAbsValSqr: {absValSqr(num)}")
    print()

