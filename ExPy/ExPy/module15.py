""" Password Validation """

import csv
import bcrypt

def ex15():
    """ Prompt for username and password
    Attempt to look up in the csv file
    Inform the user if the login attempt was successful
    """

    passwords = {}
    with open('module15.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            passwords[row[0]] = row[1].encode('utf-8')

    user = input('What is the username? ')
    # abc$123 for all users in the csv
    password = input('What is the password? ').encode('utf-8')

    if user in passwords and bcrypt.checkpw(password, passwords[user]):
        print('Welcome!')
        return
    print("I don't know you")
