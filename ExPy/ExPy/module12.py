""" Computing Simple Interest """

import decimal

def ex12():
    """ Collection principal, rate, and term from the user
    Print the principal plus interest
    """

    while True:
        try:
            principal = decimal.Decimal(input('Enter the principal: '))
            break
        except decimal.InvalidOperation:
            print('Enter a valid principal')

    while True:
        try:
            rate = decimal.Decimal(input('Enter the rate of interest: '))
            break
        except decimal.InvalidOperation:
            print('Enter a valid rate of interest')

    while True:
        try:
            term = int(input('Enter the number of  years: '))
            term = decimal.Decimal(term)
            break
        except ValueError:
            print('Enter a valid number of years')

    amount = principal * (1 + ((rate / 100) * term))
    
    print('After {} years at {}% your investment will'.format(term, rate))
    print('be worth ${0:.2f}'.format(amount))