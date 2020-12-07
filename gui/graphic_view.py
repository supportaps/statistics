import tkinter
import datetime
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from tkcalendar import DateEntry, Calendar

from controller.backend import GetKpi


class GraphicView:

    def __init__(self, x, y):
        self.columns = GetKpi()
        self.x = x
        self.y = y
        self.column_2gh = self.columns.get_columns_2g_h()
        self.column_2gd = self.columns.get_columns_2g_d()
        self.column_3gh = self.columns.get_columns_3g_h()
        self.column_3gd = self.columns.get_columns_3g_d()
        self.column_4gh = self.columns.get_columns_4g_h()
        self.column_4gd = self.columns.get_columns_4g_d()


        self.main_window = tkinter.Tk()
        self.main_window.wm_title("Statistics")

        self.input_data_fr = tkinter.Frame(self.main_window,relief='raised', borderwidth=1, background="misty rose")
        self.input_data_fr.pack(side='left', fill='y')

        self.cal_start_lab = tkinter.Label(self.input_data_fr, text='Choose date').pack(side='top', padx=10, pady=10)
        self.cal_start_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                       foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                       selectmode='day')
        self.cal_start_ent.pack(padx=10, pady=10)

        self.cal_end_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                     foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                     selectmode='day')
        self.cal_end_ent.pack(padx=10, pady=10)



        self.var_tech = tkinter.IntVar()
        self.var_tech.set(0)
        self.choose_tech_gsm_rb = tkinter.Radiobutton(self.input_data_fr, text='GSM', variable=self.var_tech, value=1, command=self.rb_tech_call)
        self.choose_tech_gsm_rb.pack(side='top')
        self.choose_tech_wcdma_rb = tkinter.Radiobutton(self.input_data_fr, text='WCDMA', variable=self.var_tech, value=2, command=self.rb_tech_call)
        self.choose_tech_wcdma_rb.pack(side='top')
        self.choose_tech_lte_rb = tkinter.Radiobutton(self.input_data_fr, text='LTE', variable=self.var_tech, value=3, command=self.rb_tech_call)
        self.choose_tech_lte_rb.pack(side='top')

        self.var_period = tkinter.IntVar()
        self.var_period.set(0)
        self.choose_hourly_rb = tkinter.Radiobutton(self.input_data_fr, text='Hourly', variable=self.var_period, value=1, command=self.rb_tech_call)
        self.choose_hourly_rb.pack(side='top')
        self.choose_daily_rb = tkinter.Radiobutton(self.input_data_fr, text='Daily', variable=self.var_period, value=2, command=self.rb_tech_call)
        self.choose_daily_rb.pack(side='top')

        self.input_cell_name_lb = tkinter.Label(self.input_data_fr,text='CellName:')
        self.input_cell_name_lb.pack(side='top')

        self.input_cell_name_ent = tkinter.Entry(self.input_data_fr, width='22')
        self.input_cell_name_ent.pack(side='top', padx=5, pady=5)

        self.input_cell_ci_lb = tkinter.Label(self.input_data_fr, text='CellId:')
        self.input_cell_ci_lb.pack(side='top')

        self.input_cell_ci_ent = tkinter.Entry(self.input_data_fr, width='22')
        self.input_cell_ci_ent.pack(side='top', padx=5, pady=5)

        self.om_chosen1 = tkinter.StringVar()

        self.result_column_cbx = self.rb_tech_call()
        print(self.result_column_cbx)
        self.cb_items = []
        self.cb1 = ttk.Combobox(self.input_data_fr)
        self.cb1.pack()
        self.cb2 = ttk.Combobox(self.input_data_fr)
        self.cb2.pack()
        self.cb3 = ttk.Combobox(self.input_data_fr)
        self.cb3.pack()
        self.cb4 = ttk.Combobox(self.input_data_fr)
        self.cb4.pack()
        self.cb5 = ttk.Combobox(self.input_data_fr)
        self.cb5.pack()
        self.cb6 = ttk.Combobox(self.input_data_fr)
        self.cb6.pack()
        self.cb7 = ttk.Combobox(self.input_data_fr)
        self.cb7.pack()
        self.cb8 = ttk.Combobox(self.input_data_fr)
        self.cb8.pack()

        self.cb_items.append(self.cb1)
        self.cb_items.append(self.cb2)
        self.cb_items.append(self.cb3)
        self.cb_items.append(self.cb4)
        self.cb_items.append(self.cb5)
        self.cb_items.append(self.cb6)
        self.cb_items.append(self.cb7)
        self.cb_items.append(self.cb8)









        f = Figure(figsize=(8, 2), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self.main_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=0)
        tkinter.mainloop()

    def draw_plot(self):
        pass

    def rb_tech_call(self):
            rb_tech = self.var_tech.get()
            rb_period = self.var_period.get()
            
            if rb_tech == 1 and rb_period == 1:
                for cb in self.cb_items:
                  cb.configure(values=self.column_2gh)
            elif rb_tech == 1 and rb_period == 2:
                for cb in self.cb_items:
                  cb.configure(values=self.column_2gd)
            elif rb_tech == 2 and rb_period == 1:
                for cb in self.cb_items:
                  cb.configure(values=self.column_3gh)
            elif rb_tech == 2 and rb_period == 2:
                for cb in self.cb_items:
                  cb.configure(values=self.column_3gd)
            elif rb_tech == 3 and rb_period == 1:
                for cb in self.cb_items:
                    cb.configure(values=self.column_4gh)
            elif rb_tech == 3 and rb_period == 2:
                for cb in self.cb_items:
                    cb.configure(values=self.column_4gd)


