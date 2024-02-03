"""
Těžká varianta

    Napište program text_numbers.py, který převádí čísla mezi slovní a číselnou reprezentací.

        Vstup: řetězec ze standardního vstupu

            Tento řetězec buď obsahuje číslo v desítkové soustavě nebo číslo zapsané anglicky slovy, např.

            twohundredfiftyseventhousandthreehundredseventyfive

        Výstup: řetězec na standardní výstup

            tento řetězec obsahuje vstup převedený do opačného zápisu, tj. text na číslo, a číslo na text.
            pokud výstup není ani číslo, ani platný slovní popis, pak je výstup ERROR

    Všechna čísla jsou pouze celá čísla v rozsahu 1 až 999.999.
    Pro textovou reprezentaci čísel použijte pouze následující spojení:
        one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand.
    Vypisujte i úvodní jedničku, tj. pro vstup 1000 vypište onethousand, podobně pro 120 se očekává výstup onehundredtwenty

    Poznámka
        Snažte se napsat program s využitím pole, nebo asociativního pole na co nejmenší počet řádek.

"""

import copy


def processStr(numStr):

    rawDataLst = []

    """     Collect words from input and index them     """
    for numWrd in num_words:
        if numWrd in numStr:

            startPos = 0
            if numStr.count(numWrd) > 1:

                """     index() method finds the first occurrence of the specified value.
                            string.index(value, start, end) """
                index = numStr.index(numWrd, startPos)

                rawDataLst.append([numWrd, index])
                startPos = index + len(numWrd)

            else:
                rawDataLst.append([numWrd, numStr.index(numWrd)])

    ediDataLst = copy.deepcopy(rawDataLst)

    for i in range(len(rawDataLst)):
        for j in range(i+1, len(rawDataLst)):

            if rawDataLst[i][1] == rawDataLst[j][1]:
                """     For words found on the same position    
                            Remove the smaller one      """

                if len(rawDataLst[i][0]) < len(rawDataLst[j][0]):
                    ediDataLst.remove(rawDataLst[i])
                else:
                    ediDataLst.remove(rawDataLst[j])

    """     Sort by position, first to last    """
    ediDataLst.sort(key=lambda x: x[1])

    if not tempCheck(ediDataLst):
        return False

    """     Strip of indexes    """
    wordLst = []
    for numWrd in ediDataLst:
        wordLst.append(numWrd[0])

    return wordLst


def tempCheck(sorDataLst):

    """     Boolean-like table for found words on certain positions   """
    tabTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    """     List table for possible words on certain positions  """
    valTemp = [one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words, ["thousand"], one_num_words,
               ["hundred"], ty_num_words, teen_num_words, one_num_words]

    """     Description of certain positions      """
    desTemp = ["(1, 2,...) * 100 000", "100 * 1000", "(10, 20,...) * 1000", "(11, 12,...) * 1000", "(1, 2,...) * 1000",
               "(1, 2,...) * 100", "10, 20,...", "11, 12,...", "1, 2,..."]

    temp_Cnt = 1
    numWrd_Cnt = 1
    hunderd = ten = 1

    while (numWrd_Cnt <= len(wordLst)):
        # print(sor_data_list[-numWrd_Cnt][0])
        # numWrd_Cnt += 1

        if wordLst[-numWrd_Cnt] in valTemp[-temp_Cnt]:
            tabTemp[-temp_Cnt] = 1

            numWrd_Cnt += 1
        temp_Cnt += 1


    # print("Template table function: ", tabTemp)
    # for t in range(len(tabTemp)):
    #     if tabTemp[t]:
    #         print(f"\t{desTemp[t]}")
    # print()

    corOrder = True

    """
    Template table descriptions:

        0. tabTemp[0] ~ (1, 2,...) * 100 * 1000
        1. tabTemp[1] ~ 100 * 1000
        2. tabTemp[2] ~ (10, 20,...) * 1000
        3. tabTemp[3] ~ (11, 12,...) * 1000
        4. tabTemp[4] ~ (1, 2,...) * 1000
        5. tabTemp[5] ~ 1000
        6. tabTemp[6] ~ (1, 2,...) * 100
        7. tabTemp[7] ~ 100
        8. tabTemp[8] ~ 10, 20,...
        9. tabTemp[9] ~ 11, 12,...
        10. tabTemp[10] ~ 1, 2,...
    """

    if tabTemp[0]:
        if not (tabTemp[1] and tabTemp[5]):
            corOrder = False
            return False

    if tabTemp[1]:
        if not (tabTemp[0] and tabTemp[5]):
            corOrder = False
            return False

    if tabTemp[2]:
        if not (tabTemp[5] and not tabTemp[3]):
            corOrder = False
            return False

    if tabTemp[3]:
        if not (tabTemp[5] and not (tabTemp[3] or tabTemp[2])):
            corOrder = False
            return False

    if tabTemp[4]:
        if not (tabTemp[5] and not tabTemp[3]):
            corOrder = False
            return False

    if tabTemp[5]:
        if not tabTemp[4]:
            corOrder = False
            return False

    if tabTemp[6]:
        if not tabTemp[7]:
            corOrder = False
            return False

    if tabTemp[7]:
        if not tabTemp[6]:
            corOrder = False
            return False

    if tabTemp[8]:
        if tabTemp[9]:
            corOrder = False
            return False

    if tabTemp[9]:
        if tabTemp[8] or tabTemp[10]:
            corOrder = False
            return False

    if tabTemp[10]:
        if tabTemp[9]:
            corOrder = False
            return False

    return True


def toIntTemp(numStr):

    wordLst = processStr(numStr)

    if wordLst == False:
        print("ERROR - Failed template check")
        return

    """     Boolean template for found words on certain positions   """
    tabTemp = [False for state in range(11)]

    """     List template for possible words on certain positions  """
    valTemp = [one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words, ["thousand"], one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words]

    wrdCnt = tempCnt = 1

    while(wrdCnt <= len(wordLst)):

        if wordLst[-wrdCnt] in valTemp[-tempCnt]:
            tabTemp[-tempCnt] = True

            wrdCnt += 1
        tempCnt += 1

    sum_1 = sum_2 = 0
    wrdCnt = 0

    if tabTemp[0]:
        sum_2 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[1]:
        sum_2 *= num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[2]:
        sum_2 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[3]:
        sum_2 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[4]:
        sum_2 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[5]:
        sum_2 *= num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[6]:
        sum_1 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[7]:
        sum_1 *= num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[8]:
        sum_1 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[9]:
        sum_1 += num_dict[wordLst[wrdCnt]]
        wrdCnt += 1

    if tabTemp[10]:
        sum_1 += num_dict[wordLst[wrdCnt]]

    sum = sum_2 + sum_1

    print("Sum:", sum)
    return sum


def toIntAdd(numStr):

    wordLst = processStr(numStr)

    if wordLst == False:
        print("ERROR - Failed template check")
        return

    hund = False
    thou = False
    hundThou = False

    sum = 0

    for wrd in wordLst[::-1]:
        # print(wrd)

        if wrd in one_num_words:
            if hund:
                if thou:
                    if hundThou:
                        sum += 100000 * num_dict[wrd]
                    else:
                        sum += 1000 * num_dict[wrd]
                else:
                    sum += 100 * num_dict[wrd]
            else:
                sum += num_dict[wrd]


        elif wrd in teen_num_words:
            if hund:
                if thou:
                    sum += 1000 * num_dict[wrd]
                else:
                    sum += 100 * num_dict[wrd]
            else:
                sum += num_dict[wrd]


        elif wrd in ty_num_words:
            if hund:
                if thou:
                    sum += 1000 * num_dict[wrd]
                else:
                    sum += 100 * num_dict[wrd]
            else:
                sum += num_dict[wrd]


        elif wrd == "hundred":
            hund = True
            if thou:
                hundThou = True

        elif wrd == "thousand":
            thou = True

    print("Sum:", sum)
    return sum


num_dict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
    "eleven" : 11,
    "twelve" : 12,
    "thirteen" : 13,
    "fourteen" : 14,
    "fifteen" : 15,
    "sixteen" : 16,
    "seventeen" : 17,
    "eighteen" : 18,
    "nineteen" : 19,
    "twenty" : 20,
    "thirty" : 30,
    "forty" : 40,
    "fifty" : 50,
    "sixty" : 60,
    "seventy" : 70,
    "eighty" : 80,
    "ninety" : 90,
    "hundred" : 100,
    "thousand" : 1000
    }


num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
             "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

one_num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen_num_words = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ty_num_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
dec_num_words = ["hundred", "thousand"]

input_str_list = ["twohundredfiftyseventhousandthreehundredseventyfive",
                  "threehundredsixtyfive", "tentwenty", "seventytwothreehundred",
                  "tenonehundredtwenty", "elevenonehundredtwenty"]

# str_num = "twohundredfiftyseventhousandthreehundredseventyfive"
input_str = input_str_list[5]

# print(str_num.index("two"))
raw_data_list = []

print("Input string: ", input_str)
# print(str_num1.count("two"))

"""     Collect words from input and index them     """
for numWrd in num_words:
    if numWrd in input_str:
        if input_str.count(numWrd) > 1:
            """     For multiple occurances of a word   """

            pos = 0
            for next in range(input_str.count(numWrd)):

                """     index() method finds the first occurrence of the specified value.
                            string.index(value, start, end) """
                index = input_str.index(numWrd, pos)

                raw_data_list.append([numWrd, index])
                pos = index + len(numWrd)

        else:
            raw_data_list.append([numWrd, input_str.index(numWrd)])


print("\nRaw data: ", raw_data_list)
edi_data_list = copy.deepcopy(raw_data_list)


for i in range(len(raw_data_list)):
    for j in range(i+1, len(raw_data_list)):

        # print(f"{num_data_list[i]} : {num_data_list[j]}")

        if raw_data_list[i][1] == raw_data_list[j][1]:
            """     For words found on the same position    
                        Remove the smaller one      """

            if len(raw_data_list[i][0]) < len(raw_data_list[j][0]):
                # print(f"Remove {raw_data_list[i]}")
                edi_data_list.remove(raw_data_list[i])
            else:
                # print(f"Remove {raw_data_list[j]}")
                edi_data_list.remove(raw_data_list[j])


print("\nEdited data: ", edi_data_list)

sor_data_list = copy.deepcopy(edi_data_list)

"""     Sort by position    """
sor_data_list.sort(key = lambda x: x[1])

print("\nSorted data: ", sor_data_list)

"""     Strip of indexes    """
wordLst = []
for numWrd in sor_data_list:
    wordLst.append(numWrd[0])

print("Sorted list: ", wordLst)


"""     Boolean-like table for found words on certain positions   """
tabTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""     List table for possible words on certain positions  """
valTemp = [one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words, ["thousand"], one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words]

"""     Description of certain positions      """
desTemp = ["(1, 2,...) * 100 * 1000", "100 * 1000", "(10, 20,...) * 1000", "(11, 12,...) * 1000", "(1, 2,...) * 1000", "1000",
           "(1, 2,...) * 100", "100", "10, 20,...", "11, 12,...", "1, 2,..."]

"""
Template table descriptions:

    0. tabTemp[0] ~ (1, 2,...) * 100 * 1000
    1. tabTemp[1] ~ 100 * 1000
    2. tabTemp[2] ~ (10, 20,...) * 1000
    3. tabTemp[3] ~ (11, 12,...) * 1000
    4. tabTemp[4] ~ (1, 2,...) * 1000
    5. tabTemp[5] ~ 1000
    6. tabTemp[6] ~ (1, 2,...) * 100
    7. tabTemp[7] ~ 100
    8. tabTemp[8] ~ 10, 20,...
    9. tabTemp[9] ~ 11, 12,...
    10. tabTemp[10] ~ 1, 2,...
"""


# 1.Part
#   Sum:
#        template[10] = (one)  (+)   1, 2, 3, 4,...
#         template[9] = (teen) (+)   11, 12, 13,...
#         template[8] = (ty)   (+)   10, 20, 30,...
#         template[7] = (hund) (+)   100
#
#   Times:
#         template[6] = (one)  (*|7) 1, 2, 3,... * 100

# 2.Part
#   Sum:
#       template[5] = (thou) (+| )   1000
#       template[4] = (one)  (*| ) 1, 2, 3,... * 1000
#       template[3] = (teen) (*) 11, 12, 13,... * 1000
#       template[2] = (ty)   (*) 10, 20, 30,...
#       template[1] = (hund)
#       template[0] = (one)


temp_Cnt = 1
numWrd_Cnt = 1
hunderd = ten = 1

while(numWrd_Cnt <= len(wordLst)):
    # print(sor_data_list[-numWrd_Cnt][0])
    # numWrd_Cnt += 1


    if wordLst[-numWrd_Cnt] in valTemp[-temp_Cnt]:
        tabTemp[-temp_Cnt] = 1

        numWrd_Cnt += 1
    temp_Cnt += 1

print()
print("Template table: ", tabTemp)
for t in range(len(tabTemp)):
    if tabTemp[t]:
        print(f"\t{desTemp[t]}")
print()

# print("Template table descriptions")
# for d, des in enumerate(desTemp):
#     print(f"\t{d}. tabTemp[{d}] ~ {des}")
# print()

chckTemp = tempCheck(sor_data_list)
print("Template check: ", chckTemp)
# tempCheck(sor_data_list)

if chckTemp:
    sum_1 = sum_2 = 0
    numWrd_Cnt = 0


    if tabTemp[0]:
        sum_1 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[1]:
        sum_1 *= num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[2]:
        sum_1 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[3]:
        sum_1 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[4]:
        sum_1 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[5]:
        sum_1 *= num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[6]:
        sum_2 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[7]:
        sum_2 *= num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[8]:
        sum_2 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[9]:
        sum_2 += num_dict[wordLst[numWrd_Cnt]]
        numWrd_Cnt += 1

    if tabTemp[10]:
        sum_2 += num_dict[wordLst[numWrd_Cnt]]

    sum = sum_1 + sum_2

    print("\nSum:", sum)
    print()
else:
    print("\n\tERROR - Failed template check\n")

print("toIntTemp function:")
print("\t", end="")
toIntTemp(input_str)
# print("\tSum:", toIntTemp(input_str))
print()

print("toIntAdd function:")
print("\t", end="")
toIntAdd(input_str)
# print("\tSum:", toIntAdd(input_str))