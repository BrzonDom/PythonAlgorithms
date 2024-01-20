"""
Rekurze

    Při rekurzivním volání volá funkce samu sebe. Aby nedošlo k nekonečné smyčce, musí toho volání obsahovat ukončovací podmínku. Obecně lze rekurzi zapsat

        def funkce(promenna):
           if not (ukoncovaci podminka):
              funkce(zmenena_promenna)

    Pomocí rekurze můžeme například implementovat for cyklus:

        def recursivePrint(index, array):
            if (index < len(array) ):
                print(array[index], end=' ' );
                recursivePrint(index+1, array)
                print(array[index], end=' ' );

        a = []
        for i in range(10):
            a.append(i*i)

        print("List je",a)
        recursivePrint(0, a);

"""


def recursivePrint(index, array):
    if (index < len(array)):
        print(array[index], end=' ');
        recursivePrint(index + 1, array)
        print(array[index], end=' ');


a = []
for i in range(10):
    a.append(i * i)

print("List je", a)
print()

recursivePrint(0, a);