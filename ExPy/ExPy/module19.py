""" BMI Calculator """

import rx
import tkcomponents

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

def ex19gui():
    """ GUI version of BMI """
    root = tkcomponents.create('BMI')
    options = {
        'Imperial': ('pounds(lbs)', 'inches'),
        'Metric': ('kilograms(kg)', 'centimeters(cm)')
    }
    systems = tkcomponents.radio_stream(root, [(x, x) for x in options], 0, default='Imperial')
    weight_labels = systems.map(lambda x: 'Enter weight in {}'.format(options[x][0]))
    weights = tkcomponents.input_stream(root, weight_labels, 1)
    height_labels = systems.map(lambda x: 'Enter height in {}'.format(options[x][1]))
    heights = tkcomponents.input_stream(root, height_labels, 2)

    def callback(system, weight, height):
        """Given a system, a weight, and a height
        Calculate BMI"""
        try:
            weight = float(weight)
        except ValueError:
            return (False, 'Enter a valid weight')
        try:
            height = float(height)
        except ValueError:
            return (False, 'Enter a valid height')
        if system == 'Imperial':
            return (True, calculate_bmi(weight, height))
        weight_lbs = weight * 2.20462
        height_in = height * 0.393701
        return (True, calculate_bmi(weight_lbs, height_in))

    #pylint: disable=E1101
    bmis = rx.Observable.combine_latest(systems, weights, heights, callback)
    def bmi_output(bmi):
        """ If the BMI could successfully be converted then display it
        Otherwise display the error
        """
        okay, value = bmi
        if okay:
            return 'Your BMI is {}'.format(value)
        return value

    tkcomponents.output_label(root, bmis.map(bmi_output), 3)

    def bmi_recommendation_output(bmi):
        """ If the BMI could successfully be converted then display
        the recommendation
        Otherwise display the error
        """
        okay, value = bmi
        if okay:
            return bmi_recommendation(value)
        return ''
    tkcomponents.output_label(root, bmis.map(bmi_recommendation_output), 4)
    root.mainloop()

if __name__ == '__main__':
    ex19gui()
