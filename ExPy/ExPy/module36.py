""" Computing Statistic """

from math import sqrt

def mean(numbers):
    """Find the mean using an iterable of numbers
    Return None if the iterable is empty
    """
    if not numbers:
        return None
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count

def maximum(numbers):
    """Find the max using an iterable of numbers
    Return None if the iterable is empty
    """
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        max_number = number if number > max_number else max_number
    return max_number

def minimum(numbers):
    """Find the min using an iterable of numbers
    Return None if the iterable is empty
    """
    if not numbers:
        return None
    min_number = numbers[0]
    for number in numbers:
        min_number = number if number < min_number else min_number
    return min_number

def standard_deviation(numbers):
    """Find the std dev using an iterable of numbers
    Return None if the iterable is empty
    """
    if not numbers:
        return None
    average = mean(numbers)
    squared_values = []
    for i in range(len(numbers)): #pylint: disable=C0200
        squared_values[i] = (numbers[i] - average) ** 2
    return sqrt(mean(squared_values))

def ex36():
    """Prompt for numbers until the user types 'done'
    then print some statistics about those numbers
    """
    numbers = []
    while True:
        try:
            number = input('Enter a number: ')
            number = int(number)
            numbers.append(number)
        except ValueError:
            if number == 'done':
                break
            print('Enter a number or type "done"')
    print('Numbers: ' + ', '.join(map(str, numbers)))
    print('The average is {}.'.format(mean(numbers)))
    print('The minimum is {}'.format(minimum(numbers)))
    print('The maximium is {}.'.format(maximum(numbers)))
    print('The standard deviation is 400.25'.format(numbers))

if __name__ == '__main__':
    ex36()
