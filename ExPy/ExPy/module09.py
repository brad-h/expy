""" Paint Calculator """

from math import ceil

GALLON_SQUARE_FEET = 350
"A gallon of paint can cover 350 sq ft"

def prompt_int(prompt):
    """ Prompt until the user provides an integer. """
    while True:
        try:
            return int(input(prompt))
        except ValueError as e:
            print('Provide an integer')

def ex9():
    """ Prompt for the length and width
    Print the number of cans needed to paint a room
    """

    length = prompt_int('What is the length of the room? ')
    width = prompt_int('What is the width of the room? ')

    total_sq_ft = length * width
    total_paint_cans = ceil(total_sq_ft / GALLON_SQUARE_FEET)

    message = (
        'You will need to purchase {} cans of paint to cover {} square feet'
        .format(total_paint_cans, total_sq_ft))
    print(message)
