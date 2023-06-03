import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f'X:{event.x} Y:{event.y}')

# window
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')

# widgets
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window, text='A Button')
btn.pack()

# events
btn.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
window.bind('<Motion>', get_pos)

window.bind('<KeyPress ')
# run
window.mainloop()

# Vid time : 1.40.00 ~