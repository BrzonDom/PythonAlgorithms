"""
Funkce quit()

    Pokud není uvedeno jinak, program končí po vykonání posledního příkazu
    Někdy se hodní ukončit program dříve, např. při špatně zadaném vstupu.
    K tomu slouží funkce quit()

        if (spatny_vstup):
            quit()

    Dosud jsme se setkali s několika funkcemi:

        input() - načte řetězec ze standardního vstupu
        print( argumenty ) - tiskne řetězec na standardní výstup
        int( argument ) - převod na celé číslo
        float( argument ) - převod na reálné číslo
        str( argument ) - převod na řetězec
        quit() - ukončí běh programu

"""

In = input()

print(f"Raw input: {In}\n\tOf type: {type(In)}\n")

intIn = int(float(In))

if type(intIn) == int:
    print(f"int input: {intIn}\n\tOf type: {type(intIn)}\n")
else:
    print("Wrong type")
    quit()

fltIn = float(In)

if type(fltIn) == float:
    print(f"float input: {fltIn}\n\tOf type: {type(fltIn)}\n")
else:
    print("Wrong type")
    quit()

strIn = str(In)

if type(strIn) == str:
    print(f"str input: {strIn}\n\tOf type: {type(strIn)}")
else:
    print("Wrong type")
    quit()