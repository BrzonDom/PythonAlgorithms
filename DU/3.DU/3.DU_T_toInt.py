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


num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
             "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

one_num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teen_num_words = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ty_num_words = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
dec_num_words = ["hundred", "thousand"]


# str_num = "twohundredfiftyseventhousandthreehundredseventyfive"
str_num = "threehundredsixtyfive"

# print(str_num.index("two"))
raw_data_list = []

print("String: ", str_num)
# print(str_num1.count("two"))

"""     Collect words from input and index them     """
for numWrd in num_words:
    if numWrd in str_num:
        if str_num.count(numWrd) > 1:
            """     For multiple occurances of a word   """

            pos = 0
            for next in range(str_num.count(numWrd)):

                """     index() method finds the first occurrence of the specified value.
                            string.index(value, start, end) """
                index = str_num.index(numWrd, pos)

                raw_data_list.append([numWrd, index])
                pos = index + len(numWrd)

        else:
            raw_data_list.append([numWrd, str_num.index(numWrd)])


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
sor_list = []
for numWrd in sor_data_list:
    sor_list.append(numWrd[0])

print("Sorted list: ", sor_list)


"""     Boolean-like table for found words on certain positions   """
template_table = [      0,           0,            0,              0,             0,             0,            0,            0,          0,               0,              0]

"""     List table for possible words on certain positions  """
template_values = [one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words, ["thousand"], one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words]

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

while(numWrd_Cnt <= len(sor_list)):
    # print(sor_data_list[-numWrd_Cnt][0])
    # numWrd_Cnt += 1


    if sor_list[-numWrd_Cnt] in template_values[-temp_Cnt]:
        template_table[-temp_Cnt] = 1

        numWrd_Cnt += 1
    temp_Cnt += 1

#
# print()
# print(template_table)
#
sum_1 = sum_2 = 0
numWrd_Cnt = 0


if template_table[0]:
    sum_1 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[1]:
    sum_1 *= num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[2]:
    sum_1 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[3]:
    sum_1 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[4]:
    sum_1 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[5]:
    sum_1 *= num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[6]:
    sum_2 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[7]:
    sum_2 *= num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[8]:
    sum_2 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[9]:
    sum_2 += num_dict[sor_list[numWrd_Cnt]]
    numWrd_Cnt += 1

if template_table[10]:
    sum_2 += num_dict[sor_list[numWrd_Cnt]]

sum = sum_1 + sum_2

print("\nSum:", sum)