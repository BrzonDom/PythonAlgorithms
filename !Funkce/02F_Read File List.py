
file_list = ["data_01", "data_02"]

file_name = file_list[0]
file_path = "data\\" + file_name + ".txt"

Mat = []
file = open(file_path, 'rt')

# line = list(map(int, str_line.split()))

for line in file:
    Mat.append(list(map(int, line.split())))
file.close()

print(Mat)
print("", end="\n\t")

for row in Mat:
    print(row, end="\n\t")
