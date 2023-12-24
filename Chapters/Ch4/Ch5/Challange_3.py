Vehicle = {
    'Model' : 'Tesla',
    'Vehicle Gear' : 6,
    'Model_No' :'ASPT56',
    'Charcoal_Black_Colour' : True,
    'Features' : ['Stylish', 'Power Engine', 'Speed']
}
print(Vehicle)
Vehicle.update({'Wheels' : 'Power_sports'})
print(Vehicle)

Roll_1 = input('Roll the Dice:')
Bal1 = 20 - int(Roll_1)
print(f'You rolled {Roll_1} you are now on space {Roll_1} and have {Bal1} more to go')

Roll_2 = input('Roll the Dice:')
Bal2 = Bal1 - int(Roll_2)
print(f'You rolled {Roll_2} you are now on space {Roll_2} and have {Bal2} more to go')

Roll_3 = input('Roll the Dice:')
Bal3 = Bal2 - int(Roll_3)
print(f'You rolled {Roll_3} you are now on space {Roll_3} and have {Bal3} more to go')

Roll_4 = input('Roll the Dice:')
Bal4 = Bal3 - int(Roll_4)
print(f'You rolled {Roll_4} you are now on space {Roll_4} and have {Bal4} more to go')

Roll_5 = input('Roll the Dice:')
Bal5 = Bal4 - int(Roll_5)
print(f'You rolled {Roll_5} you are now on space {Roll_5}. you are on space {Bal5}')


Balance = int(Roll_1) + int(Roll_2) + int(Roll_3) + int(Roll_4) + int(Roll_5)
print(Balance)

if Balance == 20:
    print('Congratulations your value is 20')
if Balance >= 21:
    print('Your Value is greater than 20')
if Balance <= 19:
    print('Value is Less than 20')
else: print('Invalid input')
