""" Self Checkout """

import decimal

SALES_TAX_RATE = decimal.Decimal('0.055')

def prompt_decimal(prompt):
    """ Prompt until the user provides a decimal """
    while True:
        try:
            return decimal.Decimal(input(prompt))
        except decimal.InvalidOperation:
            print('Provide a decimal')

def prompt_integer(prompt):
    """ Prompt until the user provides an integer """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Provide an integer')

def ex10():
    """ Prompt the user for 3 items/quantities and
    give them their total with sales tax.
    """

    sub_total = decimal.Decimal(0)
    for i in range(1, 4):
        price = prompt_decimal('Enter the price of item {}: '.format(i))
        quantity = prompt_integer('Enter the quantity of item {}: '.format(i))
        sub_total += price * quantity
    tax = sub_total * SALES_TAX_RATE
    total = sub_total + tax

    print('Subtotal: ${}'.format(sub_total))
    print('Tax: ${}'.format(tax))
    print('Total: ${0:.2f}'.format(total))