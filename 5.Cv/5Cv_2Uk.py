"""
Stopa matice

    Napište funkci pro výpočet stopy matice

"""

Mat2D = [[ 7,  0,  1, -5],
         [-9,  1, -7,  8],
         [ 8, -6,  6,  9],
         [ 4, -1,  7, -7]]

row = len(Mat2D)
col = len(Mat2D[0])

print(f"Row: {len(Mat2D)}")
print(f"Col: {len(Mat2D[0])}")

print()

for r in range(row):
    for c in range(col):
        print(Mat2D[r][c], end=" ")
    print()

Trace = 0

for r in range(row):
    Trace += Mat2D[r][r]

print()

print(f"Trace: {Trace}")