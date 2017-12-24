"""Word Frequency Finder"""

import re
import collections

def ex46():
    """Produce a tally of word frequencies from words.txt"""
    with open('module46.txt') as filehandle:
        contents = filehandle.read()
    words = re.findall(r'\w+', contents)
    counter = collections.Counter(words)
    max_word_len = max(map(len, counter.keys()))
    for word, frequency in counter.most_common():
        print((word + ':').ljust(max_word_len + 1), '*' * frequency)

if __name__ == '__main__':
    ex46()
