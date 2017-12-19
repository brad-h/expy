""" Troubleshooting Car Issues """

QUESTIONS = [
    {
        'question': 'Is the car silent when you turn the key?',
        'answers': {
            'Yes': 1,
            'No': 2
        }
    },
    {
        'question': 'Are the battery terminals corroded?',
        'answers': {
            'Yes': 'Clean terminals and try starting again.',
            'No': 'Replace cables and try again.'
        }
    },
    {
        'question': 'Does the car making a clicking noise?',
        'answers': {
            'Yes': 'Replace the battery.',
            'No': 3
        }
    },
    {
        'question': 'Does the car crank up but fail to start?',
        'answers': {
            'Yes': 'Check spark plug connections',
            'No': 4
        }
    },
    {
        'question': 'Does the engine start and then die?',
        'answers': {
            'Yes': 5,
            'No': 'Unknown'
        }
    },
    {
        'question': 'Does your car have fuel injection?',
        'answers': {
            'Yes': 'Get it in for service.',
            'No': 'Check to ensure the chcoke is opening and closing.'
        }
    }
]

def ex23():
    """ Use QUESTIONS to help a user diagnose car issues """
    # QUESTIONS[0] is the "root" question
    # start from the root and follow the answers through the QUESTIONS list
    question = QUESTIONS[0]

    while True:
        print(question['question'])
        answer = input(', '.join(question['answers'].keys()) + ': ')
        answers = question['answers']
        if answer in answers:
            if isinstance(answers[answer], int):
                question = QUESTIONS[answers[answer]]
            else:
                # reached a diagnosis; print and exit
                print(answers[answer])
                break
        else:
            print('Please enter a valid selection')

if __name__ == '__main__':
    ex23()
