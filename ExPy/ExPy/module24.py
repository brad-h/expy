""" Anagram Checker """

def is_anagram(first, second):
    """ Checks to see if both input strings are anagrams of eachother
    first - (str) first string
    second - (str) second string
    Returns (bool) - True if x is an anagram of y, otherwise False
    """
    assert isinstance(first, str)
    assert isinstance(second, str)
    firsts = list(first)
    firsts.sort()
    seconds = list(second)
    seconds.sort()
    return ''.join(firsts) == ''.join(seconds)

def ex24():
    """ Prompt for two strings
    Check if they are anagrams
    """

    first = input('Enter the first string: ')
    second = input('Enter the second string: ')

    anagram = is_anagram(first, second)

    if anagram:
        print('{} is an anagram of {}'.format(first, second))
    else:
        print('{} is not an anagram of {}'.format(first, second))

if __name__ == '__main__':
    ex24()
