import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print('a button was pressed')
    print(entry_string.get())

# entah kenapa kalo pake outer_func pas di run dia nggak langsung call
def outer_func(parameter):
    def inner_func():
        print('a button was pressed')
        print(parameter.get())
    return inner_func

# window
window = tk.Tk()
window.title('buttons, functions and arguments')
window.geometry('600x400')

# widgets
entry_string = tk.StringVar(value='test')
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text='button', command = lambda: button_func(entry_string)) # bisa ganti lambda dengan outer func
button.pack()

#run
window.mainloop()

# Vid time : 1.32.30 ~ 1.40.00