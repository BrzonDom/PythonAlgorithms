"""
Největší společný dělitel

    Napište funkce gcd1(a,b) a gcd2(a,b), které vrátí největšího společného dělitele čísel a & b.

    Funkce gcd1 bude počítat největšího společného dělitele čísel a & b takto:

        Dokud a není rovno b
            Je-li a větší než b
                a = a-b
            jinak
                b = b-a

        a i b jsou největší společný dělitel původních čísel

    Funkce gcd2 bude počítat největšího společného dělitele čísel následovně:

        Dokud b není rovno nule
            t = b
            b = a mod b
            a = t
        a je největší společný dělitel původních čísel

    Zjistěte kolik kroků potřebuje gcd1 a gcd2 pro spočtení největšího společného dělitele 6997193,18992381 a dvojice 361,18992381
"""

def GCD1(num1, num2):

    """
        Dokud a není rovno b
            Je-li a větší než b
                a = a-b
            jinak
                b = b-a

        a i b jsou největší společný dělitel původních čísel
    """

    # if num1 <= num2:
    #     a = num1
    #     b = num2
    # else:
    #     a = num2
    #     b = num1

    a = num1
    b = num2

    steps = 0

    while a != b:
        steps += 1

        if a > b:
            a -= b
        else:
            b -= a

    print(f"GCD.1: ({num1},{num2}) = {a}\n\tSteps: {steps}\n")

    return a


def GCD2(num1, num2):

    """
        Dokud b není rovno nule
            t = b
            b = a mod b
            a = t
        a je největší společný dělitel původních čísel
    """

    a = num1
    b = num2

    steps = 0

    while b != 0:
        steps += 1

        t = b
        b = a % b
        a = t

    print(f"GCD.2: ({num1},{num2}) = {a}\n\tSteps: {steps}\n")

    return a


# a = 56
# b = 8
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a

GCD1(6997193,18992381)
GCD2(6997193,18992381)

GCD1(361,18992381)
GCD2(361,18992381)

