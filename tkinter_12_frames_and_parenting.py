import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Frames and parenting')
window.geometry('600x400')

# frame
frame = ttk.Frame(window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side= 'left')

# master setting
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text= 'button in frame')
button.pack()

# example
label2 = ttk.Label(frame, text = 'Label outside frame')
label2.pack(side='left')

# ecercise
# create another frame with a label, a button and an entry and place it to the right
# of the other widgets

frame2 = ttk.Frame(window, width=100, height=200, borderwidth=10, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side= 'right')

# master setting
label3 = ttk.Label(frame2, text = 'Label in frame')
label3.pack()

button2 = ttk.Button(frame2, text= 'button in frame')
button2.pack()

entry = ttk.Entry(frame2)
entry.pack()

# run
window.mainloop()