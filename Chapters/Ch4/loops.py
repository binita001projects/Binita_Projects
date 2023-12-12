from calendar import week

numbers =[1,2,3]
cereals = ['Pops','cap','cookie crisp']
print(cereals)
print(numbers[1])
x = numbers.pop()
print(numbers)
y = numbers.append(4)
numbers.remove(2)
print(numbers)
numbers.reverse()

numbers.append(5)
numbers.append(7)

numbers.sort()
numbers.append(11)
print(numbers)

x = 0
while x < 5:
    print(x)
    x += 1

y = 15
while y < 20:
    print(y)
    y += 1

print('#############')
z = 19
while z < 29:
    print(z)
    z +=3
print('#############')
numbers = [1, 2, 3]
for num in numbers:
    print(num * 2)


print('''while True:
    do something()''')


for character in "carlos":
    print(character.capitalize())

name_as_lsi = list('carlos')
print(name_as_lsi)

name = ''.join(name_as_lsi)
print(name)

numbers =[1, 2, 3, 4]
for num in numbers:
    print(num * 2)
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in week:
    print(day)

print("#######*******#######)")
search = "Python"
inventory = ['Clean COde', 'Python', 'Naturo']
if search in inventory:
    print('available')
else:
    print(('not available'))