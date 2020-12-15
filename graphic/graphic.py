from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
import tkinter
import datetime
from tkinter import ttk
import matplotlib.pyplot as plt


class Graphic:

    def __init__(self, frame):
        self.x = []
        self.y = []

        self.fig1 = Figure()
        self.ax1 = self.fig1.add_subplot(211)
        self.ax1.plot(1, 1)


        self.ax2 = self.fig1.add_subplot(212)
        self.ax2.plot(2.2, 2)



        self.canvas1 = FigureCanvasTkAgg(self.fig1, frame)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0)




    def update_plot_graphik1(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        #self.fig1.clear()
        self.ax1.clear()

        #self.a = self.f.add_subplot(111)
        #self.ax1 = self.fig.add_subplot(211)
        self.ax1.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()


    def update_plot_graphik2(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)


        #self.fig2.clear()
        self.ax2.clear()
        self.ax2.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()