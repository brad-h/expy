"""Counting the number of characters"""

def ex2():
    """ Be sure the output contains the original string.
    Use a single output statement to construct the output.
    Use a built-in function of the programming language to determine the length of the string.
    """

    prompt = input('What is the input string? ')
    print(prompt + ' has ' + str(len(prompt)) + ' characters.')

def ex2a():
    """If the user enters nothing, state that the user must enter something into the program."""

    while True:
        prompt = input('What is the input string? ')
        if prompt == '':
            print('You must enter something into the program.')
        else:
            break
    print(prompt + ' has ' + str(len(prompt)) + ' characters.')

def ex2b():
    """implement this program using a GUI
    Update the output string every time the user presses a key
    """

    import tkinter as tk
    root = tk.Tk()
    root.title('Count the number of characters')

    input_var = tk.StringVar()
    tk.Label(root, text='What is the input string?').grid(row=0)
    tk.Entry(root, textvariable=input_var).grid(row=0, column=1)
    output_var = tk.StringVar()
    tk.Label(root, textvariable=output_var).grid(row=1)
    def callback(*_):
        """Called every time the input Entry is changed to update the output Label"""

        prompt = input_var.get()
        output = prompt + ' has ' + str(len(prompt)) + ' characters.'
        output_var.set(output)

    input_var.trace('w', callback)

    root.mainloop()
