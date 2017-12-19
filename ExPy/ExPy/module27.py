""" Validating Inputs """

import os
import re

def exists(value):
    """ True and None if the value is (str) and not ''
    Otherwise False and a function to format an error message
    """
    if isinstance(value, str) and value != '':
        return True, None
    return False, 'The {} must be filled in'.format

def min_length(minimum):
    """ Return a function that tests if values are the specified minimum length """
    def callback(value):
        """Accept a value to validate, return validation results"""
        if len(value) >= minimum:
            return True, None
        return False, ('"' + str(value) + '" is not a valid {}. It is too short.').format
    return callback

def numeric(value):
    """Accept a value to validate, ensure that all characters in string are digits"""
    if str.isdigit(value):
        return True, None
    return False, 'The {} must be numeric.'.format

def pattern(regex):
    """Return a function that tests if values can be matched
    with the specified (str) (treated as a regular expression)
    """
    def callback(value):
        """Accept a value to validate, return validation results"""
        if re.fullmatch(regex, value) is not None:
            return True, None
        return False, (str(value) + ' is not a valid {}').format
    return callback

def sequence(left_validator, right_validator):
    """Given two validators, attempt to validate the first
    If successful, attempt to validate with the second
    """
    def callback(value):
        """Accept a value to validate, return validation results"""
        okay, result = left_validator(value)
        if okay:
            return right_validator(value)
        return okay, result
    return callback

def validator(dictionary):
    """Given a dictionary of keys (properties of the structure to validated)
    and values (validators for those keys)
    Assemble validation results
    """
    def callback(value):
        """Accept a value to validate, return validation results"""
        results = []
        for k, vldtr in dictionary.items():
            val = value[k] if k in value else None
            okay, result = vldtr(val)
            if not okay:
                results.append(result(k))
        if results:
            return False, os.linesep.join(results)
        return True, None
    return callback

NAME_VALIDATOR = sequence(exists, min_length(2))
VALIDATOR = validator({
    'first name': NAME_VALIDATOR,
    'last name': NAME_VALIDATOR,
    'ZIP code': numeric,
    'ID': pattern(r'^\a{2}-\d{4}')
})

def ex27():
    """Prompt for first and last name, ZIP code and Employee ID
    Display validation errors for each field
    """
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    zip_code = input('Enter the ZIP code: ')
    employee_id = input('Enter an employee ID: ')

    data = {
        'first name': first_name,
        'last name': last_name,
        'ZIP code': zip_code,
        'ID': employee_id
    }

    okay, results = VALIDATOR(data)
    if okay:
        print('There were no errors found.')
    else:
        print(results)

if __name__ == '__main__':
    ex27()
