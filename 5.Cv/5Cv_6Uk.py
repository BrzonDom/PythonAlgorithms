"""
Načtení zakódovaného obrázku ze souboru

    Stáhněte si soubor encoded.txt, jenž obsahuje zakódovaný obrázek. Každý řádek obsahuje různý počet dvojic znak+číslo (např. #2) oddělených mezerou. Pro zobrazení obrázku se musí tyto dvojice prvně dekódovat.
    Pročtete si a porozumějte tomutou kódu a poté ho spusťte.

"""


## | ------------------ Functions definition ------------------ |

# [You should understand this function]
# Function loading given file
def loadFile(filename):
    mat = []  # create empty list
    f = open(filename, 'rt')  # open file with name 'filename' in 'read' and 'text' modes
    for line in f:  # iterate all lines in the file
        # parse single line from file:
        #  1) strip: remove spaces and new line characters from beginning and end of the line
        #  2) split: split line by spaces, returns list
        #  3) map:   maps each element to string
        #  4) list:  convert output of map to list of strings
        lst = list(map(str, line.strip().split(' ')))
        mat.append(lst)  # append list to our 'mat' variable
    f.close()
    return mat


# [You don't need to understand this function]
# Function decoding our file
def decode(mat):
    mat_decoded = []  # create empty output list
    for lst in mat:  # for each list in 'mat' (list of lists)
        decoded = ''  # initialize the decoded string to empty value
        for s in lst:  # for each encoded value in list 'lst'
            char = s.rstrip('0123456789')  # cut the numbered part of our string out, example: #2 -> #
            num = s[len(char):]  # retrieve the cut part, example: 2
            if char == 's':  # space is encoded as 's'
                char = ' '  # replace 's' by space character
            decoded = decoded + int(num) * char  # decode and store into 'decoded' variable
        mat_decoded.append(decoded)  # append single decoded line into our output list
    return mat_decoded  # return output list


## | -------------- Python starts processing here ------------- |
encoded = loadFile('encoded.txt')  # load the encoded file
decoded = decode(encoded)  # decode the encoded file
for line in decoded:  # print our decoded file
    print(line)