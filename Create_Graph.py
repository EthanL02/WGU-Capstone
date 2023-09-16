import tkinter as tk
import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

frame = None
size = (5, 5)


def scatter(xax, yax):
    figure, grp = plot.subplots(figsize=size)
    canvas = FigureCanvasTkAgg(figure, master=frame)
    frame.pack()

    grp.plot(xax, yax, 'k.', ms=5)
    grp.set_title("GPA - Study Hours Correlation")
    grp.set_xlabel("GPA")
    grp.set_ylabel("Study Hours")
    canvas.get_tk_widget().pack(side=tk.LEFT)

    return grp, canvas


def histogram(xax, title):
    figure, grp = plot.subplots(figsize=size)
    canvas = FigureCanvasTkAgg(figure, master=frame)
    frame.pack()

    grp.hist(xax)
    grp.set_title(title)
    grp.set_xlabel(title)
    grp.set_ylabel("Count")
    canvas.get_tk_widget().pack(side=tk.LEFT)

    return grp, canvas


def pie_chart(sizes, labels):
    figure, grp = plot.subplots(1)
    grp.pie(sizes, labels=labels, autopct="%1.1f%%", pctdistance=.85)
    canvas = FigureCanvasTkAgg(figure, master=frame)
    frame.pack()

    grp.set_title("Study Hours for GPA")

    canvas.get_tk_widget().pack(side=tk.LEFT)

    return grp, canvas
