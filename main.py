import Util
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit Program", "Do you want to quit?"):
        window.quit()


# create window
window = tk.Tk()
window.state('zoomed')  # full-screen
window.protocol("WM_DELETE_WINDOW", on_closing)

# initialize Tkinter
figure, ax = plot.subplots()

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

for gpa in gpas:
    ax.scatter(gpa[1], gpa[0])
canvas.draw()

window.mainloop()
