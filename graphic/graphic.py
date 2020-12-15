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

        self.ax1 = self.fig1.add_subplot(811)
        self.ax1.plot(1, 1)
        self.ax2 = self.fig1.add_subplot(812)
        self.ax2.plot(2.2, 2)
        self.ax3 = self.fig1.add_subplot(813)
        self.ax3.plot(2.2, 2)
        self.ax4 = self.fig1.add_subplot(814)
        self.ax4.plot(2.2, 2)
        self.ax5 = self.fig1.add_subplot(815)
        self.ax5.plot(1, 1)
        self.ax6 = self.fig1.add_subplot(816)
        self.ax6.plot(2.2, 2)
        self.ax7 = self.fig1.add_subplot(817)
        self.ax7.plot(2.2, 2)
        self.ax8 = self.fig1.add_subplot(818)
        self.ax8.plot(2.2, 2)



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

        self.ax1.clear()
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

        self.ax2.clear()
        self.ax2.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik3(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        self.ax3.clear()
        self.ax3.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik4(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        self.ax4.clear()
        self.ax4.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik5(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        self.ax5.clear()
        self.ax5.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik6(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        self.ax6.clear()
        self.ax6.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik7(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        self.ax7.clear()
        self.ax7.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik8(self, result_data_graphic):
        print(result_data_graphic)
        self.x.clear()
        self.y.clear()
        for item in result_data_graphic:
            for d in item:
                if type(d) == datetime.datetime:
                    self.x.append(d)
                elif type(d) == float or type(d) == int:
                    self.y.append(d)

        self.ax8.clear()
        self.ax8.plot(self.x, self.y)
        self.canvas1.flush_events()
        self.canvas1.draw()
