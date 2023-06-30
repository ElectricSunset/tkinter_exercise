import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Menu')
window.geometry('600x400')

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label='New', command= lambda: print('New File'))
file_menu.add_command(label='Open', command= lambda: print('Open File'))
file_menu.add_separator()
menu.add_cascade(label = 'File', menu= file_menu)

# another sub menu
help_menu = tk.Menu(menu, tearoff= False)
help_menu.add_command(label='Help entry', command= lambda: print(help_check_string.get()))
 
help_check_string = tk.StringVar(value="off")
help_menu.add_checkbutton(label='check', onvalue= 'on', offvalue='off', variable=help_check_string)

menu.add_cascade(label='Help', menu=help_menu)

# add another menu to the main menu, this one should have a sub menu
# try to read the website below and add a submenu
# docs: https://www.tutorialspoint.com/python/tk_menu.htm

# exercise menu
option_menu = tk.Menu(menu, tearoff= False)

menu.add_cascade(label='Options', menu= option_menu)

# exercise sub menu
video_menu = tk.Menu(option_menu, tearoff=False)
video_menu.add_command(label='60 Hz', command= lambda: print('set to 60 Hz'))
video_menu.add_command(label='120 Hz', command= lambda: print('set to 120 Hz'))

option_menu.add_cascade(label='Video Refresh Rate', menu=video_menu)

# menu button
menu_button = ttk.Menubutton(window, text = ' Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff= False)
button_sub_menu.add_command(label='entry 1', command= lambda: print('test 1'))
button_sub_menu.add_checkbutton(label='check 1')
# menu_button.configure(menu=button_sub_menu)
menu_button['menu'] = button_sub_menu

window.configure(menu=menu)

# run
window.mainloop()

# Vid time :  03.27.55 ~ 03.46.55
