
sentence = input('Enter any sentance /Word: ')
vovels = ['a', 'e', 'i', 'o', 'u']
print(sentence)
letters = list(sentence)
print(letters)
print(vovels)

if "a" in letters:
    print("Yes")

a = letters.count("a")
e = letters.count("e")
i = letters.count("i")
o = letters.count("o")
u = letters.count("u")
sum_vovels = (a+e+i+o+u)
print(sum_vovels)