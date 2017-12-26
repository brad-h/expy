"""Who's in space?"""

import urllib.request
import json
import pretty

def ex47():
    """Look up who is currently in space
    Display the results in a table
    """
    with urllib.request.urlopen('http://api.open-notify.org/astros.json') as response:
        body = response.read()
    content = json.loads(body)
    print(pretty.pretty_print_table(content['people'], ['name', 'craft']))

if __name__ == '__main__':
    ex47()
