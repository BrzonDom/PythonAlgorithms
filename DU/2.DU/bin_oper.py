
binA = "101"
binB = "1110"

print("binA: ", binA)
print("binB: ", binB)
print()

intA = int(binA, 2)
intB = int(binB, 2)

print("\t", binA, " = ", int(binA, 2), " = ", intA)
print("\t", binB, " = ", int(binB, 2), " = ", intB)
print()


print("\t", intA, " = ", bin(intA), " = ", str(bin(intA))[2:])
print("\t", intB, " = ", bin(intB), " = ", str(bin(intB))[2:])
print()

binNumWhole = "1110"
binNumFrac = "101000100001"
Num = 0
FrNum = 0
Cnt = 0


for i in reversed(binNumWhole):
    if i == "1":
        Num += 2**(Cnt)
    Cnt += 1

print(Num)

Cnt = 1.0
for i in binNumFrac:
    if i == "1":
        FrNum += 1/2**(Cnt)
    Cnt += 1

print(FrNum)
print()

whNum1 = "110"
whNum2 = "1011"

print("whNum1: ", whNum1)
print("whNum2: ", whNum2)
print()

whNum3 = str(bin(int(whNum1, 2) + int(whNum2, 2)))

print(f"\twhNum3 = {whNum1} + {whNum2} = {whNum3}")

whNum3 = str(bin(int(whNum1, 2) - int(whNum2, 2)))
print(f"\twhNum3 = {whNum1} - {whNum2} = {whNum3}")
print()


frNum1 = "1101"
frNum2 = "11101001"

dif = len(frNum1) - len(frNum2)

if dif > 0:
    frNum2 += ("0" * dif)
else:
    frNum1 += ("0" * abs(dif))

print(f"frNum1: 0.{frNum1}")
print(f"frNum2: 0.{frNum2}")
print()

exp = max(len(frNum1), len(frNum2))

frNum3 = str(bin(int(frNum1, 2) - int(frNum2, 2)))
pol = False

if frNum3[0] == '-':
    pol = True
    frNum3 = frNum3[3:]
else:
    frNum3 = frNum3[2:]


for i in range(exp):
    if i == 0:
        frOfNum3 = frNum3[-1]
        frNum3 = frNum3[:-1]
    else:
        frOfNum3 = frNum3[-1] + frOfNum3
        frNum3 = frNum3[:-1]

        if len(frNum3) == 0:
            frNum3 = "0"

if pol:
    frNum3 = "-" + frNum3

print(f"frNum3: {frNum3}.{frOfNum3}")


# print(bin(int("1" + frNum1, 2) - int("1" + frNum2, 2)))

# print(bin(whNum3))

