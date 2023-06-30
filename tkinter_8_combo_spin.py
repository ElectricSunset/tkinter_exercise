import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Combo and Spin')
window.geometry('300x300')

# Combobox
items = ('Ice cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
# combo.configure(values=items)
combo.pack()

# events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.config(text= f'Selected value: {food_string.get()}'))

combo_label = ttk.Label(window, text='a label' ,textvariable=food_string)
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(
    window, 
    from_=3, 
    to=20, 
    increment=3, 
    command= lambda : print('a arrow was pressed'),
    textvariable= spin_int)


spin.bind('<<Increment>>', lambda event: print('up'))
spin.bind('<<Decrement>>', lambda event: print('up'))
# spin['value'] = (1,2,3,4,5)
spin.pack()

# excercise:
# create a spinbox that contains the letter A B C D E
# and print the value whenever the value is decreased
spin_str = tk.StringVar(value='A')
spin2 = ttk.Spinbox(
    window,
    textvariable=spin_str
)
spin2['value'] = ('A','B','C', 'D', 'E')
spin2.bind('<<Decrement>>', lambda event: print(spin_str.get()))
spin2.pack()

# # run
window.mainloop()

# Vid time : 1.53.40 ~ 02.18.23