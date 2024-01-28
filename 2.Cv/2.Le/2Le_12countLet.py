
def countLet(text, letter):
    cnt = 0

    for i in range(len(text)):
        if text[i] == letter:
            cnt += 1

    return cnt

text = "hippopotomonstrosesquippedaliophobia"

print(f"Text: {text}\n")

# for char in text:
#     if char != " ":
#         print(char, end="")

for char in range(ord('a'), ord('z')+1):
    cnt = countLet(text, chr(char))

    if cnt != 0:
        print(f"\t{chr(char)} : {cnt}")