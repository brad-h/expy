"""Parsing a Data File"""

import decimal
import pretty

def _record(row):
    """Make a record from the csv file row"""
    last, first, salary = row.strip().split(',')
    return {
        'Last': last,
        'First': first,
        'Salary': pretty.money(decimal.Decimal(salary))
    }

def ex43():
    """Read a csv file
    Write to the console formatted
    """
    with open('module42.csv') as filehandle:
        lines = list(map(_record, filehandle))
    lines.sort(key=lambda x: decimal.Decimal(x['Salary'].replace('$', '').replace(',', '')))
    table = pretty.pretty_print_table(lines, 'Last,First,Salary'.split(','), ' ', '-')
    print(table)

if __name__ == '__main__':
    ex43()
