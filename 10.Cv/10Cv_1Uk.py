"""
Reprezentace grafu

    Graf lze reprezentovat maticí sousednosti, seznamem hran nebo seznamem odchozích hran

    Budeme používat seznam odchozích hran.

    Pro graf na obrázku bude reprezentace vypadat takto:

    G je proměnná typu dictionary, indexujeme ji jménem (číslem) uzlu, hodnota je pole, které obsahuje seznam uzlů, které jsou dosažitelné

        G = {}
        G [0] = [1 ,2 ,5]
        G [1] = [0 ,2]
        G [2] = [0 ,1 ,3]
        G [3] = [2]
"""

G = {}
G[0] = [1, 2, 5]
G[1] = [0, 2]
G[2] = [0, 1, 3]
G[3] = [2]

print(G)

print("\n\t", end="")
for key in G:
    print(f"{key}: ", end="")
    for val in G[key]:
        if val == G[key][-1]:
            print(f"{val}")
        else:
            print(f"{val}", end=", ")
    print("\t", end="")
    # for

