'''cereals = ['chex', 'Fruty pebbles', 'cookie crisps']
quantities = [24, 12, 8]

for index, cereals in enumerate(cereals):
    print(cereals,quantities[index])

cereals1 = {
    'Chex': 24,
    'Pops':12,
    'Cookie Crisps':8
}

print(cereals1)

print(cereals1['Chex'])
print(cereals1.get('Pops'))
print((cereals1.get('Cher',0)))

numbers1 = {
    1: 'One',
    2: 'Two'
}

for key in numbers1.keys():
    print(key)

for val in numbers1.values():
    print(val)

for item in numbers1.items():
    print(item)

dictionary = {}
dictionary1 = dict()

cereals2 = {}
cereals2['chex'] = 12
print(cereals2)

cereals2['chex'] = 15
print(cereals2)
'''

me = {
    'first_name' : 'binita',
    'last_name' : 'KP'
}

print(me)
me.update({'age': 30})
print(me)

