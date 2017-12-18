""" Temperature Converter """

def fahrenheit_to_celsius(fahrenheit):
    """ Given Fahrenheit, convert to Celsius """
    celsius = (fahrenheit - 32.) * (5. / 9.)
    return celsius

def celsius_to_fahrenheit(celsius):
    """ Given Celsius, convert to Fahrenheit """
    fahrenheit = (celsius * (9.  / 5.)) + 32.
    return fahrenheit

SCALES = {
    'C': ('Fahrenheit', 'Celsius', fahrenheit_to_celsius),
    'F': ('Celsius', 'Fahrenheit', celsius_to_fahrenheit)
}

def ex18():
    """ Prompt for scale (Celsius vs Fahrenheit) and temperature
    Print the converted temperature
    """
    print('Print C to convert from Fahrenheit to Celsius.')
    print('Press F to convert from Celsius to Fahrenheit')

    while True:
        scale = input('Your choice: ').upper()
        if scale in SCALES:
            from_scale, to_scale, conversion = SCALES[scale]
            break

    while True:
        try:
            temperature = float(input('Please enter the temperature in {}: '.format(from_scale)))
            break
        except ValueError:
            print('Enter a valid number')

    converted = conversion(temperature)

    print('The temperature in {} is {}'.format(to_scale, converted))


if __name__ == '__main__':
    ex18()
