def add(x, y):
    return x + y


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_positive(number):
    if number >= 1:
        return True
    else:
        return False
def convert_to_number(string):
    return int(string)

def add(x, y):
    if isinstance(x,str) or isinstance(y,str):
        return 'error: invalid number entered'
    else:
        return x + y

def Challenge_1():
    input_1 = input('Enter a Number: ')
    input_2 = input('Enter another Number: ')
    Number1 = convert_to_number(input_1)
    Number2 = convert_to_number(input_2)
    total = add(Number1,Number2)
    print(total)

if __name__ == '__main__':
    Challenge_1()