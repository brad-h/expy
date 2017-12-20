""" Filtering Values """

def filter_even_numbers(numbers):
    """Take a list of numbers, produce a list of even numbers"""
    for number in numbers:
        if number % 2 == 0:
            yield number

def ex38():
    """Prompt for  a list of numbers
    Filter the even numbers
    """
    user_input = input('Enter a list of numbers, seperated by spaces: ')
    numbers = [int(x) for x in user_input.split(' ')]
    evens = filter_even_numbers(numbers)
    print('The even numbers are {}.'.format(' '.join(map(str, evens))))
    

if __name__ == '__main__':
    ex38()
