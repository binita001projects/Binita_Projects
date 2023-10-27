from Chapters.Ch2.add_numbers import add, is_even, is_positive, convert_to_number


def test_string_input():
    output = add('carlos',2)
    assert output == 'error: invalid number entered'

def test_4_is_even():
    assert is_even(4)

def test_5_is_odd():
    assert is_even(5) is False

def test_adding_even_numbers_returs_even_numbers():
    number = add(2, 2)
    assert number == 4
    assert is_even(number)

def test_adding_negative_numbers_returns_negative_numbaers():
    number = add(-1,-1)
    assert number == -2
    assert is_even(number)

def test_adding_negative_and_positive_numbers_returns_positive_if_greater():
    number = add(2, -1)
    assert number == 1
    assert is_positive(number)
def test_convert_string_to_integer():
    number = convert_to_number('5')
    assert number == 5


