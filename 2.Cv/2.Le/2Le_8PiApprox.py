
def fact(n):
    res = 1

    for i in range(2, n+1):
        res *= i

    return res

def piApprox():
    s = 0
    kMax = 6

    for k in range(kMax):
        a = fact(4 *k) * (1103 + 26390 *k)
        b = (fact(k) **4) * (396 **(4 *k))
        s += a / b
        print(k, a / b)

    r = (2 *(2 **(0.5)) / 9801) *s
    return 1 / r

print("\nPi = ", piApprox())