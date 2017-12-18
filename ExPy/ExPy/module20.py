""" Multistate Sales Tax Calculator """

import os
from decimal import Decimal
from decimal import InvalidOperation

def prompt_decimal(prompt):
    """ Using the prompt, attempt to get a decimal from the user """
    while True:
        try:
            return Decimal(input(prompt))
        except InvalidOperation:
            print('Enter a valid number')

def dollar(amount):
    """ Given an amount as a number
    Return a string formatted as a dollar amount
    """
    amount = round(amount, 2)
    return '${0:0.2f}'.format(amount)

STATE_RATES = {
    'ILLINOIS': Decimal('0.08'),
    'WISCONSIN': Decimal('0.05')
}

WISCONSIN_RATES = {
    'EAU CLAIRE': Decimal('0.005'),
    'DUNN': Decimal('0.004')
}

def ex20():
    """ Prompt for the order amount and state
    If the state is Wisconsin, prompt for the county
    Print the sales tax and total amount
    """

    amount = prompt_decimal('What is the order amount? ')
    state = input('What state do you live in? ')
    if state.upper() in STATE_RATES:
        rate = STATE_RATES[state.upper()]
    else:
        rate = Decimal(0)

    if state.upper() == 'WISCONSIN':
        county = input('What county do you live in? ')
        if county.upper() in WISCONSIN_RATES:
            rate += WISCONSIN_RATES[county.upper()]

    tax = amount * rate
    total = tax + amount

    output = os.linesep.join([
        'The tax is {}'.format(dollar(tax)),
        'The total is {}'.format(dollar(total))])
    print(output)

if __name__ == '__main__':
    ex20()
