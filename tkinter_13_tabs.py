import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Tab Widget')
window.geometry('600x400')

# Notebook widget
notebook = ttk.Notebook(window)

# Tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text= ' Text in tab 1')
label1.pack()
button1 = ttk.Button(tab1, text='Button in tab 1')
button1.pack()

# Tab 2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text= ' Text in tab 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

# exercise
# add another tab with 2 buttons and one label inside

tab3 = ttk.Frame(notebook)

button3a = ttk.Button(tab3, text='Button in tab 3a')
button3a.pack()

button3b = ttk.Button(tab3, text='Button in tab 3b')
button3b.pack()

label3 = ttk.Label(tab3, text= ' Text in tab 3')
label3.pack()

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.add(tab3, text='Tab 3')
notebook.pack()

# run
window.mainloop()

# Vid time :  ~ 03.27.55