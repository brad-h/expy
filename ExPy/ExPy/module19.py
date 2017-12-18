""" BMI Calculator """

def calculate_bmi(weight, height):
    """ Given weight (pounds), height (inches)
    Return BMI
    """
    return (weight / (height * height)) * 703.

def bmi_recommendation(bmi):
    """Given a BMI, return a recommendation"""
    if bmi < 18.5:
        return 'You are underweight. You should see a doctor.'
    elif bmi < 25:
        return 'You are within the ideal weight range.'
    return 'You are overweight. You should see a doctor.'

def prompt_float(prompt):
    """ Given a specified prompt, return a float """

    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Enter a valid number')

def ex19():
    """ Prompt for weight and height
    Print BMI and BMI range
    """

    weight = prompt_float('Enter weight in pounds(lbs): ')
    height = prompt_float('Enter height in inches: ')

    bmi = calculate_bmi(weight, height)
    recommendation = bmi_recommendation(bmi)

    print('Your BMI is {}'.format(bmi))
    print(recommendation)


if __name__ == '__main__':
    ex19()
