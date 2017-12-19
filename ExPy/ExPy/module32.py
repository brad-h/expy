""" Guess the Number Game """

import random

DIFFICULTIES = {
    1: 10,
    2: 100,
    3: 1000
}

def ex32():
    """Prompt the user to guess a number
    If they guess right, then congratulate them
    Otherwise, tell them if they guessed above or below and
    give them another change to guess
    """
    print("Let's play Guess the Number.")
    play = True
    while play:
        difficulty = int(input('Pick a difficulty level (1, 2, or 3): '))
        assert difficulty in DIFFICULTIES
        difficulty_max = DIFFICULTIES[difficulty]
        number_to_guess = random.randint(1, difficulty_max)
        previous_guesses = set()
        guesses = 0
        guess = None

        while guess != number_to_guess:
            try:
                if guess is None:
                    guess = int(input("I have my number. What's your guess? "))
                elif guess < number_to_guess:
                    guess = int(input('Too low. Guess again: '))
                else:
                    guess = int(input('Too high. Guess again: '))

                if guess in previous_guesses:
                    print("You've tried this number already")
                else:
                    previous_guesses.add(guess)

            except ValueError:
                print('Enter a number')
            guesses += 1

        print('You got it in {} guesses!'.format(guesses))
        if guesses > 6:
            print('Better luck next time.')
        elif guesses > 4:
            print('You can do better than that.')
        elif guesses > 1:
            print('Most impressive.')
        else:
            print("You're a mind reader!")
        play = input('Play again? ').upper() == 'Y'

if __name__ == '__main__':
    ex32()
