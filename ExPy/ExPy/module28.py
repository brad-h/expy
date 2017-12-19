""" Adding Numbers """

def ex28():
    """Prompt user for numbers 5 times and show the sum"""
    counter = int(input('Enter how many numbers to sum: '))
    sum = 0
    loop = True
    while loop:
        try:
            sum += int(input('Enter a number: '))
        except ValueError:
            print('Enter valid numbers')
        else:
            counter -= 1
        loop = counter > 0
    print('The total is {}.'.format(sum))

if __name__ == '__main__':
    ex28()
