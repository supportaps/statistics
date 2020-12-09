import tkinter
import datetime
from tkinter import ttk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from tkcalendar import DateEntry, Calendar

from config.settings import Settings
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
        self.n1 = self.columns.get_n1()
        self.n2 = self.columns.get_n2()
        self.n3 = self.columns.get_n3()
        self.n4 = self.columns.get_n4()
        self.n5 = self.columns.get_n5()
        self.n6 = self.columns.get_n6()


        self.main_window = tkinter.Tk()
        self.main_window.wm_title("Statistics")

        self.input_data_fr = tkinter.Frame(self.main_window,relief='raised', borderwidth=1, background="misty rose")
        self.input_data_fr.pack(side='left', fill='y')


        self.cal_start_lab = tkinter.Label(self.input_data_fr, text='Choose date').pack(side='top', padx=10, pady=10)
        self.cal_start_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                       foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                       selectmode='day')
        self.cal_start_ent.bind("<<DateEntrySelected>>", self.get_date_start)
        self.cal_start_ent.pack(padx=10, pady=10)

        self.end_chosen_date = tkinter.StringVar()
        self.cal_end_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                     foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                     selectmode='day')
        self.cal_end_ent.bind("<<DateEntrySelected>>", self.get_date_end)
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

        self.cell_name_bt = tkinter.Button(self.input_data_fr,
                                                 text='OK', command=self.get_cell_name_from_ent)
        self.cell_name_bt.pack(side='top')

        self.input_lac_tac_lb = tkinter.Label(self.input_data_fr, text='LAC(TAC):')
        self.input_lac_tac_lb.pack(side='top')


        self.input_lac_tac_ent = tkinter.Entry(self.input_data_fr,width='22')
        self.input_lac_tac_ent.pack(side='top', padx=5, pady=5)


        self.input_cell_ci_lb = tkinter.Label(self.input_data_fr, text='CellId:')
        self.input_cell_ci_lb.pack(side='top')


        self.input_cell_ci_ent = tkinter.Entry(self.input_data_fr,width='22')
        self.input_cell_ci_ent.pack(side='top', padx=5, pady=5)

        self.lac_ci_bt = tkinter.Button(self.input_data_fr,
                                        text='OK', command=self.get_gui_vars)
        self.lac_ci_bt.pack(side='top')

        self.kpi = []
        self.kpi_chosen1 = tkinter.StringVar()
        self.kpi_chosen2 = tkinter.StringVar()
        self.kpi_chosen3 = tkinter.StringVar()
        self.kpi_chosen4 = tkinter.StringVar()
        self.kpi_chosen5 = tkinter.StringVar()
        self.kpi_chosen6 = tkinter.StringVar()
        self.kpi_chosen7 = tkinter.StringVar()
        self.kpi_chosen8 = tkinter.StringVar()


        self.result_column_cbx = self.rb_tech_call()
        print(self.result_column_cbx)
        self.cb_items = []
        self.cb1 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen1)
        self.cb1.pack()

        self.cb2 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen2)
        self.cb2.pack()
        self.cb3 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen3)
        self.cb3.pack()
        self.cb4 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen4)
        self.cb4.pack()
        self.cb5 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen5)
        self.cb5.pack()
        self.cb6 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen6)
        self.cb6.pack()
        self.cb7 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen7)
        self.cb7.pack()
        self.cb8 = ttk.Combobox(self.input_data_fr, textvariable=self.kpi_chosen8)
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
                else:
                    return self.n1
            elif rb_tech == 1 and rb_period == 2:
                for cb in self.cb_items:
                    cb.configure(values=self.column_2gd)
                else:
                    return self.n2
            elif rb_tech == 2 and rb_period == 1:
                for cb in self.cb_items:
                    cb.configure(values=self.column_3gh)
                else:
                    return self.n3
            elif rb_tech == 2 and rb_period == 2:
                for cb in self.cb_items:
                    cb.configure(values=self.column_3gd)
                else:
                    return self.n4
            elif rb_tech == 3 and rb_period == 1:
                for cb in self.cb_items:
                    cb.configure(values=self.column_4gh)
                else:
                    return self.n5
            elif rb_tech == 3 and rb_period == 2:
                for cb in self.cb_items:
                    cb.configure(values=self.column_4gd)
                else:
                    return self.n6

    def get_date_start(self,e):
        return self.cal_start_ent.get_date().strftime("%d-%b-%y")

    def get_date_end(self,e):
        return self.cal_end_ent.get_date().strftime("%d-%b-%y")

    def get_cell_name_from_ent(self):
        return  self.input_cell_name_ent.get()

    def get_lac_ci(self):
        ci = self.input_cell_ci_ent.get()
        lac_tac = self.input_lac_tac_ent.get()
        return ci,lac_tac

    def get_gui_vars(self):

        self.kpi.append(self.kpi_chosen1.get())
        self.kpi.append(self.kpi_chosen2.get())
        self.kpi.append(self.kpi_chosen3.get())
        self.kpi.append(self.kpi_chosen4.get())
        self.kpi.append(self.kpi_chosen5.get())
        self.kpi.append(self.kpi_chosen6.get())
        self.kpi.append(self.kpi_chosen7.get())
        self.kpi.append(self.kpi_chosen8.get())

        start = self.cal_start_ent.get_date().strftime("%d-%b-%y")
        end = self.cal_end_ent.get_date().strftime("%d-%b-%y")
        kpi_list = self.kpi
        n = self.rb_tech_call()
        ci = self.input_cell_ci_ent.get()
        lac_tac = self.input_lac_tac_ent.get()
        settings = Settings(start,end,kpi_list,n, lac_tac, ci)
        settings.get_gui_variables()

