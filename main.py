import Create_Graph
import Util
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
    pie_chart.set_title(f"Study Hours for GPA: {selected}")
    pie_canvas.draw_idle()


def on_closing():
    if messagebox.askokcancel("Quit Program", "Do you want to quit?"):
        window.quit()


def on_gpa_entered(*args):
    try:
        gpa = float(gpa_text_var.get())
        get_study_hours(gpa)
        return True
    except ValueError:
        return False


def get_study_hours(gpa):
    gpa_label.config(text=f"Study hours for Gpa '{gpa}': {round(np.interp(gpa, ml_xdata, ml_ydata), 2)} hrs / week")


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
# pie chart combo box
pie_cbox = ttk.Combobox(window, values=Util.get_dict_keys(data_dict), state="readonly")
pie_cbox.pack(side="top", anchor="e")
pie_cbox.bind("<<ComboboxSelected>>", on_pie_select)

# gpa entry field
gpa_text_var = tk.StringVar()
gpa_entry = tk.Entry(window, textvariable=gpa_text_var)
gpa_entry.pack(side="top", anchor="w")
gpa_text_var.trace("w", on_gpa_entered)

# gpa text field
gpa_label = tk.Label(window, text="Study hours per week for Gpa '': ")
gpa_label.pack(side="top", anchor="w")

# data visualization
scatter_graph, scatter_canvas = Create_Graph.scatter(Util.get_xs(data_pair), Util.get_ys(data_pair))
ml_model = np.poly1d(np.polyfit(Util.get_xs(data_pair), Util.get_ys(data_pair), 3))
ml_line = np.linspace(np.min(Util.get_xs(data_pair)), np.max(Util.get_xs(data_pair)), int(np.max(Util.get_ys(data_pair))))
guess_line, = scatter_graph.plot(ml_line, ml_model(ml_line))
ml_xdata = guess_line.get_xdata()
ml_ydata = guess_line.get_ydata()
# np.interp(40, ml_xdata, ml_ydata)     # get suggested hours for given GPA

Create_Graph.histogram(Util.get_ys(data_pair), "Study Hours")
Create_Graph.histogram(Util.get_xs(data_pair), "GPA")
pie_data = Util.get_pie_chart_from_data(data_pair, True)
pie_chart, pie_canvas = Create_Graph.pie_chart(Util.get_ys(pie_data), Util.get_xs(pie_data))

window.mainloop()
