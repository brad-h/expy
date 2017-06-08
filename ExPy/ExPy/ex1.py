"""Saying Hello"""

def ex1():
    """Keep the input, string concatenation and output separate"""
    name = input('What is your name? ')
    greeting = 'Hello, ' + name + ', nice to meet you!'
    print(greeting)

def ex1a():
    """Write a new version of the program without using any variables"""
    print(
        'Hello, ' +
        input('What is your name? ') +
        ', nice to meet you!')

def ex1b():
    """Write a version of the program that displays different greetings for
    different people"""
    pass
