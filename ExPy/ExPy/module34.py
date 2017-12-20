""" Employee List Removal """

import os

DATA_FILE_PATH = 'module34.txt'

def load():
    """ Load employee list from file system and return as a list of strings """
    with open(DATA_FILE_PATH, 'r') as filehandle:
        lines = filehandle.readlines()
    return list(line.strip() for line in lines)

def save(employees):
    """ Save employee list to file system """
    with open(DATA_FILE_PATH, 'w') as filehandle:
        filehandle.write(os.linesep.join(employees) + os.linesep)

def ex34():
    """ Display the employee list
    Allow the user to specify an employee to remove from the list
    Save the modified list
    """
    employees = load()
    print('There are {} employees'.format(len(employees)))
    for employee in employees:
        print(employee)
    print()
    remove_employee = input('Enter an Employee to remove: ')
    print()
    if remove_employee in employees:
        employees.remove(remove_employee)
    else:
        print('That employee does not exist')
    save(employees)

if __name__ == '__main__':
    ex34()
