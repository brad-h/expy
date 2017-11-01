"""Mad Lib"""

def ex4():
    """Use a single output statement for this program
    Use string interpolation/substitution
    """

    noun = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    adverb = input('Enter an adverb: ')
    print("Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"
          .format(verb=verb, adjective=adjective, noun=noun, adverb=adverb))

def ex4a():
    """Add more inputs to the story"""

    noun = input('Enter a noun: ')
    verb = input('Enter a verb: ')
    adjective = input('Enter an adjective: ')
    adverb = input('Enter an adverb: ')
    article = input('Enter an article: ')
    print("Do you {verb} {article} {adjective} {noun} {adverb}? That's hilarious!"
          .format(verb=verb, article=article, adjective=adjective, noun=noun, adverb=adverb))

def ex4b():
    """Implement branching"""
    pass
