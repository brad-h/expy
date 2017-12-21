"""Tabular helper functions"""

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
