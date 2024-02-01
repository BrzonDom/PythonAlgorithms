
def myHash(text):
    prime = 67
    hsh = 0

    for letter in text:
        hsh = ((hsh * prime) + ord(letter)) % m

    return hsh


# print(f"a: {ord('a')}")
# print(f"z: {ord('z')}")
#
# for indx in range(ord('a'), ord('g')):
#     print(f"'{chr(indx)}', ", end="")

dict_lst = ['a', 'b', 'c', 'd', 'e', 'f']

m = 10
n = len(dict_lst)
l = m / n

print("My hash:")
for char in dict_lst:
    print(f"\tmyHash({char}) = {myHash(char)}")

print()

print("Build-in hash:")
for char in dict_lst:
    print(f"\thash({char}) = {hash(char)}")