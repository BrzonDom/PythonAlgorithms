import copy

words = []

# file = open("german.txt", "rt")
#
# print("Text from file to list:")
# print("[")
# for line in file:
#     print(f"\"{line[:-1]}\\n\",")
# print("]")
# file.close()

file_text = [
            "Wachsam wer schones barbele gewogen ein eigenes . Pa en so bist ja\n",
            "eile hals sein euer . Bett und sage weg mirs gelt fur dort .\n",
            "Kartoffeln halboffene ob ungerechte vertreiben lehrlingen te .\n",
            "Brotkugeln vorpfeifen neidgefuhl zu erhaltenen so es nachtessen\n",
            "geheiratet . Wollen herauf leisen rothfu freude aus nah .\n",
            "Gerbers unrecht te in zwiebel an .\n",
            "Meinung atemzug konntet gerbers dorthin wie wer ein . Spateren\n",
            "verlogen blattern pa mi . Regen nur fremd schlo lernt brief\n",
            "ihren den . Schritt schurze eigenes ige ehe gru ahnlich . Die\n",
            "sieben singen kannst der treppe . Hat ehe vorn trat lich gute\n",
            "arme . Feierabend wei betrachtet gearbeitet jahreszeit\n",
            "grashalden ist . Du acht im te la fand wert \n",
            ]

# org_text = []
prc_text = []


print("Orginal text:")
for line in file_text:
    # org_text.append(line)
    print("\t", line, end="")

    line = line.strip().lower()
    line = line.replace(".","").replace(",", "")

    prc_text.append(line)
    # print("\t", line)

    wordsLine = line.split()
    words += wordsLine

# file.close()
print("\n")

print("Processed text:")
for line in prc_text:
    print("\t", line)
print("\n")

print("Loaded", len(words), "words")
print()

hist = {}

for word in words:
    if not word in hist:
        hist[word] = 0
    hist[word] += 1

hist_lst = list(hist.items())
# print(list(hist.items()))


hist_lst.sort(key=lambda x: x[1], reverse=True)
print("Top 10 most used words:")
for i in range(10):
    print(f"\t{hist_lst[i][0]}: {hist_lst[i][1]}x")