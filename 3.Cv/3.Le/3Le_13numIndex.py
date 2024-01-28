


numbers = [0, 1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10]

searNum = 3

print(f"Number to be found: {searNum}")
print(f"List of numbers: {numbers}")
print()

index = []

for n, num in enumerate(numbers):
    # print(f"{n}. {num}")
    if num == searNum:
        index.append(n)
        # print(f"Num. {searNum} found at index", end=" ")

if index:
    print(f"Num. {searNum} found at index", end=" ")
    for i in index:
        print(i, end=" ")

elif not index:
    print(f"Num. {searNum} not found")


