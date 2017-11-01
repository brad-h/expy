"""Retirement Calculator"""

from datetime import date

def prompt(difference_check):
    """Calculate the year you can retire
    difference_check - a function that takes a number and returns boolean,
    the number provided is the difference between current age and retirement age
    """

    age = int(input('What is your age? '))
    retirement_age = int(input('At what age would you like to retire? '))
    current_year = date.today().year

    difference = retirement_age - age
    if difference_check(difference):
        future_year = current_year + difference
        print("You have {difference} years left until you can retire."
              .format(difference=difference))
        print("It's {current_year}, so you can retire in {future_year}."
              .format(current_year=current_year, future_year=future_year))
    else:
        print('You can retire now!')

def ex6():
    """Do not handle negative numbers"""

    prompt(lambda _: True)

def ex6a():
    """Handle negative numbers"""

    prompt(lambda x: x > 0)
