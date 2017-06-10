"""A library of components for tk with rx"""

import tkinter as tk
import rx

def create(title):
    """Create a Tk root
    title - a title for the application
    """

    assert isinstance(title, str)

    root = tk.Tk()
    root.title = title
    rx.concurrency.TkinterScheduler(root)
    return root

def input_stream(root, prompt, row):
    """Creates input component with label given as prompt on a given row,
    root - a Tk root
    prompt - an observable of string values
    row - the row of the tk window to place the radio buttons
    returns observable of input values
    """

    assert isinstance(root, tk.Tk)
    assert isinstance(prompt, rx.Observable)
    assert isinstance(row, int)

    output_label(root, prompt, row)
    subject = rx.subjects.Subject()
    string_var = tk.StringVar()
    string_var.trace('w', lambda *args: subject.on_next(string_var.get()))
    tk.Entry(root, textvariable=string_var).grid(row=row, column=1)
    return subject

def radio_stream(root, options, row, default=''):
    """Produce a stream of user selections on a radio button
    root - a Tk root
    options - a list of pairs, [(value, text)]
      value - the value that is generated when selected
      text - the text displayed to the user
    row - the row of the tk window to place the radio buttons
    """

    assert isinstance(root, tk.Tk)
    assert isinstance(options, list)
    assert isinstance(row, int)

    string_var = tk.StringVar()
    string_var.set(default)
    subject = rx.subjects.Subject()
    subject.on_next(default)
    column = 0
    for (value, text) in options:
        radio_button = tk.Radiobutton(
            root,
            text=text,
            variable=string_var,
            value=value,
            command=lambda: subject.on_next(string_var.get()))
        radio_button.grid(row=row, column=column)
        column += 1
    return subject

def output_label(root, stream, row):
    """Used to display a stream of values to the user
    root - a Tk root
    stream - a stream of values to be displayed
    row = the row of the tk window to place the output
    """

    assert isinstance(root, tk.Tk)
    assert isinstance(stream, rx.Observable)

    string_var = tk.StringVar()
    string_var.set('')
    stream.subscribe(string_var.set)
    tk.Label(root, textvariable=string_var).grid(row=row)
