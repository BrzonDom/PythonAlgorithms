"""
Funkce

    Při programování často potřebujeme vykonat určité operace opakovaně. K tomu se hodí tzv. funkce.

        Funkce je seskupení příkazů
        Vstupem funkce jsou argumenty (jsou nepovinné)
        Složitý problém se typicky rozdělí na jednodušší úkony, které se naprogramují do funkcí
        Takový kód je snáze udržovatelný/čitelný
        Funkce mohou obsahovat lokální proměnné, které “nejsou vidět” ve zbytku programu
        V Pythonu se funkce definují klíčovým slovem def a tělo funkce (vnitřní příkazy) jsou odsazeny

            def jmenoFunkce( parametry ):
               telo_funkce

    Maximum ze dvou čísel:

        def maximum(x,y):
            if x>y:
                return x
            else:
                return y

    klíčové slovo return vrací výsledek funkce. Příklad volání této funkce:

        max = maximum(2,0.5)
        print(max)

        # nebo rovnou muzeme predat jiné funkci
        a = 6
        b = 7
        print("Maximum z ",a," a ", b, " je ", maximum(a,b))

    Parametry jsou nepovinné. Funkci bez parametrů definmujeme s prázdnými závorkami

        def hello():
            print("Hello World!")


    V tomto případě funkce ani nevrací žádnou hodnotu (pouze vypíše řetězec), není tedy třeba volat return
    Volání funkce bez parametrů

    Funkce v Pythonu mohou vracet více parametrů
    Příklad: funkce vracející maximum ze dvou čísel, s informací o tom, jestli maximem je 1. nebo 2. argument

        def maximum2(x,y):
            if (x > y):
                return x, True
            else:
                return y, False

    Volání

        maxValue, info = maximum2(5,6)

        #zkusime predat printu:
        print("Maximum z 5,6 je ", maximum2(5,6))

"""


def hello():
    print("Hello World!")

def maximum(x, y):
    if x > y:
        return x
    else:
        return y

def maximumTrue(x,y):
    if (x > y):
        return x, True
    else:
        return y, False

hello()
print()

x = 2
y = 5

MaxNum = maximum(x, y)

print(f"From numbers {x} & {y}, {MaxNum} is the bigger one")

MaxNumTrue = maximumTrue(x, y)

if MaxNumTrue:
    print(f"{x} <= {y}")
else:
    print(f"{x} > {y}")