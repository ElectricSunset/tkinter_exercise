import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title('Canvas')
window.geometry('500x500')

# canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()

# canvas.create_rectangle((50,20,100,200), fill='red', width=10, dash=(4,2,1,1), outline='green')
# canvas.create_oval((200,0,300,100), fill='green')
# canvas.create_arc(
#     (200,0,300,100), 
#     fill='red', 
#     start=45, 
#     extent = 180, 
#     style = tk.CHORD, 
#     outline='red', 
#     width=10)

# canvas.create_line((0,0,100,150), fill='blue')
# canvas.create_polygon((0,0,100,200,300,50, 150,-50), fill='gray')

# canvas.create_text((100,200), text= 'this is some text', fill='green', width=10)

# canvas.create_window((150,100), window= ttk.Button(window, text= 'this is text in canvas'))

# Exercise
# Use Event binding to create a basic paint app (draw a line where the mouse at)



# def track(event):
#     x= event.x
#     y= event.y
#     canvas.bind('<Button>', lambda x,y: draw(x,y))

#     return event.x, event.y

# def draw(event,x,y):
#     canvas.create_oval((x-brush_size/2,
#                     y-brush_size/2,
#                     x+brush_size/2,
#                     y+brush_size/2), 
#                     fill='red')


# brush_size = 4
# canvas.bind('<Motion>', track)

def track(event):
    x= event.x
    y= event.y

    return event.x, event.y

def draw(event):
    print(canvas.bind('<Motion>', track))
    # canvas.create_oval((x-brush_size/2,
    #                 y-brush_size/2,
    #                 x+brush_size/2,
    #                 y+brush_size/2), 
    #                 fill='red')


brush_size = 4
canvas.bind('<Button>', draw)

# run
window.mainloop()

# Vid time : 18.23.15 ~