""" Blood Alcohol Calculator """

import decimal

ALCOHOL_DISTRIBUTION_RATIO = {
    'M': decimal.Decimal('0.73'),
    'F': decimal.Decimal('0.66')
}

def ex17():
    """ Prompt for alcohol consumed, sex, weight, and hours since last drink
    Display the Blood Alcohol Content level
    """

    while True:
        try:
            a = decimal.Decimal(input('Enter alcohol consumed (in ounces): '))
            break
        except decimal.InvalidOperation:
            print('Enter a valid amount')

    while True:
        sex = input('Enter sex (M/F): ').upper()
        if sex in ALCOHOL_DISTRIBUTION_RATIO:
            r = ALCOHOL_DISTRIBUTION_RATIO[sex]
            break
    
    while True:
        try:
            w = int(input('Enter weight (in pounds): '))
            w = decimal.Decimal(w)
            break
        except ValueError:
            print('Enter a valid amount')
    
    while True:
        try:
            h = int(input('Enter the number of hours since the last drink: '))
            h = decimal.Decimal(h)
            break
        except ValueError:
            print('Enter valid hours')
    bac = (a * decimal.Decimal('5.14') / w * r) - decimal.Decimal('0.15') * h
    print('bac: {}'.format(bac))