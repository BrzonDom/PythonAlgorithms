


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

searNum = 0

print(f"Number to be found: {searNum}")
print(f"List of numbers: {numbers}")
print()

index = -1

for n, num in enumerate(numbers):
    # print(f"{n}. {num}")
    if num == searNum:
        index = n
        print(f"Num. {searNum} found at index {index}")

if index == -1:
    print(f"Num. {searNum} not found")


