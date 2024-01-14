"""
Úkol 2 - Python jako kalkulačka

    Zjistěte kolik je:
        14 % 6
        14 % -6
        14 % 2.5
        14 // 6
        14 / 6
        int(14 / 6)
        14.0 // 6.0
        14 // -6
        int(14 / -6)
        float(14 // -6)
        2 ** 2 ** 2 ** 2

    Přidejte závorky, aby platilo (řešení ověřte v Pythonu):
        10 - 3 + 7 je 0
        12 + 3 * 2 je 30
        10 - 3 % 3 ** 10 je 1
        2 ** 2 ** 2 ** 2 je 256 - najděte alespoň dvě řešení
"""

print("14 % 6", end=" = ")
print(14 % 6)
print("14 % -6", end=" = ")
print(14 % -6)
print("14 % 2.5", end=" = ")
print(14 % 2.5)
print("14 // 6", end=" = ")
print(14 // 6)
print("14 / 6", end=" = ")
print(14 / 6)
print("int(14 / 6)", end=" = ")
print(int(14 / 6))
print("14.0 // 6.0", end=" = ")
print(14.0 // 6.0)
print("14 // -6", end=" = ")
print(14 // -6)
print("int(14 / -6)", end=" = ")
print(int(14 / -6))
print("float(14 // -6)", end=" = ")
print(float(14 // -6))
print("2 ** 2 ** 2 ** 2", end=" = ")
print(2 ** 2 ** 2 ** 2)

print()
# 10 - 3 + 7 je 0
print("10 - (3 + 7)", end=" = ")
print(10 - (3 + 7))
# 12 + 3 * 2 je 30
print("(12 + 3) * 2", end=" = ")
print((12 + 3) * 2)
# 10 - 3 % 3 ** 10 je 1
print("10 - 3 % 3 ** 10", end=" = ")
print(((10 - 3) % 3) ** 10)
# 2 ** 2 ** 2 ** 2 je 256
print("2 ** 2 ** 2 ** 2", end=" = ")
print((2 ** 2) ** 2 ** 2)


