""" Numbers to Names """

I18N = {
    'EN': {
        'language': 'For English, enter "EN"',
        'prompt': 'Please enter the number of the month ',
        'responseInvalid': 'Enter a valid month',
        'outputTemplate': 'The name of the month is: ',
        'months': ('January February March April May June ' +
                   'July August September October November December').split(' ')
    },
    'ES': {
        'language': 'Para español, ingrese "ES"',
        'prompt': 'Por favor ingrese el número del mes ',
        'responseInvalid': 'Ingrese un mes válido',
        'outputTemplate': 'El nombre del mes es: ',
        'months': ('Enero Febrero Marzo Abril Mayo Junio ' +
                   'Julio Agosto Septiembre Octubre Noviembre Diciembre').split(' ')
    }
}
def ex21():
    """ Convert the number of the month to a localized month name """

    while True:
        for messages in I18N.values():
            print(messages['language'])
        language = input(': ')
        if language in I18N:
            break

    messages = I18N[language]

    while True:
        try:
            month = int(input(messages['prompt']))
            assert month > 0 and month <= 12
            month_str = messages['months'][month - 1]
            break
        except (ValueError, AssertionError):
            print(messages['responseInvalid'])

    print(messages['outputTemplate'] + month_str)



if __name__ == '__main__':
    ex21()
