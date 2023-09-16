import Create_Graph
import Util
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import numpy as np


def on_pie_select(event):
    """
    updates the pie chart to show hours for gpas near selected gpa

    :param event:
    :return:
    """
    selected = float(pie_cbox.get())
    arr = []
    for key, val in data_dict.items():
        if round(key, 1) == selected:
            arr = arr + val

    data = Util.get_pie_chart_from_array(arr)

    pie_chart.clear()
    pie_chart.pie(Util.get_ys(data), labels=Util.get_xs(data), autopct="%1.1f%%", pctdistance=.85)
    pie_canvas.draw_idle()


def on_closing():
    if messagebox.askokcancel("Quit Program", "Do you want to quit?"):
        window.quit()


# create window
window = tk.Tk()
window.state('zoomed')  # full-screen
window.protocol("WM_DELETE_WINDOW", on_closing)
Util.window = window

# data extraction
data_dict = Util.get_data_info()
data_pair = Util.dict_to_pairs(data_dict)

# Tkinter app
# static ui
frame = tk.Frame(window)
Create_Graph.frame = frame
label = tk.Label(text="Scatterplot Test")
label.pack()
# dynamic ui
pie_cbox = ttk.Combobox(window, values=Util.get_dict_keys(data_dict), state="readonly")
pie_cbox.pack()
pie_cbox.bind("<<ComboboxSelected>>", on_pie_select)

# data visualization
Create_Graph.scatter(Util.get_xs(data_pair), Util.get_ys(data_pair))
Create_Graph.histogram(Util.get_ys(data_pair))
Create_Graph.histogram(Util.get_xs(data_pair))
pie_data = Util.get_pie_chart_from_data(data_pair, True)
pie_chart, pie_canvas = Create_Graph.pie_chart(Util.get_ys(pie_data), Util.get_xs(pie_data))

window.mainloop()
