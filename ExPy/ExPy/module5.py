"""Simple Math"""

class SimpleMath():
    """A class for computing simple math"""

    def __init__(self, collect):
        """Use collect, a function that takes a prompt and produces a number,
        to gather x and y and use them to produce simple math
        """

        self._x = collect('What is the first number? ')
        self._y = collect('What is the second number? ')

    def calculate(self):
        """Report simple math"""
        out = {
            'x': self._x,
            'y': self._y,
            'a': self._x + self._y,
            's': self._x - self._y,
            'm': self._x * self._y,
            'd': self._x // self._y
        }
        return ('{x} + {y} = {a}\n{x} - {y} = {s}\n{x} * {y} = {m}\n{x} / {y} = {d}'
                .format_map(out))

    def report(self):
        """Print the results of the calculate method"""
        print(self.calculate())

def ex5():
    """Values coming in from users will be strings, ensure that you convert
    them to numbers before doing the math
    Keep the inputs/outputs separate from doing the calculations
    Generate a single output statement with appropriate line breaks"""

    SimpleMath(lambda prompt: int(input(prompt))).report()

def get_number(prompt):
    """Get a number from the user"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Input must be a number')
def ex5a():
    """Ensure that inputs are numeric values"""

    SimpleMath(get_number).report()

def get_positive(prompt):
    """Get a positive number from the user"""

    while True:
        result = get_number(prompt)
        if result >= 0:
            return result
        print('Enter a non-negative number')

def ex5b():
    """Ensure that inputs are non-negative"""

    SimpleMath(get_positive).report()

def ex5c():
    """Break the program into functions that do the computations"""

    ops = [
        ('+', lambda x, y: x + y),
        ('-', lambda x, y: x - y),
        ('*', lambda x, y: x * y),
        ('/', lambda x, y: x // y)
    ]

    x_input = int(input('What is the first number? '))
    y_input = int(input('What is the second number? '))

    out = ['{x} {o} {y} = {r}'.format(x=x_input, o=o, y=y_input, r=f(x_input, y_input))
           for (o, f) in ops]
    print('\n'.join(out))

def ex5d():
    """GUI program that updates when either operand changes"""

    import rx
    from tkcomponents import create, input_stream, output_label

    # pylint: disable=no-member
    root = create('Simple Math')
    x_stream = input_stream(root, rx.Observable.just('What is the first number?'), 0)
    y_stream = input_stream(root, rx.Observable.just('What is the second number?'), 1)

    def calculate(x_str, y_str):
        """Report simple math"""
        try:
            x_int = int(x_str)
            y_int = int(y_str)
            out = {
                'x': x_int,
                'y': y_int,
                'a': x_int + y_int,
                's': x_int - y_int,
                'm': x_int * y_int,
                'd': x_int // y_int
            }
            return ('{x} + {y} = {a}\n{x} - {y} = {s}\n{x} * {y} = {m}\n{x} / {y} = {d}'
                    .format_map(out))
        except ValueError:
            return ''

    out_stream = rx.Observable.combine_latest(
        x_stream, y_stream, calculate)
    output_label(root, out_stream, 2)
    root.mainloop()
