"""
Výpočet Fibonacciho posloupnosti

    Napište rekurzivní výpočet Fibonacciho posloupnosti. Pro tuto posloupnost platí:

        F_n = F_n−1 + F_n−2

    První členy posloupnosti jsou

        F_0 = 0 a F_1 = 1.

"""
def fibRec(n):
   if n <= 1:
       # print(f"F({n}) = {n}")
       return n
   else:
       # print(f"F({n}) = F({n-1}) + F({n-2})")
       return(fibRec(n-1) + fibRec(n-2))

print("Fibonacci sequence:")

n = 8

Fib_sol = [[0, 0], [1, 1]]
Fib_list = [n]
Fib_len = len(Fib_list)

# for num in range(Fib_len):
#     if Fib_list[num] > 1:
#         Fib_list.append((Fib_list[num] - 2))
#         Fib_list[num] -= 1
#         Fib_len = len(Fib_list)
#     else:
#         continue


num = 0
while num < Fib_len:
    if Fib_list[num] > 1:
        Fib_list.append((Fib_list[num] - 2))
        Fib_list[num] -= 1
        Fib_len = len(Fib_list)
        num = 0
    else:
        num += 1

Fib_num = 0
for num in Fib_list:
    Fib_num += num

print(f"\tF({n}) = {Fib_num}")

print()

print("Fibonacci sequence function:")
print(f"\tF({n}) = {fibRec(n)}")



