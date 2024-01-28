"""
Mince

    Vstupem je hodnota a seznam mincí, úkolem je určit všechny
    kombinace mincí, které dávají požadovanou hodnotu

    Mince: postup
        Rekurzivní řešení: skládáme částku amount z mincí [c_i, c_i+1, ... , c_n]

            Zkusíme minci c_i, snížíme částku na: amount - c_i, řešíme s mincemi [c_i, c_i+1, ... , c_n]

            Nebo: nepoužijeme c_i, řešíme úlohu amount s mincemi [c_i+1, c_i+2, ... , c_n]

"""

def allChanges (amount, coins, result, i):
    if amount == 0:
        for i in range(len(result)):
            if result[i] != 0:
                print(coins[i], "CZK x", result[i], end=" , ")
        print()
    else:
        if coins[i] <= amount:
            result[i] += 1
            allChanges(amount - coins[i], coins, result, i)
            result[i] -= 1
        if i < len(coins)-1:
            allChanges(amount, coins, result, i+1)

coins = [1,2,5,10]
s = [0] * len(coins)
allChanges(12, coins, s, 0)

