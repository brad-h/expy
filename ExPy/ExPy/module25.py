""" Password Strength Indicator """

import rx
import tkcomponents

VERY_WEAK = 0
WEAK = 1
STRONG = 2
VERY_STRONG = 3

def password_validator(password):
    """Given a password
    Return either:
        VERY_WEAK, WEAK, STRONG or VERY_STRONG
    """
    if len(password) < 8:
        if str.isdigit(password):
            return VERY_WEAK
        if str.isalpha(password):
            return WEAK
    else:
        if any(map(str.isalpha, password)) and any(map(str.isdigit, password)):
            if any(map(lambda x: not str.isalnum(x) and str.isprintable(x), password)):
                return VERY_STRONG
            return STRONG

PASSWORD_STRENGTH_DESCRIPTION = {
    VERY_WEAK: 'very weak',
    WEAK: 'weak',
    STRONG: 'strong',
    VERY_STRONG: 'very strong'
}

def password_strength_description(password_strength):
    """Given a password strength: VERY_STRONG, WEAK, STRONG or VERY_STRONG
    Return a string to be displayed to the user
    """
    if password_strength in PASSWORD_STRENGTH_DESCRIPTION:
        return PASSWORD_STRENGTH_DESCRIPTION[password_strength]
    return 'unknown strength'

def ex25():
    """ Prompt for a password
    Print the strength of the password
    """
    password = input('Password: ')
    strength_code = password_validator(password)
    strength = password_strength_description(strength_code)
    print("The password '{}' is a {} password".format(password, strength))

def ex25gui():
    """ GUI version of ex 25 """
    root = tkcomponents.create('Password Strength Validator')
    #pylint: disable=E1101
    passwords = tkcomponents.input_stream(root, rx.Observable.just('Password'), 0)
    def callback(password):
        """Given a password, return the output"""
        strength_code = password_validator(password)
        strength = password_strength_description(strength_code)
        return "The password '{}' is a {} password".format(password, strength)
    tkcomponents.output_label(root, passwords.map(callback), 1)
    root.mainloop()

if __name__ == '__main__':
    ex25gui()
