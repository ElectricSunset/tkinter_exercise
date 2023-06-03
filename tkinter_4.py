import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('300x500')

# tkinter variable
string_var = tk.StringVar(value = 'start value')

# widgets
label = ttk.Label(master=window, text='Label', textvariable=string_var)
label.pack()

entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()

button = ttk.Button(master=window, text='Button', command=button_func)
button.pack()

# exercise
# create 2 entry fields and 1 labels, they should all be connected via a StringVar
# set a start value of 'test'

# Exercise Widgets
exercise_string_var = tk.StringVar(value= 'test')

label2 = ttk.Label(master=window, text='Exercise Label', textvariable=exercise_string_var)
label2.pack()

entry2 = ttk.Entry(master=window, textvariable=exercise_string_var)
entry2.pack()

entry3 = ttk.Entry(master=window, textvariable=exercise_string_var)
entry3.pack()


# run
window.mainloop()

# Vid time : 54.30 ~ 1.06.05