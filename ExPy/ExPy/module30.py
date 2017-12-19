""" Multiplication Table """

def ex30():
    """Generate a multiplication table"""
    for left in range(13):
        for right in range(13):
            print('{} X {} = {}'.format(left, right, left * right))

if __name__ == '__main__':
    ex30()
