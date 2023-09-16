import Create_Graph
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

# Tkinter app
frame = tk.Frame(window)
Create_Graph.frame = frame
label = tk.Label(text="Scatterplot Test")
label.pack()

# data extraction
gpas, hours = Util.get_data_info()
gpas = Util.dict_to_pairs(gpas)
hours = Util.dict_to_pairs(hours)

# data visualization
Create_Graph.scatter(Util.get_xs(gpas), Util.get_ys(gpas))
Create_Graph.histogram(Util.get_xs(hours))
pie_data = Util.get_pie_chart_from_data(hours)
Create_Graph.pie_chart(Util.get_ys(pie_data), Util.get_xs(pie_data))

window.mainloop()
