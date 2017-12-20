"""Name Sorter"""

import os

def ex41():
    """Read a file, sort it's contents and write it to another file"""
    with open('module41.in') as infile:
        lines = infile.readlines()

    lines.sort()

    with open('module41.out', 'w') as outfile:
        header = 'Total of {} names'.format(len(lines))
        outfile.writelines([header + os.linesep, ('-' * len(header)) + os.linesep])
        outfile.writelines(lines)

if __name__ == '__main__':
    ex41()
