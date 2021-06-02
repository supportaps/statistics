from __future__ import unicode_literals
import matplotlib as mpl
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from gui.scroll import Scroll
import matplotlib.style
import matplotlib.dates as mdates
import numpy


class Graphic:

    def __init__(self, frame1):
        self.x = []
        self.y = []
        self.frame1 = frame1

        mpl.style.use('dark_background')
        mpl.rcParams['figure.raise_window'] = False
        mpl.rcParams['figure.frameon'] = True
        mpl.rcParams['figure.dpi'] = 80
        mpl.rcParams['figure.figsize'] = [13, 40]
        mpl.rcParams['figure.edgecolor'] = 'blue'
        mpl.rcParams['figure.facecolor'] = '#474645'
        mpl.rcParams['axes.grid'] = True
        mpl.rcParams['grid.color'] = 'gray'
        mpl.rcParams['grid.linestyle'] = '-.'

        self.fig1 = Figure()

        self.ax1 = self.fig1.add_subplot(8, 1, 1)
        self.ax1.plot('0000-00-00', 20, alpha=0.2)
        self.ax1.tick_params(axis='x', labelrotation=45)
        self.ax2 = self.fig1.add_subplot(8, 1, 2)
        self.ax2.plot(2.2, 2)
        self.ax2.plot('0000-00-00', 20, alpha=0.2)
        self.ax2.tick_params(axis='x', labelrotation=45)
        self.ax3 = self.fig1.add_subplot(813)
        self.ax3.plot(2.2, 2)
        self.ax3.set_ylabel(' ')
        self.ax3.plot('0000-00-00', 20, alpha=0.2)
        self.ax3.tick_params(axis='x', labelrotation=45)
        self.ax4 = self.fig1.add_subplot(814)
        self.ax4.plot(2.2, 2)
        self.ax4.plot('0000-00-00', 20, alpha=0.2)
        self.ax4.tick_params(axis='x', labelrotation=45)
        self.ax5 = self.fig1.add_subplot(815)
        self.ax5.plot(1, 1)
        self.ax5.plot('0000-00-00', 20, alpha=0.2)
        self.ax5.tick_params(axis='x', labelrotation=45)
        self.ax6 = self.fig1.add_subplot(816)
        self.ax6.plot(2.2, 2)
        self.ax6.plot('0000-00-00', 20, alpha=0.2)
        self.ax6.tick_params(axis='x', labelrotation=45)
        self.ax7 = self.fig1.add_subplot(817)
        self.ax7.plot(2.2, 2)
        self.ax7.plot('0000-00-00', 20, alpha=0.2)
        self.ax7.tick_params(axis='x', labelrotation=45)
        self.ax8 = self.fig1.add_subplot(818)
        self.ax8.plot(2.2, 2)
        self.ax8.plot('0000-00-00', 20, alpha=0.2)
        self.ax8.tick_params(axis='x', labelrotation=45)

        self.fig1.tight_layout()

        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.frame1)
        vertical_scroll = Scroll(self.canvas1, self.frame1, self.fig1)
        self.canvas1.get_tk_widget().itemconfigure(self.fig1, width=300, height=300)

        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side='right')

        self.canvas1.get_tk_widget().bind("<Configure>", self.canvas_dimen)
        self.canvas1.get_tk_widget().update_idletasks()

        self.canvas1.mpl_connect('resize_event', self.resize)

        print("BACKEND: ", mpl.rcParams)
        print("alpha", self.fig1.get_alpha())
        print("axes", self.fig1.get_axes)
        print("agg_filter", self.fig1.get_agg_filter())
        print("dpi", self.fig1.get_dpi())
        print("gid", self.fig1.get_gid())

        print("animated", self.fig1.get_animated())
        print("children", self.fig1.get_children())
        print("clip box", self.fig1.get_clip_box())
        print("clip on", self.fig1.get_clip_on())
        print("clipp path", self.fig1.get_clip_path())
        print("constrained layot", self.fig1.get_constrained_layout())

        print("constr layot pads", self.fig1.get_constrained_layout_pads())
        print("get contains", self.fig1.get_contains)

        print("artist", self.fig1.get_default_bbox_extra_artists())
        print("edgecolor", self.fig1.get_edgecolor())
        print("facecolor", self.fig1.get_facecolor())

        print("get figheight", self.fig1.get_figheight())
        print("getfigurre", self.fig1.get_figure())
        print("get_figwidth", self.fig1.get_figwidth())
        print("frame on", self.fig1.get_frameon)
        print("layout", self.fig1.get_in_layout())
        print("facecolor", self.fig1.get_facecolor())

        print("label", self.fig1.get_label())
        print("picker", self.fig1.get_picker())
        print("rasterised", self.fig1.get_rasterized())
        print("inch", self.fig1.get_size_inches())
        print("effect", self.fig1.get_path_effects())
        print("sketch", self.fig1.get_sketch_params())

        print("snap", self.fig1.get_snap())
        print("snap", self.fig1.get_snap())

        print("transform", self.fig1.get_transform())
        print("affine", self.fig1.get_transformed_clip_path_and_affine())
        print("url", self.fig1.get_url())

        print("visible", self.fig1.get_visible())
        print("extent", self.fig1.get_window_extent())
        print("zorder", self.fig1.get_zorder())
        print("extent bbox", self.fig1._get_clipping_extent_bbox())
        print("get dpi", self.fig1._get_dpi)

        print("state", self.fig1.__getstate__())

    def canvas_dimen(self, event):
        canvas_width = event.width
        print("canvas_width: ", canvas_width)

    def resize(self, event):

        self.fig1.tight_layout()
        self.fig1.set_dpi(80)
        self.fig1.set_size_inches(13, 40)
        fig_weight = self.fig1.get_figwidth()
        fig_height = self.fig1.get_figheight()
        dpi = self.fig1.get_dpi()
        print(fig_weight, fig_height, dpi)
        # self.canvas1.get_tk_widget().config(width=fig_weight*dpi, height=fig_height*dpi)
        x1, y1, x2, y2 = self.canvas1.get_tk_widget().bbox("all")
        print(x1, y1, x2, y2)
        copy = self.canvas1.copy_from_bbox(self.canvas1.get_tk_widget().bbox("all"))
        print(copy)
        self.canvas1.get_tk_widget()

    def update_figure_label(self, cell):

        self.fig1.suptitle(
            "BSC: " + cell.controller + " ,Cell Name: " + cell.name + " ,LAC: " + cell.lac + " ,CI: " + cell.cell_id,
            fontsize=16, color='blue', x=0.001, y=.99, horizontalalignment='left')

    def set_tick(self, ax, x):
        elements = len(x)
        interval = 2
        if elements >= 720:
            interval = 7

        ax.tick_params(axis='x', labelrotation=45)
        fmt_major_date = mdates.DayLocator(bymonthday=None, interval=interval, tz=None)
        ax.xaxis.set_major_locator(fmt_major_date)
        fmt_minor_date = mdates.DayLocator()
        ax.xaxis.set_minor_locator(fmt_minor_date)

    def calculate_rms(self, y):

        rms = numpy.std(y)
        return numpy.round(rms, 2)

    def calculate_avg(self, y):
        average = numpy.mean(y)
        return numpy.round(average, 2)

    def calculate_maximum(self, y):
        maximum = numpy.max(y)
        return maximum

    def calculate_minimum(self, y):
        minimum = numpy.min(y)
        return minimum

    def calculate_second_maximum(self, y):

        y.sort()
        return y[-2]

    def calculate_third_maximum(self, y):

        y.sort()
        return y[-3]

    def update_plot_graphik1(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:
                print(y_value)
                self.y.append(y_value)

        print(self.x, "\n", self.y)
        self.ax1.clear()
        self.ax1.plot(self.x, self.y, color='red', marker='o', alpha=0.5, linewidth=2.5, markersize=3)
        self.ax1.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.2)

        self.ax1.set_ylabel(kpi_name)

        self.set_tick(self.ax1, self.x)

        self.ax1.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax1.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik2(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax2.clear()
        self.ax2.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax2.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax2.set_ylabel(kpi_name)

        self.set_tick(self.ax2, self.x)

        self.ax2.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax2.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik3(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax3.clear()
        self.ax3.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax3.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax3.set_ylabel(kpi_name)


        self.set_tick(self.ax3, self.x)

        self.ax3.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax3.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik4(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax4.clear()
        self.ax4.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax4.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax4.set_ylabel(kpi_name)

        self.set_tick(self.ax4, self.x)

        self.ax4.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax4.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik5(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax5.clear()
        self.ax5.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax5.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax5.set_ylabel(kpi_name)

        self.set_tick(self.ax5, self.x)

        self.ax5.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax5.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik6(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax6.clear()
        self.ax6.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax6.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax6.set_ylabel(kpi_name)

        self.set_tick(self.ax6, self.x)

        self.ax6.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax6.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik7(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax7.clear()
        self.ax7.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax7.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax7.set_ylabel(kpi_name)

        self.set_tick(self.ax7, self.x)

        self.ax7.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax7.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()

    def update_plot_graphik8(self, result_data_graphic, n, kpi_name):

        self.x.clear()
        self.y.clear()

        for item in range(len(result_data_graphic)):
            if 'hourly' in n:
                date_point = result_data_graphic[item][0]
                hour = result_data_graphic[item][1]
                y_value = result_data_graphic[item][2]
                date_point = date_point.replace(hour=hour)
            else:
                date_point = result_data_graphic[item][0]
                y_value = result_data_graphic[item][1]

            self.x.append(date_point)
            if y_value is None:

                self.y.append(0)
            else:

                self.y.append(y_value)

        self.ax8.clear()
        self.ax8.plot(self.x, self.y, color='red', marker='o', alpha=0.1)
        self.ax8.fill_between(self.x, 0, self.y, facecolor='red', alpha=0.5)

        self.ax8.set_ylabel(kpi_name)

        self.set_tick(self.ax8, self.x)

        self.ax8.text(0.99, 0.99,
                      f"avg = {self.calculate_avg(self.y)}\nrms = {self.calculate_rms(self.y)}\nmax1 = {self.calculate_maximum(self.y)}\nmax2 = {self.calculate_second_maximum(self.y)}\nmax3 = {self.calculate_third_maximum(self.y)}\nmin = {self.calculate_minimum(self.y)}",
                      horizontalalignment='right',
                      verticalalignment='top',
                      transform=self.ax8.transAxes)

        self.canvas1.flush_events()
        self.canvas1.draw()
