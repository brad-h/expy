""" Picking a Winner """

import random

def ex35():
    """Prompt the user for names until they given a blank input
    Select one of those names and declare them the winner
    """
    names = []
    while True:
        name = input('Enter a name: ')
        if name == '':
            break
        names.append(name)
    winner = names[random.randint(0, len(names) - 1)]
    print('The winner is... {}.'.format(winner))

if __name__ == '__main__':
    ex35()
