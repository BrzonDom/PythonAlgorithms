
def my_findMax(Set):

    if len(Set) == 0:
        return -1

    index_list = []
    index = 0
    Max = Set[0]

    for num in Set:

        if num > Max:
            Max = num
            index_list = [index]

        elif num == Max:
            index_list.append(index)

        index += 1

    print(f"Max: {Max}\n\tIndex: ", end="")
    for i in index_list:
        print(i, end=" ")

    return [num, index_list]


# def numIndex(numbers, num):
#



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


