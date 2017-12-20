"""Sorting Records"""

import csv
from prettyprinttable import pretty_print_table

ORDER = dict(zip('LPS', 'Last Name,Position,Separation Date'.split(',')))
DISPLAY_COLUMNS = 'Name,Position,Separation Date'.split(',')

def ex39():
    """Read the data set, sort and display it"""
    records = []
    with open('module39.csv') as filehandle:
        reader = csv.DictReader(filehandle)
        for row in reader:
            records.append(row)
    options = 'Sort by ' + ', '.join('{} ({})'.format(v, k) for k, v in ORDER.items()) + ': '
    while True:
        order = input(options).upper()
        if order in ORDER:
            order = ORDER[order]
            break
        print('Select a valid option')
    records.sort(key=lambda x: x[order])
    for record in records:
        record['Name'] = record['First Name'] + ' ' + record['Last Name']
    print(pretty_print_table(records, DISPLAY_COLUMNS))


if __name__ == '__main__':
    ex39()
