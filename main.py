import Util
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# initialize Tkinter
root = tk.Tk()
figure, ax = plot.subplots()

# Tkinter app
frame = tk.Frame(root)
label = tk.Label(text="Scatterplot Test")
label.pack()

canvas = FigureCanvasTkAgg(figure, master=frame)
canvas.get_tk_widget().pack()

frame.pack()

gpas, hours = Util.get_data_info()
gpas = Util.dict_to_pairs(gpas)
hours = Util.dict_to_pairs(hours)

for gpa in gpas:
    ax.scatter(gpa[0], gpa[1])
canvas.draw()

root.mainloop()
