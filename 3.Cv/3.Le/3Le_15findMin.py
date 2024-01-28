



numbers = [1, 6, 1, -1, 0, -1]

print(f"List of numbers: {numbers}\n")

index = []

if numbers:
    min = numbers[0]

    for n, num in enumerate(numbers):
        if num < min:
            min = num
            index = []
            index.append(n)
        elif num == min:
            index.append(n)


    print(f"Minimum: {min}")
    print(f"Found at index: ", end="")
    for i in index:
        print(i, end=" ")
