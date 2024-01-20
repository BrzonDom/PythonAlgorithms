"""
Výpis matice

    Napište funkci printMatrix, která vypíše matici zadanou 2D polem
    Prvky budou odděleny mezerou a každý řádek bude vypsán na nový řádek
    Kromě prvků matice nebude vypsán žádný jiný znak

"""

MatNum = [[1,2,3],[4,0,5],[7,-1,2]]
MatTxt = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]


print("Txt. Mat.:", end="\n\t")

for row in MatTxt:
    for col in row:
        print(col, end=" ")
    print(end="\n\t")
print()

print("Num. Mat.:", end="\n\t")
for row in MatNum:
    for col in row:
        print(f"{col:2}", end=" ")
    print(end="\n\t")
print()