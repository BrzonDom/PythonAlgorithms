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

def num_dict(word):

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

    num = num_dict[word]
    return num

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

for numWrd in num_words:
    if numWrd in str_num:
        if str_num.count(numWrd) > 1:

            pos = 0
            for next in range(str_num.count(numWrd)):
                index = str_num.index(numWrd, pos)
                raw_data_list.append([numWrd, index])
                pos = index + len(numWrd)


            # for next in range(str_num.count(num_word)):
            #     raw_data_list.append()
        else:
            raw_data_list.append([numWrd, str_num.index(numWrd)])
    # elif "and" in str_num:
    #     raw_data_list.append(["and", str_num.index("and")])

print("\nRaw data: ", raw_data_list)
edi_data_list = copy.deepcopy(raw_data_list)

finish = 1

for i in range(len(raw_data_list)):
    for j in range(i, len(raw_data_list)):

        # print(f"{num_data_list[i]} : {num_data_list[j]}")

        if i == j:
            continue

        elif raw_data_list[i][1] == raw_data_list[j][1]:

            if len(raw_data_list[i][0]) < len(raw_data_list[j][0]):
                # print(f"Remove {raw_data_list[i]}")
                edi_data_list.remove(raw_data_list[i])
            else:
                # print(f"Remove {raw_data_list[j]}")
                edi_data_list.remove(raw_data_list[j])


print("\nEdited data: ", edi_data_list)

sor_data_list = copy.deepcopy(edi_data_list)
sor_data_list.sort(key = lambda x: x[1])

print("\nSorted data: ", sor_data_list)

template_table = [      0,           0,            0,              0,             0,             0,            0,            0,          0,               0,              0]
template_values = [one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words, ["thousand"], one_num_words, ["hundred"], ty_num_words, teen_num_words, one_num_words]

# template_table[9] = 1, 2, 3, 4,...
# template_table[8] = 11, 12, 13,...
# template_table[7] = 10, 20, 30,...
# template_table[6] = 1st 100
# template_table[5] = 1st 1, 2, 3,... * 100
# template_table[4] =

temp_Cnt = 1
numWrd_Cnt = 1
hunderd = ten = 1

while(numWrd_Cnt <= len(sor_data_list)):
    # print(sor_data_list[-numWrd_Cnt][0])
    # numWrd_Cnt += 1
    if sor_data_list[-numWrd_Cnt][0] in template_values[-temp_Cnt]:
        template_table[-temp_Cnt] = 1
        temp_Cnt += 1
        numWrd_Cnt += 1
    else:
        temp_Cnt += 1

print()
print(template_table)

sum_1 = sum_2 = 0
numWrd_Cnt = 0


if template_table[0]:
    sum_1 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[1]:
    sum_1 *= num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[2]:
    sum_1 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[3]:
    sum_1 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[4]:
    sum_1 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[5]:
    sum_1 *= num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[6]:
    sum_2 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[7]:
    sum_2 *= num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[8]:
    sum_2 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[9]:
    sum_2 += num_dict(sor_data_list[numWrd_Cnt][0])
    numWrd_Cnt += 1

if template_table[10]:
    sum_2 += num_dict(sor_data_list[numWrd_Cnt][0])

sum = sum_1 + sum_2

print("\nSum:", sum)