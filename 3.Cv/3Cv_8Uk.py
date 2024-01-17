"""
Césarova šifra

    Napište program pro realizaci tzv. Césarovy šifry
    Vstup: dvě řádky
        1. řádka: textový řetězec (pouze písmena a mezery)
        2. řádka: číslo definující posunutí písmen v Césarově šifře

    Program na výstup vypíše vstupní řetězec zašifrovaný posunutím písmen o zadanou hodnotu
    Ascii hodnota znaku se získá funkcí ord('A'), opačně znak z celého čísla získáte funkcí chr(65)
    Je nutné posouvat velká písmena na velká písmena, malá písmena na malá písmena a mezeru ponechat jako mezeru

"""

print(f"a = {ord('a')}")
print(f"z = {ord('z')}")
print(f"' ' = {ord(' ')}")
print(f"A = {ord('A')}")
print(f"Z = {ord('Z')}")

org_string = "Hello World try to encode this"
enc_string = ""
shift = 6

# print()
# print("A")
# print(f"{chr(ord('A')+25)}")
# print()

# tstCh = 'Y'
# tstOrdCh = ord(tstCh) + 13
#
# if tstOrdCh > ord('Z'):
#     tstOrdCh -= 25
# print(chr(tstOrdCh))

for char in org_string:

    if 'A' <= char <= 'Z':
        # print("Big")
        ordChar = ord(char) + shift

        if ordChar > ord('Z'):
            ordChar -= 25

    elif 'a' <= char <= 'z':
        # print("small")
        ordChar = ord(char) + shift

        if ordChar > ord('z'):
            ordChar -= 25

    else:
        # print("space")
        ordChar = ord(char)

    enc_string += chr(ordChar)

        # print("small")

    # print(f"{char} = {ord(char)}")

print(f"\nShift: {shift}")

print("\nOriginal string: ", end="\n\t")
print(org_string)
print("Encoded string: ", end="\n\t")
print(enc_string)

