
"""
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
"""

def my_findMin(Set):

    if len(Set) == 0:
        return -1

    index = []
    min = Set[0]

    for n, num in enumerate(Set):

        if num < min:
            min = num
            index = [n]

        elif num == min:
            index.append(n)

    print(f"Min: {min}\n\tIndex: ", end="")
    for i in index:
        print(i, end=" ")

    return num, index


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

print("\n")

min, index = my_findMin(numbers)

print("\n")

print(f"Minimum: {min}")
print(f"Found at index: ", end="")
for i in index:
    print(i, end=" ")