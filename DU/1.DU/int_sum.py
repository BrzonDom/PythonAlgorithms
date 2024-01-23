# In1 = 2
# In2 = -3

In1 = int(input())
In2 = int(input())

Res = 0

if (In1 <= In2):
    Rng = range(In1, In2+1)
    Last = In2
elif (In1 > In2):
    Rng = range(In2, In1+1)
    Last = In1

for i in Rng:
    Res += (i**4)

# print("Vstup:")
# print(str(In1))
# print(str(In2))
    # print("\t" + str(In1))
    # print("\t" + str(In2))
# print("Výstup:")
print(str(Res))
    # print("\t" + str(Res))

# print("\n")

# print("Range:", end=" ")
# for i in Rng:
#     print(i, end=" ")
#
# print("")
# print("Expresion:", end=" ")
# for i in Rng:
#     if (i == Last):
#         Str = "({})^4 = {}"
#         print(Str.format(i, Res))
#     else:
#         Str = "({})^4 +"
#         print(Str.format(i), end=" ")