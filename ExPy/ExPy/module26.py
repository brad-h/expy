""" Months to Pay Off a Credit Card """

from math import log10

def prompt_float(prompt):
    """ Using the prompt, attempt to get a float from the user """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Enter a valid number')

def calculate_months_until_paid_off(balance, apr, payment):
    """ Given a balance, apr and payment
    Return the number of months that it would take to pay off the balance
    """
    daily_rate = apr / 100 / 365
    months = ((-1 / 30) *
              (log10(1 + ((balance / payment) * (1 - ((1 + daily_rate)) ** 30))) /
               log10(1 + daily_rate)))
    return int(months)

def ex26():
    """ Prompt for balance, APR, and monthly payment
    Print the number of months it will take to pay off the balance
    """
    balance = prompt_float('What is the balance? ')
    apr = prompt_float('What is the APR on the card (as a percent)? ')
    payment = prompt_float('What is the monthly payment you can make? ')

    months = calculate_months_until_paid_off(balance, apr, payment)

    print('It will take {} months to pay off this card'.format(months))

if __name__ == '__main__':
    ex26()
