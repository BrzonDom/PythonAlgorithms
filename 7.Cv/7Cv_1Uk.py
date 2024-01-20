"""
Binomický koeficient

    Napište funkci binomial(k,n), která počítá hodnotu (n | k)

    Můžete využít vztah
            (n | k) = (n−1 | k) + (n−1 | k−1)

    Počáteční podmínky
            (n | 0) = (n | n) = 1 a (n | 1) = (n | n−1) = n

"""

def fact(n):

    fN = 1

    for i in range(n):
        fN *= (i+1)
    return fN

def binomial(k, n):

    if (n >= k >= 0):
        return (fact(n))/(fact(k) * fact(n-k))
    else:
        return 0


n = 3
fN = 1

# print(f"Factorial of {n}:")
print("Factorial:")

print(f"\t!n = !{n} = ", end="")
for i in range(n):
    fN *= (i+1)

    if i != n-1:
        print(f"{i+1}", end=" * ")
    else:
        # print(f"{i + 1} = {fN}")
        print(f"{i+1}", end=" = ")

print(f"{fN}")
print()


print("Binomial coefficient:")

n = 6
k = 2

# print(f"/ {n} \\", end=" ")
# print("|   |  = ")
# print(f"\\ {k} /")

print(f"\t({n} | {k})", end=" = ")
print(f"!{n} / !{k} * !({n} - {k})", end=" = ")
print(f"!{n} / !{k} * !{n-k}", end=" =\n\t\t= ")
print(f"{fact(n)} / {fact(k)} * {fact(n-k)}", end=" = ")
print(f"{fact(n)} / {(fact(k)) * fact(n-k)}", end=" = ")
print(f"{fact(n)/((fact(k)) * fact(n-k))}")
print()
