""" Validating Inputs """

import os
import re
import rx
import tkcomponents

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
EMPLOYEE_ID_VALIDATOR = pattern(r'^[a-zA-Z]{2}-[0-9]{4}$')
VALIDATOR = validator({
    'first name': NAME_VALIDATOR,
    'last name': NAME_VALIDATOR,
    'ZIP code': numeric,
    'ID': EMPLOYEE_ID_VALIDATOR
})

def validate_input(first_name, last_name, zip_code, employee_id):
    """first_name - (str)
    last_name - (str)
    zip_code - (str)
    employee_id - (str)
    Return a pair (bool, None|str)
    None if True
    str error message if False
    """
    data = {
        'first name': first_name,
        'last name': last_name,
        'ZIP code': zip_code,
        'ID': employee_id
    }

    okay, results = VALIDATOR(data)
    return 'There were no errors found.' if okay else results

def ex27():
    """Prompt for first and last name, ZIP code and Employee ID
    Display validation errors for each field
    """
    first_name = input('Enter the first name: ')
    last_name = input('Enter the last name: ')
    zip_code = input('Enter the ZIP code: ')
    employee_id = input('Enter an employee ID: ')

    output = validate_input(first_name, last_name, zip_code, employee_id)
    print(output)

def _display_result(field, result):
    """Accept a field name and a validation result pair
    Display an error if it exists
    """
    okay, error = result
    return '' if okay else error(field)

def _validated_input(root, label, row, vldtr):
    """Create a Validated Input component
    root - a Tk root
    label - a str to be used as the input label
    row - the row in the window
    vldtr - the validator to use for the input
    Return a stream of input values
    """
    #pylint: disable=E1101
    label = rx.Observable.just(label)
    values = tkcomponents.input_stream(root, label, row)
    results = rx.Observable.combine_latest(label, values.map(vldtr), _display_result)
    tkcomponents.output_label(root, results, row + 1, fg='red')
    return values

def ex27gui():
    """GUI version of ex 27"""
    #pylint: disable=E1101
    root = tkcomponents.create('Validating Inputs')

    first_names = _validated_input(root, 'First Name', 0, NAME_VALIDATOR)
    last_names = _validated_input(root, 'Last Name', 2, NAME_VALIDATOR)
    zip_codes = _validated_input(root, 'ZIP code', 4, numeric)
    employee_ids = _validated_input(root, 'Employee ID', 6, EMPLOYEE_ID_VALIDATOR)

    validation_results = rx.Observable.combine_latest(first_names,
                                                      last_names,
                                                      zip_codes,
                                                      employee_ids,
                                                      validate_input)
    tkcomponents.output_label(root, validation_results, 8)

    root.mainloop()

if __name__ == '__main__':
    ex27gui()
