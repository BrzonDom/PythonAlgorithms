
"""     !!   Redirecting sys.stdout to file   !! """

import sys
org_stdout = sys.stdout

inOp = 0
file_namePrt = ""
file_specPrt = f".{inOp+1}"
file_pathPrt = "output\\" + file_namePrt + file_specPrt + ".txt"

file_prt = open(file_pathPrt, 'w')
sys.stdout = file_prt

# for i in range(2):
#     print('i = ', i)

print("Hello world")


"""     !!   Redirecting sys.stdout back org_stdout   !! """

sys.stdout = org_stdout
file_prt.close()