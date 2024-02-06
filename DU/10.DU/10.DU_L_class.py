import sys

class Board:
    def __init__(self, size=0):
        self.size = size
        self.values = {}
        self.values_list = []

    def board_set(self, file_name):

        file = open(file_name, "rt")
        self.values_list = []
        self.values = {}

        for str_line in file:
            line = list(map(int, str_line.split()))
            self.values_list.append(line)

    def isIn(self, row, col):

        return (col >= 0) and (col < self.size) and (row >= -(col // 2)) and (row < (self.size - col // 2))





file_list = ["PrL_1", "PrL_2", "PrL_3"]

# file_name = sys.argv[1]
file_name = file_list[2]
file_path = "data\\" + file_name + ".txt"

file = open(file_path, "r")

tst_size = 0
