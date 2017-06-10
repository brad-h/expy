"""Area of a Rectangular Room"""

from math import sqrt

CONVERSION_FACTOR = 0.09290304

def area_of_rectangle(prompt, units):
    """Separate calculations from output.
    prompt - a function that takes a message
     to prompt the user and returns a number
    units - either 'feet' or 'meters'
    """

    if units == 'feet':
        conversion_factor = CONVERSION_FACTOR
        units_converted = 'meters'
    elif units == 'meters':
        conversion_factor = 1 / CONVERSION_FACTOR
        units_converted = 'feet'
    else:
        raise ValueError("units must be either 'feet' or 'meters'")

    length = prompt('What is the length of the room in {units}? '
                    .format(units=units))
    width = prompt('What is the width of the room in {units}? '
                   .format(units=units))

    area = length * width
    area_converted = area * conversion_factor

    print('You entered dimensions of {length} {units} by {width} {units}.'
          .format(length=length, width=width, units=units))
    print('The area is')
    print('{area} square {units}'.format(area=area, units=units))
    print('{area:.3f} square {units}'
          .format(area=area_converted, units=units_converted))

def ex7():
    """Non-numeric inputs through an exception"""

    area_of_rectangle(lambda prompt: int(input(prompt)), 'feet')

def input_numeric(prompt):
    """Keep prompting the user until the number can be converted"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Value entered must be a number.')

def ex7a():
    """Do not accept non-numeric inputs"""

    area_of_rectangle(input_numeric, 'feet')

def ex7b():
    """Prompt the user for either feet or meters"""

    while True:
        units = input('Select the unit of measure, feet or meters: ')
        if units in ['feet', 'meters']:
            break

    area_of_rectangle(input_must_be_number, units)

def ex7c():
    """GUI"""

    import tkinter as tk
    from tkcomponents import create, input_stream, radio_stream, output_label
    import rx

    root = create('Area of a Rectangular Room')
    conversions = {
        'feet': (CONVERSION_FACTOR, 'meters'),
        'meters': (1 / CONVERSION_FACTOR, 'feet'),
    }
    options = [(x, x) for x in conversions.keys()]
    units = radio_stream(root, options, 0)
    length = input_stream(root, units.map('What is the length of the room in {0}?'.format), 1).map(int)
    width = input_stream(root, units.map('What is the width of the room in {0}?'.format), 2).map(int)

    def callback(unit, length, width):
        """Called every time any of the arguments changes to update the output"""
        
        (conversion_factor, units_converted) = conversions[unit]
        area = length * width
        area_converted = area * conversion_factor
        return '\n'.join([
            ('You entered dimensions of {length} {units} by {width} {units}.'
             .format(length=length, width=width, units=unit)),
             'The area is',
             ('{area} square {units}'.format(area=area, units=unit)),
             ('{area:.3f} square {units}'
              .format(area=area_converted, units=units_converted))
        ])
    
    output_label(root, rx.Observable.combine_latest(units, length, width, callback), 3)
    root.mainloop()