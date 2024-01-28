"""
Mince

    Vstupem je hodnota a seznam mincí


    Hledáme nejmenší počet mincí (o známých hodnotách), které poskládají
    vstupní částku

"""

def solve (amount ,result ,coins):
    if amount == 0:
        return
    for i in range(len(coins)-1, -1, -1):
        c = coins[i]
        if c <= amount:
            num = amount // c
            amount %= c
            result.append([num, c])
            solve(amount, result, coins[:i] + coins[i:])
            break

result = []
solve (37, result, [1, 2, 5, 10])
for item in result: # item is [ numberOfCoin , coin ]
    number, coin = item
    print(coin, " CZK x ", number)