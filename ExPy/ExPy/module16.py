""" Legal Driving Age """

def ex16():
    """ Prompt for age
    Display whether the age is of driving age
    """

    while True:
        try:
            age = int(input('What is your age? '))
            if age < 0:
                raise ValueError()
            break
        except ValueError:
            print('Enter a valid age')
    
    if age < 16:
        print('You are not old enough to legally drive')
    else:
        print('You are old enough to legally drive')