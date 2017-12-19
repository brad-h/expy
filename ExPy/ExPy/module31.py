""" Karvonen Heart Rate """

from tkinter import HORIZONTAL
import rx
import tkcomponents as tkc

def karvonen_heart_rate(age, resting_heart_rate, intensity):
    """ Compute a target heart rate given:
    age (int) - in years
    resting_heart_rate (int) - beats per minute
    intensity (float) - as a percentage
    """
    intensity /= 100
    target_heart_rate = (((220 - age) - resting_heart_rate) * intensity) + resting_heart_rate
    return int(round(target_heart_rate))

def ex31():
    """Prompt for age resting heart rate
    Display a table of target heart rates
    """
    age = int(input('Age: '))
    resting_heart_rate = int(input('Resting heart rate: '))

    print('Resting Pulse: {}   Age: {}'.format(resting_heart_rate, age))
    print('Intensity    | Rate')
    print('-------------|--------')
    for intensity in range(55, 100, 5):
        target_heart_rate = karvonen_heart_rate(age, resting_heart_rate, intensity)
        print('{0:12s} | {1} bpm'.format(str(intensity) + '%', target_heart_rate))

def ex31gui():
    """Karvonen GUI"""
    #pylint: disable=E1101
    root = tkc.create('Karvonen Heart Rate')
    ages = tkc.input_stream(root, rx.Observable.just('Age'), 0)
    resting_heart_rates = tkc.input_stream(root, rx.Observable.just('Resting Heart Rate'), 1)
    intensities = tkc.scale_stream(root, rx.Observable.just('Intensity'), 2, orient=HORIZONTAL)

    def callback(age, resting_heart_rate, intensity):
        """ merge input streams to produce target heart rate output """
        try:
            age = int(age)
        except ValueError:
            return 'Age must be a number'
        try:
            resting_heart_rate = int(resting_heart_rate)
        except ValueError:
            return 'Resting heart rate must be a number'
        try:
            intensity = int(intensity)
        except ValueError:
            # not sure how this could happen, but w/e
            return 'Intensity must be a number'
        target_heart_rate = karvonen_heart_rate(age, resting_heart_rate, intensity)
        return '{} bpm'.format(target_heart_rate)

    target_heart_rates = rx.Observable.combine_latest(ages, resting_heart_rates,
                                                      intensities, callback)
    tkc.output_label(root, target_heart_rates, 3)
    root.mainloop()

if __name__ == '__main__':
    ex31gui()
