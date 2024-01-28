
def change(amount, coins, result, i):
    if amount == 0:
        for i in range(len(result)):
            if result[i] != 0:
                print(f"{result[i]:2} x ({coins[i]})", end = " ")
        print()
    else:
        if coins[i] <= amount:
            result[i] += 1
            change(amount - coins[i], coins, result, i)
            result[i] -= 1
        if i < len(coins) - 1:
            change(amount, coins, result, i+1)



coins = [1, 2, 5, 10]
amount = 12
res = [0] * len(coins)


print(f"Amount: {amount}")
print("Coins: ", end="")
for coin in coins:
    print(f"({coin})", end=" ")
print("\n")

change(amount, coins, res, 0)

