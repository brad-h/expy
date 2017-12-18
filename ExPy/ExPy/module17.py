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
            alcohol = decimal.Decimal(input('Enter alcohol consumed (in ounces): '))
            break
        except decimal.InvalidOperation:
            print('Enter a valid amount')

    while True:
        sex = input('Enter sex (M/F): ').upper()
        if sex in ALCOHOL_DISTRIBUTION_RATIO:
            ratio = ALCOHOL_DISTRIBUTION_RATIO[sex]
            break

    while True:
        try:
            weight = int(input('Enter weight (in pounds): '))
            weight = decimal.Decimal(weight)
            break
        except ValueError:
            print('Enter a valid amount')

    while True:
        try:
            height = int(input('Enter the number of hours since the last drink: '))
            height = decimal.Decimal(height)
            break
        except ValueError:
            print('Enter valid hours')
    bac = (alcohol * decimal.Decimal('5.14') / weight * ratio) - decimal.Decimal('0.15') * height
    print('bac: {}'.format(bac))
