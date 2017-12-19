""" Handling Bad Input """

import decimal

def ex29():
    """Prompt for a rate of return
    Display the length of time it will take to double the investment
    """
    while True:
        try:
            rate = decimal.Decimal(input(' What is the rate of return? '))
            assert rate != 0
            break
        except decimal.InvalidOperation:
            print("Sorry. That's not a valid input.")
        except AssertionError:
            print('Rate of return cannot be zero.')
    years = 72 / rate
    print('It will take {} years to double your initial investment.'.format(years))

if __name__ == '__main__':
    ex29()
