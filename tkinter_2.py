import tkinter as tk
from tkinter import ttk

def button_func():
    print('a button was pressed')

def print_hello():
    print('hello')
    entry_label.set('hello')

# window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry('800x500')

# ttk label
label = ttk.Label(master=window, text= 'This is a test')
label.pack()

# tk.text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry_label = tk.StringVar()
entry = ttk.Entry(master=window, textvariable=entry_label)
entry.pack()

# ttk Label "my label"
my_label = ttk.Label(master=window, text='My Label', font='Roman 12 italic')
my_label.pack()

# ttl button hello
button_hello = ttk.Button(master= window, text='Say Hello', command=print_hello)
button_hello.pack()

# ttk button
button = ttk.Button(master= window, text= 'A button', command= button_func)
button.pack()

# exercise
# add one more text label and a button with a function that prints 'hello'
# the label should say "my label" and be between the entry widget and the button

# run
window.mainloop()
# main loop will be going until the app is closed

