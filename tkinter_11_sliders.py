import tkinter as tk
from tkinter import ttk, scrolledtext

# window
window = tk.Tk()
window.title('Sliders')
window.geometry('600x400')

# # slider
# scale_float = tk.DoubleVar(value=15)
# scale = ttk.Scale(window, 
#                   command=lambda value: progress.stop(),
#                   from_ = 0,
#                   to = 25,
#                   length= 300,
#                   orient= 'vertical',
#                   variable= scale_float)
# scale.pack()

# # progress bar
# progress = ttk.Progressbar(window, 
#                            variable= scale_float, 
#                            maximum=25,
#                            orient='horizontal',
#                            mode='indeterminate',
#                            length=400)
# progress.pack()

# # progress.start(1000)

# # Scrolled Text
# scrolled_text = scrolledtext.ScrolledText(window, width= 200, height=5)
# scrolled_text.pack()

# exercise
# create a progress that is vertical, starts automatically and also show the progress as a number
# there should also be a scale slider that is affected by the progress bar

#slider
scale_num = tk.IntVar(value=50)
exercise_scale = ttk.Scale(
    window,
    command = lambda value: exercise_progress.stop(),
    from_ = 0,
    to = 100,
    length = 500,
    orient = 'vertical',
    variable= scale_num
)
exercise_scale.pack()

# exercise progress
exercise_progress = ttk.Progressbar(
    window,
    variable= scale_num,
    maximum=100,
    orient='vertical',
    mode='determinate',
    length=500
)
exercise_progress.pack()
exercise_progress.start(1000)

label = ttk.Label(window, textvariable=scale_num)
label.pack()

# run
window.mainloop()

# Vid time : 02.49.25 ~ 03.08.50
