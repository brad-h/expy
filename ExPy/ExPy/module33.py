""" Magic 8 Ball """

import random

MAGIC_8_BALL_RESPONSES = [
    'Yes',
    'No',
    'Maybe',
    'Ask again later.'
]

def ex33():
    """Prompt for a question and select a random response"""
    input("What's your question? ")
    print(MAGIC_8_BALL_RESPONSES[random.randint(0, len(MAGIC_8_BALL_RESPONSES) - 1)])

if __name__ == '__main__':
    ex33()
