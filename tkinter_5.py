import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('duh')
window.geometry('600x400')

# button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value='A button with string var')
button = ttk.Button(master= window, text='A Simple Button', command=button_func, textvariable=button_string)
button.pack()

# check button
check_var = tk.IntVar(value=10)
check1 = ttk.Checkbutton(
    master=window, 
    text= 'checkbox 1', 
    command= lambda: print(check_var.get()),
    variable= check_var,
    onvalue=10,
    offvalue=5
    )
check1.pack()

check2 = ttk.Checkbutton(
    master=window, 
    text= 'checkbox 2', 
    command= lambda: check_var.set(5)
    )
check2.pack()

# radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(master=window, 
                         text='Radio Button 1', 
                         value='radio 1', 
                         variable= radio_var,
                         command= lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(master=window, 
                         text='Radio Button 2', 
                         value= 2,
                         variable= radio_var,
                         )
radio2.pack()

# exercise 
# create another checkbutton and 2 radiobuttons
# radio button:
    # values for the buttons are A and B
    # ticking either prints the value of the checkbutton
    # ticking the radio button unchecks the checkbutton
# check button:
    # ticking the checkbutton prints the value of the radio button value
    # use tkinter var for Booleans!

exc_radio_var = tk.StringVar()
exc_check_var = tk.BooleanVar(value = False)

def radio_func():
    print(exc_check_var.get())
    exc_check_var.set(False)

def exc_check_func():
    print(exc_radio_var.get())

exc_radio_button1 = ttk.Radiobutton(master=window,
                                    text= 'Exercise Radio Button 1',
                                    value='A',
                                    variable=exc_radio_var,
                                    command=radio_func
                                    )
exc_radio_button1.pack()

exc_radio_button2 = ttk.Radiobutton(master=window,
                                    text= 'Exercise Radio Button 2',
                                    value='B',
                                    variable=exc_radio_var,
                                    command=radio_func
                                    )
exc_radio_button2.pack()

exc_check_button = ttk.Checkbutton(master=window,
                                   text= 'Exercise Check Button',
                                   variable=exc_check_var,
                                   command=exc_check_func)
exc_check_button.pack()

# run
window.mainloop()

# Vid time : 1.06.05 ~ 1.32.30