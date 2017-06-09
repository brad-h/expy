"""Printing Quotes"""

def ex3():
    """Use a single output statement, using appropriate string-escaping techniques for quotes.
    Use concatenation, do not use string interpolation or string substitution
    """

    quote = input('What is the quote? ')
    attribution = input('Who said it? ')
    print(attribution + ' says, "' + quote + '"')

EXAMPLE_DATA = [
    {'attribution': 'Obi-Wan Kenobi', 'quote': "These aren't the droids you're looking for"}
]

def ex3a(quotes):
    """Use a list of dict to print quotes"""

    for quote in quotes:
        print(quote['attribution'] + ' says, "' + quote['quote'] + '"')