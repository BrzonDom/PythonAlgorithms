"""
Flood fill

    Napište program, který v zadané matici nahradí souvislou oblast 0 ze zadaného bodu hodnotou 2.
    Matici vezměte jako vnitřní proměnnou:

        m=[[0,0,1,0,0,1,0,0,0,0],
           [0,0,1,0,0,1,0,0,0,0],
           [0,0,1,1,0,1,0,0,0,1],
           [0,0,1,0,0,0,1,0,1,0],
           [0,0,1,0,0,0,0,1,0,0],
           [0,0,1,1,0,1,0,0,0,0],
           [0,0,1,0,1,1,1,1,0,0],
           [0,0,1,0,0,1,0,1,1,1],
           [0,0,1,0,0,1,0,0,0,0],
           [0,0,1,0,0,1,0,0,0,0]]


    Program si načte počáteční bod ze standardního vstupu
    Do zásobníku vloží vstupní bod
    Opakuje, dokud není zásobník prázdný:
        uloží si hodnotu (x, y) prvního prvku v zásobníku
        odstraní první prvek ze zásobníku
        pokud je hodnota matice v bodě (x, y) rovna 0, vloží do zásobníku:
            souřadnice (x-1,y),(x+1,y),(x,y-1),(x,y+1), pokud jsou v mezích rozměrů matice
    Vytiskněte výslednou matici
    Program otestujte pro vstupy: 4,4 a 9,9

    Co by se stalo, pokud byste na zásobník vložili i body (x-1,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1)?
    Jaká je složitost tohoto algoritmu? Uměli byste tento algoritmus zefektivnit, aby nevkládal jedno pole matice do zásobníku vícekrát?

"""

Mat = [[0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 0, 0, 1],
       [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
       [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 1, 1, 1, 1, 0, 0],
       [0, 0, 1, 0, 0, 1, 0, 1, 1, 1],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 1, 0, 0, 0, 0]]

# ("⬜") = 0
# ("⬛") = 1
# ("🟥") = 2

def showMat(Mat):

    print("", end="\n\t")

    for row in Mat:
        for col in row:
            if col == 0:
                print("⬜", end="")
            elif col == 1:
                print("⬛", end="")
            elif col == 2:
                print("🟥", end="")
        print("", end="\n\t")

input = [[4,4], [9,9]]

matRow = len(Mat)
matCol = len(Mat[0])

boardRow = [item for item in range(0, matRow)]
boardCol = [item for item in range(0, matCol)]
# print(boardRow)
# print(boardCol)

print(f"Row: {matRow}\nCol: {matCol}")

# showMat(Mat)

stackFill = []
stackVisit = []

stackFill.append(input[1])
print(stackFill)
# stackFill.append([3,2])
# stackFill.append([7,5])
# print(stackFill)

print(stackFill[-1][0])

showMat(Mat)

while len(stackFill) > 0:

    curRow = stackFill[-1][0]
    curCol = stackFill[-1][1]

    # if Mat[curRow][curCol] == 0:
    #     Mat[curRow][curCol] = 2
    #     stackVisit.append(stackFill[-1])

    Mat[curRow][curCol] = 2
    stackVisit.append(stackFill[-1])
    stackFill.pop()

    if (curRow+1) in boardRow:
        if Mat[curRow+1][curCol] == 0 and [curRow+1, curCol] not in (stackVisit or stackFill):
            stackFill.append([curRow+1, curCol])

    if (curRow-1) in boardRow:
        if Mat[curRow-1][curCol] == 0 and [curRow-1, curCol] not in (stackVisit or stackFill):
            stackFill.append([curRow-1, curCol])

    if (curCol+1) in boardCol:
        if Mat[curRow][curCol+1] == 0 and [curRow, curCol+1] not in (stackVisit or stackFill):
            stackFill.append([curRow, curCol+1])

    if (curCol-1) in boardCol:
        if Mat[curRow][curCol-1] == 0 and [curRow, curCol-1] not in stackVisit:
            stackFill.append([curRow, curCol-1])


showMat(Mat)