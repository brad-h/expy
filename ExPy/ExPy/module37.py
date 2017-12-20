"""Password Generator
TERRIBLE IDEA! DO NOT USE THIS UNDER ANY CIRCUMSTANCES
"""

# probably insufficient for this purpose, but that shouldn't matter since DON'T USE IT
import random

ALPHA = (''.join(map(chr, range(ord('a'), ord('z') + 1))) +
         ''.join(map(chr, range(ord('A'), ord('Z') + 1))))
DIGITS = ''.join(str(x) for x in range(10))
SPECIALS = ''.join(
    x for x in map(chr, range(256)) if not str.isalnum(x) and str.isprintable(x))
LEET = dict(zip('aeio', '4310'))

def _knuth_shuffle(chars):
    """Given a string, shuffle the characters randomly"""
    # probably wrong, again don't use any of this
    char_list = list(chars)
    for i in reversed(range(1, len(chars))):
        j = random.randint(0, i)
        temp = char_list[i]
        char_list[i] = char_list[j]
        char_list[j] = temp
    return ''.join(char_list)

def ex37():
    """Prompt for minimum password length
    Number of special characters
    Number of... numbers
    Display the generated password
    """
    min_length = int(input("What's the minimum length? "))
    special_count = int(input('How many special characters? '))
    number_count = int(input('How many numbers? '))
    print('Your password is')
    # going to do the bare minimum length, because why shouldn't all of this be terrible
    real_minimum_length = max((min_length, special_count + number_count))
    specials = [SPECIALS[random.randrange(0, len(SPECIALS))] for _ in range(special_count)]
    numbers = [DIGITS[random.randrange(0, len(DIGITS))] for _ in range(number_count)]
    remainder = real_minimum_length - (special_count + number_count)
    alpha = [ALPHA[random.randrange(0, len(ALPHA))] for _ in range(remainder)]
    alpha = [LEET[x] if x.lower() in LEET and random.random() < .5 else x for x in list(alpha)]
    password_chars = specials + numbers + alpha
    print(_knuth_shuffle(password_chars))


if __name__ == '__main__':
    ex37()
