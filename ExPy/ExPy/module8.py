""" Pizza Party """
import math

# the book is a little ambiguous on
# where this is supposed to come from
NUMBER_OF_SLICES = 8

def ex8():
    """ Prompt the user for number of people and number of pizzas
    Print the number of slices each person will get and the number
    of leftover pieces
    """
    number_of_people = int(input('How many people? '))
    number_of_pizzas = int(input('How many pizzas do you have? '))

    total_slices = NUMBER_OF_SLICES * number_of_pizzas
    pieces_per_person = total_slices // number_of_people
    leftover_pieces = total_slices % number_of_people
    if pieces_per_person == 1:
        piece = 'piece'
    else:
        piece = 'pieces'

    print('{} people with {} pizzas'.format(number_of_people, number_of_pizzas))
    print('Each person gets {} {} of pizza.'.format(pieces_per_person, piece))
    print('There are {} leftover pieces'.format(leftover_pieces))

def ex8c():
    """ Prompt the user for the number of people and how many slices for each person
    Print the number of pizzas that should be ordered
    """
    number_of_people = int(input('How many people? '))
    pieces_per_person = int(input('How many pieces for each person? '))

    total_slices = number_of_people * pieces_per_person
    number_of_pizzas = math.ceil(total_slices / NUMBER_OF_SLICES)

    print('{} people with {} pizzas'.format(number_of_people, number_of_pizzas))
    print('There are {} pizzas'.format(number_of_pizzas))
