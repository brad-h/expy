""" Conversion Calculator """

import urllib.request
import json
import decimal

def ex11():
    """ Conversion Calcuator """
    response = urllib.request.urlopen('http://api.fixer.io/latest?base=USD')
    body = json.loads(response.read())

    rates = body['rates']
    rates['USD'] = 1.0

    while True:
        prompt = 'Enter the currency you would like to convert from: '
        currency_from = input(prompt)
        if currency_from in rates:
            break
        print('Enter a valid currency')
    while True:
        try:
            prompt = 'How many {} are you exchanging? '.format(currency_from)
            amount_from = decimal.Decimal(input(prompt))
            break
        except decimal.InvalidOperation:
            print('Enter a valid amount')
    while True:
        prompt = 'Enter the currency you would like to convert to: '
        currency_to = input(prompt)
        if currency_to in rates:
            break
        print('Enter a valid currency')

    rate_from = decimal.Decimal(rates[currency_from])
    rate_to = decimal.Decimal(rates[currency_to])
    exchange_rate = rate_from / rate_to
    amount_to = round(amount_from * exchange_rate, 2)

    print('{0:.2f} {1} at an exchange rate of {2} is'
          .format(amount_from, currency_from, exchange_rate))
    print('{0:.2f} {1}'.format(amount_to, currency_to))
