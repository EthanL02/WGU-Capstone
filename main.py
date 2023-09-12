import Util
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
import numpy as np


def on_closing():
    if messagebox.askokcancel("Quit Program", "Do you want to quit?"):
        window.quit()


# create window
window = tk.Tk()
window.state('zoomed')  # full-screen
window.protocol("WM_DELETE_WINDOW", on_closing)

# initialize Tkinter
plot.xticks(np.arange(0, 5, 1))
figure, (ax, ax2) = plot.subplots(1, 2, figsize=(8, 4))

# Tkinter app
frame = tk.Frame(window)
label = tk.Label(text="Scatterplot Test")
label.pack()

canvas = FigureCanvasTkAgg(figure, master=frame)
canvas.get_tk_widget().pack()

frame.pack()

gpas, hours = Util.get_data_info()
gpas = Util.dict_to_pairs(gpas)
hours = Util.dict_to_pairs(hours)

ax.scatter(Util.get_xs(gpas), Util.get_ys(gpas), c='black')
ax2.scatter(Util.get_xs(hours), Util.get_ys(hours), c='black')

window.mainloop()
