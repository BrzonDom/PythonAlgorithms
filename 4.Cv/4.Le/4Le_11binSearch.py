
def binSearch(numbers, tNum):

    L = 0
    R = len(numbers) - 1

    while L <= R:
        M = (L + R) // 2

        if numbers[M] == tNum:
            return M

        if numbers[M] > tNum:
            R = M - 1
        else:
            L = M + 1

    return -1

numbers = [-6, -4, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 9]

print(binSearch(numbers, 1))