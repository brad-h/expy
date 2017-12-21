"""Tabular helper functions"""

import decimal
import os

def pretty_print_table(records, columns, row_sep=' | ', header_sep='-|-'):
    """Given an iterable of dicts with key and value both of type str
    And an iterable of strings that are keys in those dict
    Return a Pretty-print table as str
    """
    column_max = {}

    header = []
    seperator = []
    for column in columns:
        col_len = len(column)
        maximum = max(len(r[column]) for r in records if column in r and r[column] is not None)
        maximum = maximum if maximum > col_len else col_len
        column_max[column] = maximum
        header.append(column.ljust(maximum))
        seperator.append('-' * maximum)

    rows = [row_sep.join(header), header_sep.join(seperator)]

    for record in records:
        row = []
        for column in columns:
            field = record[column] if column in record and record[column] is not None else ''
            row.append(field.ljust(column_max[column]))
        rows.append(row_sep.join(row))
    return os.linesep.join(rows)

def money(dec):
    """Given a decimal number
    Return a string formatted in USD with commas
    """
    # Because you really ought to be using decimal floats for money
    assert isinstance(dec, decimal.Decimal)
    dec_str = str(round(dec, 2))
    dollars, cents = dec_str.split('.')
    # reverse dollars and start peeling off groups of three numbers
    dollars = dollars[::-1]
    dollar_parts = []
    while len(dollars) > 3:
        dollar_parts.append(dollars[:3][::-1])
        dollars = dollars[3:]
    dollar_parts.append(dollars[::-1])
    dollar_parts.reverse()
    return '${}.{}'.format(','.join(dollar_parts), cents)
