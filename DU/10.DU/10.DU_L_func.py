
from board import *

def isIn(row, col, size):
    return (col >= 0) and (col < size) and (row >= -(col // 2)) and (row < (size - col // 2))


def data_to_val_dict(data):
    """     Make graph(dictionary) out of data  """

    for row, col, val in data:

        if row not in value_dict:
            value_dict[row] = {}
        value_dict[row][col] = val


def data_scan(data):

    piecesCnt = 0

    for line in data_list:

        if line[2] == 2:
            """     Find the coordinates of grasshopper    """
            hopperCo = [line[0], line[1]]
        elif line[2] == 1:
            """     Count the number of other pieces    """
            piecesCnt += 1

    return piecesCnt, hopperCo



file_list = ["PrL_1", "PrL_2", "PrL_3", "eboard-5002.txt", "eboard-5412", "eboard-6759", "eboard-7089", "eboard-7141", "eboard-7639", "eboard-8904"]

file_name = file_list[1]
# file_name = "eboard-7296"
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")
print(f"File: {file_name}.txt\n")


graph = []

# line = file.readline()
# print(line)
#
# res = list(map(int, line.split()))
# print(res)


data_list = []
value_dict = {}
border = []

row_size = 0
col_size = 0
line_cnt = 1


for str_line in file:
    """     Read line in input file     """

        # Print the lines of input
    # print(str_line, end="")

    if str_line[0] in ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    #     line_cnt += 1

        line = list(map(int, str_line.split()))

            # Print the coord of input
        # print(f"{line[0]}:{line[1]}")

        # Print the coord and coresp value of input
        print(f"\t{line[0]}:{line[1]} = {line[2]}")

        border.append([line[0], line[1]])
        data_list.append(line)
        # print(line)
        # graph[[line[0], line[1]]] = line[2]

        row_size = max(row_size, line[0])
        col_size = max(col_size, line[1])

    else:
        print("! Wrong input !")
        file.close()
        quit()

file.close()

size = row_size + 1

print()
print(f"Total Size: {size*size}")
print(f"\tSize: {size}")
print(f"\tRow:  {row_size}")
print(f"\tCol:  {col_size}")
print()

"""     Make graph(dictionary) out of data  """
data_to_val_dict(data_list)


"""     Find coord and cnt of pieces out of data    """
pieces_cnt, hopper_coord = data_scan(data_list)

print(f"Grasshopper coordinates: [{hopper_coord[0]}, {hopper_coord[1]}]")
print(f"Number of pieces: {pieces_cnt}")


