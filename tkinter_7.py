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

button = ttk.Button(window, text='A Button')
button.pack()

# events
# button.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
# window.bind('<KeyPress>', lambda event: print(f'a button was pressed ({event.char})'))

# window.bind('<Motion>', get_pos)

# entry.bind('<FocusIn>', lambda event: print('entru field was selected'))
# entry.bind('<FocusOut>', lambda event: print('entru field was unselected'))

# Exercise:
# print 'Mousewheel' when the user holds down shift and uses the mousewheel while text is selected

text.bind('<Shift-MouseWheel>', lambda event: print('Mousewheel'))
# run
window.mainloop()



# Note: More Tkinter Keybinding can be googled "Tkinter Event Binding"
# pythontutorial.net/tkinter/tkinter-event-binding
# Vid time : 1.40.00 ~ 1.53.40