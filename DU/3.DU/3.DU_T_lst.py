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

wrd_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}


def processStr(numStr):

    rawDataLst = []

    """     Collect words from input and index them     """
    for numWrd in num_words:
        if numWrd in numStr:

            if numStr.count(numWrd) > 1:

                startPos = 0
                for next in range(numStr.count(numWrd)):

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

    """     Strip of indexes    """
    wordLst = []
    for numWrd in ediDataLst:
        wordLst.append(numWrd[0])

    if not tempCheck(wordLst):
        return False

    return wordLst


def tempCheck(wordLst):

    """     Boolean-like table for found words on certain positions   """
    tabTemp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    """     List table for possible words on certain positions  """
    valTemp = [one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words, ["thousand"], one_num_words,
               ["hundred"], ty_num_words, teen_num_words, one_num_words]

    tempCnt = 1
    numWrdCnt = 1

    while (numWrdCnt <= len(wordLst)):
        # print(sor_data_list[-numWrdCnt][0])
        # numWrdCnt += 1

        if wordLst[-numWrdCnt] in valTemp[-tempCnt]:
            tabTemp[-tempCnt] = 1

            numWrdCnt += 1
        tempCnt += 1

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
            return False

    if tabTemp[1]:
        if not (tabTemp[0] and tabTemp[5]):
            return False

    if tabTemp[2]:
        if not (tabTemp[5] and not tabTemp[3]):
            return False

    if tabTemp[3]:
        if not (tabTemp[5] and not (tabTemp[3] or tabTemp[2])):
            return False

    if tabTemp[4]:
        if not (tabTemp[5] and not tabTemp[3]):
            return False

    if tabTemp[5]:
        if not tabTemp[4]:
            return False

    if tabTemp[6]:
        if not tabTemp[7]:
            return False

    if tabTemp[7]:
        if not tabTemp[6]:
            return False

    if tabTemp[8]:
        if tabTemp[9]:
            return False

    if tabTemp[9]:
        if tabTemp[8] or tabTemp[10]:
            return False

    if tabTemp[10]:
        if tabTemp[9]:
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

    print("Temp Num:", sum)
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

    print("Add Num:", sum)
    return sum


def toStr(numb):

    numStr = ""

    exp = 100000
    if exp < numb:
        rest = numb % exp
        base = (numb - rest) // exp

        numb = copy.deepcopy(rest)

        # print(f"{wrd_dict[base]}hundered", end="")
        numStr += f"{wrd_dict[base]}hundered"

    exp = 1000
    if exp < numb:
        rest = numb % exp
        base = (numb - rest) // exp

        numb = copy.deepcopy(rest)

        if base in wrd_dict:
            # print(f"{wrd_dict[base]}thousand")
            numStr += f"{wrd_dict[base]}thousand"

        else:
            rest = base % 10
            baseTh = (base - rest)

            # print(f"{wrd_dict[baseTh]}{wrd_dict[rest]}thousand", end="")
            numStr += f"{wrd_dict[baseTh]}{wrd_dict[rest]}thousand"

    exp = 100
    if exp < numb:
        rest = numb % exp
        base = (numb - rest) // exp

        numb = copy.deepcopy(rest)

        # print(f"{wrd_dict[base]}hundered", end="")
        numStr += f"{wrd_dict[base]}hundered"

        if rest in wrd_dict:
            # print(f"{wrd_dict[rest]}")
            numStr += f"{wrd_dict[rest]}"

        else:
            rest = numb % 10
            base = (numb - rest)

            # print(f"{wrd_dict[base]}{wrd_dict[rest]}")
            numStr += f"{wrd_dict[base]}{wrd_dict[rest]}"

    print("Str: ", numStr)
    return numStr


num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
             "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

one_num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen_num_words = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ty_num_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
dec_num_words = ["hundred", "thousand"]


input_str_list = ["twohundredfiftyseventhousandthreehundredseventyfive",
                  "543210", "threehundredsixtyfive", "341308", "213",
                  "tentwenty", "seventytwothreehundred", "12v34"]

# str_num = "twohundredfiftyseventhousandthreehundredseventyfive"

for i in range(len(input_str_list)):
    input_str = input_str_list[i]

    print(f"{i}. Input: {input_str}")

    intToStr = True
    strToInt = True

    for char in input_str:
        if not ('a' <= char <= 'z') and strToInt:
            # print("NOT NUM STR")
            strToInt = False

        if not ('0' <= char <= '9') and intToStr:
            # print("NOT STR NUM")
            intToStr = False


    if strToInt:
        print("\t", end="")
        toIntAdd(input_str)
        print("\t", end="")
        toIntTemp(input_str)

    elif intToStr:
        print("\t", end="")
        toStr(int(input_str))

    else:
        print("\tERROR - Letter in number input")

    print()



