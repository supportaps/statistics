import tkinter
import datetime
from tkinter import ttk

from tkcalendar import DateEntry, Calendar

from controller.backend import GetKpi
from graphic.graphic import Graphic
from kpi.kpi import Kpi
from model.cell import Cell


class Gui:

    def __init__(self):

        self.kpi_data = GetKpi()

        self.column_2gh = self.kpi_data.get_columns_2g_h()
        self.column_2gd = self.kpi_data.get_columns_2g_d()
        self.column_3gh = self.kpi_data.get_columns_3g_h()
        self.column_3gd = self.kpi_data.get_columns_3g_d()
        self.column_4gh = self.kpi_data.get_columns_4g_h()
        self.column_4gd = self.kpi_data.get_columns_4g_d()
        self.n1 = self.kpi_data.get_n1()
        self.n2 = self.kpi_data.get_n2()
        self.n3 = self.kpi_data.get_n3()
        self.n4 = self.kpi_data.get_n4()
        self.n5 = self.kpi_data.get_n5()
        self.n6 = self.kpi_data.get_n6()

        self.main_window = tkinter.Tk()

        self.main_window.wm_title("Statistics")

        self.input_data_fr = tkinter.Frame(self.main_window, relief='raised', borderwidth=1, background="misty rose")
        self.input_data_fr.pack(side='left', fill='y')

        self.cal_start_lab = tkinter.Label(self.input_data_fr, text='Choose date').pack(side='top', padx=10, pady=10)
        self.cal_start_chosen_date_var = tkinter.StringVar()
        self.cal_start_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                       foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                       selectmode='day')
        self.cal_start_ent.bind("<<DateEntrySelected>>", self.set_date_start)
        self.cal_start_ent.pack(padx=10, pady=10)

        self.cal_end_chosen_date_var = tkinter.StringVar()
        self.cal_end_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                     foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                     selectmode='day')
        self.cal_end_ent.bind("<<DateEntrySelected>>", self.set_date_end)
        self.cal_end_ent.pack(padx=10, pady=10)


        self.var_tech = tkinter.IntVar()
        self.var_tech.set(0)
        self.choose_tech_gsm_rb = tkinter.Radiobutton(self.input_data_fr, text='GSM', variable=self.var_tech, value=1,
                                                      command=self.rb_tech_call)
        self.choose_tech_gsm_rb.pack(side='top')
        self.choose_tech_wcdma_rb = tkinter.Radiobutton(self.input_data_fr, text='WCDMA', variable=self.var_tech,
                                                        value=2, command=self.rb_tech_call)
        self.choose_tech_wcdma_rb.pack(side='top')
        self.choose_tech_lte_rb = tkinter.Radiobutton(self.input_data_fr, text='LTE', variable=self.var_tech, value=3,
                                                      command=self.rb_tech_call)
        self.choose_tech_lte_rb.pack(side='top')

        self.var_period = tkinter.IntVar()
        self.var_period.set(0)
        self.choose_hourly_rb = tkinter.Radiobutton(self.input_data_fr, text='Hourly', variable=self.var_period,
                                                    value=1, command=self.rb_tech_call)
        self.choose_hourly_rb.pack(side='top')
        self.choose_daily_rb = tkinter.Radiobutton(self.input_data_fr, text='Daily', variable=self.var_period, value=2,
                                                   command=self.rb_tech_call)
        self.choose_daily_rb.pack(side='top')

        self.input_cell_name_lb = tkinter.Label(self.input_data_fr, text='CellName:')
        self.input_cell_name_lb.pack(side='top')

        self.input_cell_name_ent = tkinter.Entry(self.input_data_fr, width='22')
        self.input_cell_name_ent.pack(side='top', padx=5, pady=5)

        self.cell_name_bt = tkinter.Button(self.input_data_fr,
                                           text='OK', command=self.get_cell_name_from_ent)
        self.cell_name_bt.pack(side='top')

        self.input_lac_tac_lb = tkinter.Label(self.input_data_fr, text='LAC(TAC):')
        self.input_lac_tac_lb.pack(side='top')

        self.input_lac_tac_ent = tkinter.Entry(self.input_data_fr, width='22')
        self.input_lac_tac_ent.pack(side='top', padx=5, pady=5)

        self.input_cell_ci_lb = tkinter.Label(self.input_data_fr, text='CellId:')
        self.input_cell_ci_lb.pack(side='top')

        self.input_cell_ci_ent = tkinter.Entry(self.input_data_fr, width='22')
        self.input_cell_ci_ent.pack(side='top', padx=5, pady=5)

        self.lac_ci_bt = tkinter.Button(self.input_data_fr,
                                        text='OK', command=self.get_data_for_graphics)
        self.lac_ci_bt.pack(side='top')

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

        #graph1 = self.graphic.draw_plot(self.main_window)
        self.graphic = Graphic(self.main_window)

        self.main_window.mainloop()

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

    def set_date_start(self, event):
        start = self.cal_start_ent.get_date().strftime("%d-%b-%y")
        print(start)
        self.cal_start_chosen_date_var.set(start)
        print(self.cal_start_chosen_date_var.get())

    def set_date_end(self, event):
        end = self.cal_end_ent.get_date().strftime("%d-%b-%y")
        print(end)
        self.cal_end_chosen_date_var.set(end)
        print(self.cal_end_chosen_date_var.get())

    def get_cell_name_from_ent(self):
        return self.input_cell_name_ent.get()

    def get_ci(self):
        ci = self.input_cell_ci_ent.get()
        return ci

    def get_lac_tac(self):
        lac_tac = self.input_lac_tac_ent.get()
        return lac_tac

    def get_name(self):
        n = self.rb_tech_call()
        return n

    def get_kpi_columns(self):
        kpi = []
        kpi.append(self.kpi_chosen1.get())
        kpi.append(self.kpi_chosen2.get())
        kpi.append(self.kpi_chosen3.get())
        kpi.append(self.kpi_chosen4.get())
        kpi.append(self.kpi_chosen5.get())
        kpi.append(self.kpi_chosen6.get())
        kpi.append(self.kpi_chosen7.get())
        kpi.append(self.kpi_chosen8.get())
        return kpi

    def get_data_for_graphics(self):

        cell = Cell('', self.get_ci(), self.get_lac_tac())
        kpi_item = Kpi(self.get_kpi_columns(), self.cal_start_chosen_date_var.get(), self.cal_end_chosen_date_var.get())
        n = self.get_name()

        result_for_graphic1 = self.kpi_data.get_data_for_graphic1(cell, kpi_item, n)
        result_for_graphic2 = self.kpi_data.get_data_for_graphic2(cell, kpi_item, n)
        result_for_graphic3 = self.kpi_data.get_data_for_graphic3(cell, kpi_item, n)
        result_for_graphic4 = self.kpi_data.get_data_for_graphic4(cell, kpi_item, n)
        result_for_graphic5 = self.kpi_data.get_data_for_graphic5(cell, kpi_item, n)
        result_for_graphic6 = self.kpi_data.get_data_for_graphic6(cell, kpi_item, n)
        result_for_graphic7 = self.kpi_data.get_data_for_graphic7(cell, kpi_item, n)
        result_for_graphic8 = self.kpi_data.get_data_for_graphic8(cell, kpi_item, n)


        self.graphic.update_plot_graphik1(result_for_graphic1)
        self.graphic.update_plot_graphik2(result_for_graphic2)
        self.graphic.update_plot_graphik3(result_for_graphic3)
        self.graphic.update_plot_graphik4(result_for_graphic4)
        self.graphic.update_plot_graphik5(result_for_graphic5)
        self.graphic.update_plot_graphik6(result_for_graphic6)
        self.graphic.update_plot_graphik7(result_for_graphic7)
        self.graphic.update_plot_graphik8(result_for_graphic8)


