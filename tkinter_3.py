import  tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    entry_text = entry.get()

    # update the label
    # label.configure(text='some other text') -> identical
    label['text'] = entry_text
    entry['state'] = 'disabled'
    button['state'] = 'disabled'
    refresh_button['state'] = 'enabled'

def refresh_button_func():
    label['text'] = 'Some Text'
    entry.configure(state='enabled')
    button['state'] = 'enabled'
    refresh_button['state'] = 'disabled' 

# window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('300x200')

# widgets
label = ttk.Label(master=window, text='Some Text')
label.pack()

entry = ttk. Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text='The Button', command=button_func)
button.pack()

# exercise
# add another button that changes text back to 'some text' and that enables entry

refresh_button = ttk.Button(master=window, text='Refresh', command=refresh_button_func, state='disabled')
refresh_button.pack()

# run
window.mainloop()

# vid time
# ~54.30