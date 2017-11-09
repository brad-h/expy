""" Determining compound interest """

import decimal
import rx
import tkcomponents

def ex13():
    """ Collect principal, rate, and term from the user
    Print the principal plus interest
    """

    while True:
        try:
            principal = decimal.Decimal(input('What is the principal amount? '))
            break
        except decimal.InvalidOperation:
            print('Enter a valid principal')

    while True:
        try:
            rate = decimal.Decimal(input('What is the rate? '))
            break
        except decimal.InvalidOperation:
            print('Enter a valid rate of interest')

    while True:
        try:
            term = int(input('What is the number of years? '))
            term = decimal.Decimal(term)
            break
        except ValueError:
            print('Enter a valid number of years')

    while True:
        try:
            frequency = int(input('What is the number of times interest is compounded per year? '))
            frequency = decimal.Decimal(frequency)
            break
        except ValueError:
            print('Enter a valid frequency')

    amount = calculate_amount(principal, rate, term, frequency)

    print('${} invested at {}% for {} years'.format(principal, rate, term))
    print('compounded {} times per year is ${}'.format(frequency, amount))

def calculate_amount(principal, rate, term, frequency):
    """ Calculate the principal plus interest given the
    principal, rate, term and frequency
    """
    return round(principal * ((1 + ((rate / 100 / frequency))) ** (frequency * term)), 2)

def ex13gui():
    """ Collect principal, rate, and term from the user
    Display the principal plus interest
    """

    #pylint: disable=E1101
    root = tkcomponents.create('Simple interest')

    principal_label = rx.Observable.just('What is the principal amount?')
    principal = tkcomponents.input_stream(root, principal_label, 0).map(decimal.Decimal)

    rate_label = rx.Observable.just('What is the rate?')
    rate = tkcomponents.input_stream(root, rate_label, 1).map(decimal.Decimal)

    term_label = rx.Observable.just('What is the number of years?')
    term = tkcomponents.input_stream(root, term_label, 2).map(int).map(decimal.Decimal)

    frequency_label = rx.Observable.just(
        'What is the number of times interest is compounded per year?')
    frequency = tkcomponents.input_stream(root, frequency_label, 3).map(int).map(decimal.Decimal)

    tkcomponents.output_label(
        root,
        rx.Observable.combine_latest(principal, rate, term, frequency, calculate_amount), 4)
    root.mainloop()
