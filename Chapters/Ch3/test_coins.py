import pytest

from Chapters.Ch3 import coins
from Chapters.Ch3.coins import sum_pennies, sum_dimes, sum_quarters, sum_coins
from Chapters.Ch3.coins import sum_nickels

def test_sum_pennies():
    total = sum_pennies(user_input=50)
    assert total == 50

def test_sum_nickels():
    total = sum_nickels(user_input=5)
    assert total == 25

def test_sum_dimes():
    total = sum_dimes(user_input=2)
    assert total == 20

def test_sum_quarters():
    total = sum_quarters(user_input=3)
    assert total == 75

def test_sum_coins():

    total = coins.sum_coins(pennies='1',nickels='1',dimes='1',quarters='1')
    assert total == 41
def test_exact_dollar():
    total = coins.exact_dollar(1,1,1,1)

    assert total == 100

def test_exact_dollars():
    total = 100
    message = coins.generate_result(total)
    assert message == 'You Win'

def test_under_dollar():
    total = 60
    message = coins.generate_result(total)
    assert message == 'You Lose you are under by 40 cents'

def test_over_dollar():
    total = 125
    message = coins.generate_result(total)
    assert message == 'You lose you are over by 25 cents'