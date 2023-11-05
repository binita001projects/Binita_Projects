def sum_pennies(user_input):
    pennies = int(user_input)
    return pennies

def sum_nickels(user_input):
    nickels = int(user_input) * 5
    return nickels

def sum_dimes(user_input):
    dimes = int(user_input) * 10
    return dimes

def sum_quarters(user_input):
    quarters = int(user_input) * 25
    return quarters


def sum_coins(pennies,nickels,dimes,quarters):
    coins = sum([sum_pennies(pennies),
                 sum_nickels(nickels),
                 sum_dimes(dimes),
                 sum_quarters(quarters)])
    return coins


def exact_dollar(pennies,nickels,dimes,quarters):
    a_dollar = sum(sum_pennies(pennies),
                   sum_nickels(nickels),
                   sum_quarters(quarters),
                   sum_dimes(dimes)
                   )
    return a_dollar


def generate_result(total):
    if total == 100:
        return 'You Win'

    if total < 100:
        under = 100 - total
        return f'You Lose you are under by {under} cents'

    if total > 100:
        over = total - 100
        return f'You lose you are over by {over} cents'