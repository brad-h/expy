""" Comparing Numbers """

def ex22():
    """ Prompt for three numbers
    Ensure that all numbers are different
    Display the largest of the three or exit if there are duplicates
    """

    number_of_numbers = int(input('Enter the number of numbers: '))
    numbers = set()
    maximum = None
    for _ in range(number_of_numbers):
        number = int(input('Enter a number: '))
        assert number not in numbers
        numbers.add(number)
        maximum = number if maximum is None or number > maximum else maximum
    if maximum is not None:
        print('The largest number is {}'.format(maximum))

if __name__ == '__main__':
    ex22()
