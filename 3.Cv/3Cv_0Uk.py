"""
Ramanujan Taxi

    Ramanujan (1887-1920) byl velmi zajímavý geniální indický matematik.
    Byl objeven prof. Hardym a pozván do Anglie. Zde onemocněl a když ho prof. Hardy
    navštívil v nemocnici, řekl mu, že za ním přijel taxíkem číslo XXXX. Ramanujan mu
    okamžitě odpověděl, že je to velmi zajímavé číslo, protože je to nejmenší číslo,
    které lze zapsat dvěma různými způsoby jako součet dvou krychlí (třetích mocnin přirozených čísel).

    Najděte čtyřciferné číslo taxíku XXXX.
"""

i = 1

while (i**3) < 10000:
    print(f"{i}^3 = {i*i*i}")
    last = i
    i += 1
#
# i = j = 1

# import itertools
#
# # Define the range of numbers
# numbers = range(1, 10)
#
# # Generate all combinations of 2 numbers
# combinations = list(itertools.combinations(numbers, 2))
#
# # Print the combinations
# for combination in combinations:
#     print(combination)
list_num = []
list_i_j = []
list_Ram = []


for i in range(1, last):
    for j in range(1, last):
        if 999 < (i**3 + j**3) < 10000:
            print(f"{i}^3 + {j}^3 = {i**3 + j**3}")

            if (i**3 + j**3) in list_num and [j, i] not in list_i_j:
                print(f"\nRamanujan Taxi number found\n{i}^3 + {j}^3 = {i**3 + j**3}\n")

                list_Ram.append([i, j, i**3 + j**3])

            list_num.append(i**3 + j**3)
            list_i_j.append([i, j])
        elif (j**3 + j**3) < 10000:
            break


print()
print(list_Ram)
min = list_Ram[0][2]

for i in list_Ram:
    if i[2] < min:
        min = i[2]

print(f"\nMin Ramanujan Taxi number: {min}")



