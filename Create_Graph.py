import tkinter as tk

import matplotlib.pyplot as plot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


frame = None
size = (5, 5)


def scatter(xax, yax):
    figure, grp = plot.subplots(figsize=size)
    canvas = FigureCanvasTkAgg(figure, master=frame)
    frame.pack()

    grp.plot(xax, yax, 'k.', ms=5)
    canvas.get_tk_widget().pack(side=tk.LEFT)

    return grp


def histogram(xax):
    figure, grp = plot.subplots(figsize=size)
    canvas = FigureCanvasTkAgg(figure, master=frame)
    frame.pack()

    grp.hist(xax)
    canvas.get_tk_widget().pack(side=tk.LEFT)

    return grp


def pie_chart(sizes, labels):
    figure, grp = plot.subplots(figsize=size)
    canvas = FigureCanvasTkAgg(figure, master=frame)
    frame.pack()

    grp.pie(sizes, labels=labels)
    canvas.get_tk_widget().pack(side=tk.LEFT)

    return grp
