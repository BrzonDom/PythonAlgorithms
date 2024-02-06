
str_seq_list = ["3 3 3 3 3 3 3 3 3", "1 1 1 6 2 2 2 6 1 1 1", "1 2 5 -6 8 -3 2 1 1 2 2 5 -6 8 -3 2 3"]
str_seq = str_seq_list[2]
seq = [int(num) for num in list(str_seq.split(" "))]
lenSeq = len(seq)

LCS_Mat = [[0 for i in range(lenSeq + 1)] for j in range(lenSeq + 1)]

print("Sequens:")
print(f"\tLen: {lenSeq} Seq: {seq}")
print()


def LCS_1Vis(seq, Mat):
    len_seq = len(seq)

    # LCS_Mat = [[0 for i in range(lenSeq + 1)] for j in range(lenSeq + 1)]

    print("\n\n\t   |", end="")
    for b in range(lenSeq):
        print(f" {seq[b]:2} |", end="")
    print("\n\t", end="")

    for r in range(1, lenSeq + 2):
        print(" --", end="")
        for b in range(1, lenSeq + 1):
            print("+----", end="")
        print("+\n\t", end="")
        # print()

        if r == lenSeq+1:
            break
        print(f"{seq[r-1]:2} ", end="")

        for c in range(1, lenSeq + 1):

            # print(f"| {Mat[r][c]:2} ", end="")

            if LCS_Mat[r][c]:
                print(f"| {Mat[r][c]:2} ", end="")
            else:
                print(f"|    ", end="")


        print("|\n\t", end="")



str_seq_list = [["1 2 3 3 3 3 3 3 3 3 5 6", "3 3 3 1 3 3 3 3 3 3 3 3"],
                ["10", "1 2 3 10 3 2 1"],
                ["1 2 3 4", "1 2 3 4"]]

str_seq = str_seq_list[0]
str_seq1 = str_seq[0]
str_seq2 = str_seq[1]

seq1 = [int(num) for num in list(str_seq1.split(" "))]
seq2 = [int(num) for num in list(str_seq2.split(" "))]

len_seq1 = len(seq1)
len_seq2 = len(seq2)

print("Sequenses:")
print(f"\tLen: {len_seq1} Seq: {seq1}")
print(f"\tLen: {len_seq2} Seq: {seq2}")
print()

LCS_Mat = [[0 for i in range(len_seq1 + 1)] for j in range(len_seq2 + 1)]


def LCS_2Vis(seq, Mat):

    seq1 = seq[0]
    seq2 = seq[1]
    lenSeq1 = len(seq1)
    lenSeq2 = len(seq2)

    print("\n\n\t   |", end="")
    for b in range(lenSeq2):
        print(f" {seq2[b]:2} |", end="")
    print("\n\t", end="")

    for r in range(1, lenSeq1 + 2):
        print(" --", end="")
        for b in range(1, lenSeq2 + 1):
            print("+----", end="")
        print("+\n\t", end="")
        # print()

        if r == lenSeq1+1:
            break
        print(f"{seq1[r-1]:2} ", end="")

        for c in range(1, lenSeq2 + 1):

            # print(f"| {Mat[r][c]:2} ", end="")

            if LCS_Mat[r][c]:
                print(f"| {Mat[r][c]:2} ", end="")
            else:
                print(f"|    ", end="")


        print("|\n\t", end="")
