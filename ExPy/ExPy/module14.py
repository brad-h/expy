""" Tax Calculator """

import decimal

WI_SALES_TAX_RATE = decimal.Decimal('0.055')

def ex14():
    """ Prompt the user for an amount and a state
    Apply sales tax of 5.5% for Wisconsin residents
    Display the amount owed
    """

    amount = decimal.Decimal(input('What is the order amount? '))
    state = input('What is the state? ').upper()

    if state in {'WI', 'WISCONSIN'}:
        print('The subtotal is ${0:.2f}'.format(amount))
        tax = amount * WI_SALES_TAX_RATE
        print('The tax is ${0:.2f}'.format(tax))
        amount += tax
    
    print('The total is ${0:.2f}'.format(amount))