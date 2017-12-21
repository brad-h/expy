"""Filtering Records"""

from datetime import datetime
import csv
from pretty import pretty_print_table


def _iso_8601(yyyy_mm_dd):
    """Given a string in YYYY-MM-DD format
    Return a Date
    """
    return datetime.strptime(yyyy_mm_dd, '%Y-%m-%d')

TODAY = _iso_8601('2017-01-01')
DISPLAY_COLUMNS = 'Name,Position,Separation Date'.split(',')

def ex40():
    """Prompt for a search string and display results that
    have that search string in either the first or the last name
    """
    records = []
    with open('employee_data_set.csv') as filehandle:
        reader = csv.DictReader(filehandle)
        for row in reader:
            records.append(row)
    for record in records:
        record['Name'] = record['First Name'] + ' ' + record['Last Name']

    prompt = 'Search by Name (N), Position (P) or filter Separation Date to last 6 months (S): '
    while True:
        option = input(prompt).upper()
        if option in 'NPS':
            break
        print('Select a valid option')
    if option in 'NP':
        criteria = input('Enter a search string: ').upper()
        if option == 'N':
            predicate = lambda x: criteria in x['Name'].upper()
        else:
            predicate = lambda x: criteria in x['Position'].upper()
    else:
        sep = 'Separation Date'
        # approximately six months
        predicate = lambda x: x[sep] and abs(TODAY - x[sep]).days <= 180
    records = list(filter(predicate, records))
    print(pretty_print_table(records, DISPLAY_COLUMNS))

if __name__ == '__main__':
    ex40()
