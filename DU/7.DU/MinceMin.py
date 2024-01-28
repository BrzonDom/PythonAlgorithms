
def change (amount, result, coins):
    if amount == 0:
        return

    for i in range(len(coins)-1, -1, -1):
        c = coins[i]
        if c <= amount:
            num = amount // c
            amount %= c
            result.append([num, c])
            change(amount, result, coins[:i] + coins[i:])
            break

result = []
amount = 37
coins = [1, 2, 5, 10]

change(amount, result, coins)

print(f"Amount: {amount}")
print("Coins: ", end="")
for coin in coins:
    print(f"({coin})", end=" ")
print("\n")

for item in result:
    number, coin = item
    print(f"\t{number:2} x ({coin})")
    # print(coin, " cz * ", number)