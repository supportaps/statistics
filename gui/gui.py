import tkinter
import datetime
from tkinter import ttk
from tkcalendar import DateEntry, Calendar

from controller.backend import GetKpi
from graphic.graphic import Graphic
from gui.cellinfo import Cellinfo
from kpi.kpi import Kpi
from model.cell import Cell


class Gui:

    def __init__(self):

        self.kpi_data = GetKpi()

        self.date_column_name = ''
        self.hour_column_name = ''
        self.chosen_column = []
        self.chosen_column_cell_identity = []
        self.concatenated_chars = ''
        self.unique_result = []

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
        self.unique2 = self.kpi_data.get_unique2()
        self.unique3 = self.kpi_data.get_unique3()
        self.unique4 = self.kpi_data.get_unique4()


        self.main_window = tkinter.Tk()

        self.main_window.wm_title("Statistics")
        self.main_window.iconbitmap("vodafone_6830.ico")
        self.height = self.main_window.winfo_height()
        self.width = self.main_window.winfo_width()
        self.screen = self.main_window.winfo_screendepth()
        self.screenh = self.main_window.winfo_screenheight()
        self.screenw = self.main_window.winfo_screenwidth()
        print("SCREEN DATA: ",self.height,self.width,"MY SCREEN ---->",self.screen,self.screenh,self.screenw)

        self.input_data_fr = tkinter.Frame(self.main_window, relief='raised', borderwidth=1, background="#6E6C6B")
        self.input_data_fr.pack(side='left', fill='y', expand=0)

        self.output_data_present1 = tkinter.Frame(self.main_window)
        self.output_data_present1.pack(side='left', fill='y', expand=0)
        #self.output_data_present2 = tkinter.Frame(self.main_window)
        #self.output_data_present2.pack(side='left', fill='y', expand=0)


        self.cal_start_lab = tkinter.Label(self.input_data_fr, text='Choose date', background="#6E6C6B").pack(side='top', padx=10, pady=10)
        self.cal_start_chosen_date_var = tkinter.StringVar()
        self.cal_start_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                       foreground='white', borderwidth=2, year=2021, calendar_cursor="hand1",
                                       selectmode='day')
        self.cal_start_ent.bind("<<DateEntrySelected>>", self.set_date_start)
        self.cal_start_ent.pack(padx=10, pady=10)

        self.cal_end_chosen_date_var = tkinter.StringVar()
        self.cal_end_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                     foreground='white', borderwidth=2, year=2021, calendar_cursor="hand1",
                                     selectmode='day')
        self.cal_end_ent.bind("<<DateEntrySelected>>", self.set_date_end)
        self.cal_end_ent.pack(padx=10, pady=10)

        self.tech_label_fr = tkinter.LabelFrame(self.input_data_fr, text='Technology',background="#6E6C6B")
        self.tech_label_fr.pack()
        self.period_label_fr = tkinter.LabelFrame(self.input_data_fr, text='Period',background="#6E6C6B")
        self.period_label_fr.pack()


        self.var_tech = tkinter.IntVar()
        self.var_tech.set(0)
        self.choose_tech_gsm_rb = tkinter.Radiobutton(self.tech_label_fr, text='GSM', background="#6E6C6B", variable=self.var_tech, value=1,
                                                      command=self.rb_tech_call)
        self.choose_tech_gsm_rb.pack(side='top')
        self.choose_tech_wcdma_rb = tkinter.Radiobutton(self.tech_label_fr, text='WCDMA', background="#6E6C6B", variable=self.var_tech,
                                                        value=2, command=self.rb_tech_call)
        self.choose_tech_wcdma_rb.pack(side='top')
        self.choose_tech_lte_rb = tkinter.Radiobutton(self.tech_label_fr, text='LTE', background="#6E6C6B", variable=self.var_tech, value=3,
                                                      command=self.rb_tech_call)
        self.choose_tech_lte_rb.pack(side='top')

        self.var_period = tkinter.IntVar()
        self.var_period.set(0)
        self.choose_hourly_rb = tkinter.Radiobutton(self.period_label_fr, text='Hourly', background="#6E6C6B", variable=self.var_period,
                                                    value=1, command=self.rb_tech_call)
        self.choose_hourly_rb.pack(side='top')
        self.choose_daily_rb = tkinter.Radiobutton(self.period_label_fr, text='Daily', background="#6E6C6B", variable=self.var_period, value=2,
                                                   command=self.rb_tech_call)
        self.choose_daily_rb.pack(side='top')

        self.input_cell_name_lb = tkinter.Label(self.input_data_fr, text='CellName:', background="#6E6C6B")
        self.input_cell_name_lb.pack(side='top')

        self.cell_name_chosen = tkinter.StringVar()
        self.input_cell_name_cb = ttk.Combobox(self.input_data_fr, textvariable=self.cell_name_chosen)
        self.input_cell_name_cb.pack(side='top', padx=5, pady=5)

        self.cell_name_bt = tkinter.Button(self.input_data_fr,
                                           text='OK', command=self.get_data_for_graphics_by_cell_name)
        self.cell_name_bt.pack(side='top')

        self.input_lac_tac_lb = tkinter.Label(self.input_data_fr, text='LAC(TAC):', background="#6E6C6B")
        self.input_lac_tac_lb.pack(side='top')

        self.cell_lac_tac_chosen = tkinter.StringVar()
        self.input_lac_tac_cb = ttk.Combobox(self.input_data_fr, textvariable=self.cell_lac_tac_chosen)
        self.input_lac_tac_cb.pack(side='top', padx=5, pady=5)

        self.input_cell_ci_lb = tkinter.Label(self.input_data_fr, text='CellId:', background="#6E6C6B")
        self.input_cell_ci_lb.pack(side='top')

        self.cell_id_chosen = tkinter.StringVar()
        self.input_cell_ci_cb = ttk.Combobox(self.input_data_fr, textvariable=self.cell_id_chosen)
        self.input_cell_ci_cb.pack(side='top', padx=5, pady=5)

        self.lac_ci_bt = tkinter.Button(self.input_data_fr,
                                        text='OK', command=self.get_data_for_graphics_by_lac_ci)
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
        #self.cb1.bind("<FocusIn>", self.bind_combobox)
        self.cb1.grab_status()

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

        # graph1 = self.graphic.draw_plot(self.main_window)
        self.graphic = Graphic(self.output_data_present1)


        self.main_window.mainloop()

    def check_date_column(self, column_list):
        for date_column in column_list:
            for column in date_column:
                if column == self.kpi_data.get_c1():
                    self.date_column_name = column
                elif column == self.kpi_data.get_c2():
                    self.date_column_name = column
                elif column == self.kpi_data.get_c3():
                    self.hour_column_name = column

    def bind_combobox(self, event):
        ev = str(event.widget)
        print("EVENT INFOCUS", event.widget, ev)
        self.concatenated_chars = ''
        if ev == '.!frame.!combobox4':
            self.concatenated_chars = self.cb_items[0].get()
            print("CHECK: ",self.concatenated_chars, "CHECK: ",self.cb_items[0].get())
        elif ev == '.!frame.!combobox5':
            self.concatenated_chars = self.cb_items[1].get()
        elif ev == '.!frame.!combobox6':
            self.concatenated_chars = self.cb_items[2].get()
        elif ev == '.!frame.!combobox7':
            self.concatenated_chars = self.cb_items[3].get()
        elif ev == '.!frame.!combobox8':
            self.concatenated_chars = self.cb_items[4].get()
        elif ev == '.!frame.!combobox9':
            self.concatenated_chars = self.cb_items[5].get()
        elif ev == '.!frame.!combobox10':
            self.concatenated_chars = self.cb_items[6].get()
        elif ev == '.!frame.!combobox11':
            self.concatenated_chars = self.cb_items[7].get()
        elif ev == '.!frame.!combobox':
            self.concatenated_chars = self.input_cell_name_cb.get()
        elif ev == '.!frame.!combobox2':
            self.concatenated_chars = self.input_lac_tac_cb.get()
        elif ev == '.!frame.!combobox3':
            self.concatenated_chars = self.input_cell_ci_cb.get()

        if self.concatenated_chars.islower():
            self.concatenated_chars = self.concatenated_chars.upper()
        print("CHECK: ", self.concatenated_chars, "CHECK: ", self.cb_items[0].get())

        for cb in self.cb_items:
            cb.bind("<KeyPress>", self.create_kpilist_by_input_str)
            #cb.bind("<FocusOut>", self.get_input_string)
        self.input_cell_name_cb.bind("<KeyPress>", self.create_kpilist_by_input_str)
        self.input_lac_tac_cb.bind("<KeyPress>", self.create_kpilist_by_input_str)
        self.input_cell_ci_cb.bind("<KeyPress>", self.create_kpilist_by_input_str)

    def create_kpilist_by_input_str(self, event):
        print("EVENT: ",event)
        print("EVENT: ", event.widget)
        ev = str(event.widget)
        symbol = str(event.char)
        updated_column_list = []
        if symbol.islower():
            symbol = symbol.upper()
        if symbol.isalpha() or symbol == '_' or symbol.isnumeric():

            self.concatenated_chars += symbol


            print("current_input_str_test:", self.concatenated_chars)

            #print(self.chosen_column)

            current_input_str = self.concatenated_chars
            if ev == '.!frame.!combobox' or ev == '.!frame.!combobox2' or ev == '.!frame.!combobox3':
                for identity_set in range(len(self.chosen_column_cell_identity)):
                    lac_list = list(self.chosen_column_cell_identity[0])
                    ci_list = list(self.chosen_column_cell_identity[1])
                    cell_name_list = list(self.chosen_column_cell_identity[2])
                    if ev == '.!frame.!combobox':
                        for identity in range(len(cell_name_list)):
                            if current_input_str in cell_name_list[identity]:
                                updated_column_list.append(cell_name_list[identity])
                        self.input_cell_name_cb.configure(values=updated_column_list)
                    elif ev == '.!frame.!combobox2':
                        for identity in range(len(lac_list)):
                            if current_input_str in lac_list[identity]:
                                updated_column_list.append(lac_list[identity])
                        self.input_lac_tac_cb.configure(values=updated_column_list)
                    elif ev == '.!frame.!combobox3':
                        for identity in range(len(ci_list)):
                            if current_input_str in ci_list[identity]:
                                updated_column_list.append(ci_list[identity])
                        self.input_cell_ci_cb.configure(values=updated_column_list)
                    break
                #print("ANY KEY", updated_column_list)
            else:
                for date_column in self.chosen_column:
                    for column in date_column:
                        if current_input_str in column:
                            updated_column_list.append(column)
                #print("ANY KEY",updated_column_list)

            if ev == '.!frame.!combobox4':
                self.cb_items[0].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox5':
                self.cb_items[1].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox6':
                self.cb_items[2].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox7':
                self.cb_items[3].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox8':
                self.cb_items[4].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox9':
                self.cb_items[5].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox10':
                self.cb_items[6].configure(values=updated_column_list)
            elif ev == '.!frame.!combobox11':
                self.cb_items[7].configure(values=updated_column_list)



        elif event.keysym == 'BackSpace':
            print("Pressed backspace: ", event.keysym)

            current_input_str = ''
            #st = self.input_cell_name_cb.get()
            #st = st[:-1]
            print("DELETED_SYMBOL: ")
            if ev == '.!frame.!combobox' or ev == '.!frame.!combobox2' or ev == '.!frame.!combobox3':
                for identity_set in range(len(self.chosen_column_cell_identity)):
                    lac_list = list(self.chosen_column_cell_identity[0])
                    ci_list = list(self.chosen_column_cell_identity[1])
                    cell_name_list = list(self.chosen_column_cell_identity[2])
                    if ev == '.!frame.!combobox':
                        for identity in range(len(cell_name_list)):
                            if self.input_cell_name_cb.get()[:-1].upper() in cell_name_list[identity]:
                                updated_column_list.append(cell_name_list[identity])
                        self.input_cell_name_cb.configure(values=updated_column_list)
                    elif ev == '.!frame.!combobox2':
                        for identity in range(len(lac_list)):
                            if self.input_lac_tac_cb.get()[:-1].upper() in lac_list[identity]:
                                updated_column_list.append(lac_list[identity])
                        self.input_lac_tac_cb.configure(values=updated_column_list)
                    elif ev == '.!frame.!combobox3':
                        for identity in range(len(ci_list)):
                            if self.input_cell_ci_cb.get()[:-1].upper() in ci_list[identity]:
                                updated_column_list.append(ci_list[identity])
                        self.input_cell_ci_cb.configure(values=updated_column_list)
                    break
            else:
                for date_column in self.chosen_column:
                    for column in date_column:
                        if ev == '.!frame.!combobox4' and self.cb_items[0].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox5' and self.cb_items[1].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox6' and self.cb_items[2].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox7' and self.cb_items[3].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox8' and self.cb_items[4].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox9' and self.cb_items[5].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox10' and self.cb_items[6].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                        elif ev == '.!frame.!combobox11' and self.cb_items[7].get()[:-1].upper() in column:
                            updated_column_list.append(column)
                print("BACKSPACE KEY",updated_column_list)
                if ev == '.!frame.!combobox4':
                    self.cb_items[0].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox5':
                    self.cb_items[1].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox6':
                    self.cb_items[2].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox7':
                    self.cb_items[3].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox8':
                    self.cb_items[4].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox9':
                    self.cb_items[5].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox10':
                    self.cb_items[6].configure(values=updated_column_list)
                elif ev == '.!frame.!combobox11':
                    self.cb_items[7].configure(values=updated_column_list)

    def get_input_string(self, event):
        self.concatenated_chars = self.cb1.get()
        self.cb1.configure(values=self.chosen_column)

    def rb_tech_call(self):
        rb_tech = self.var_tech.get()
        rb_period = self.var_period.get()

    def get_cell_identity(self, identities):
        lac = set()
        cell_id = set()
        cell_name = set()
        for item in range(len(identities)):
            for identity in range(len(identities[item])):
                lac.add(identities[item][0])
                cell_id.add(identities[item][1])
                if identities[item][2] is None or identities[item][3] is None or identities[item][4] is None:

                    cell_name.add('None None None')
                else:

                    cell_name.add(identities[item][2]+identities[item][3]+identities[item][4])

        return lac, cell_id, cell_name


    def rb_tech_call(self):
        rb_tech = self.var_tech.get()
        rb_period = self.var_period.get()
        self.chosen_column_cell_identity.clear()

        if rb_tech == 1 and rb_period == 1:
            lac_list, cell_id_list, cell_name_list = self.get_cell_identity(self.unique2)
            self.unique_result = self.unique2
            self.input_cell_name_cb.configure(values=list(cell_name_list))
            self.input_lac_tac_cb.configure(values=list(lac_list))
            self.input_cell_ci_cb.configure(values=list(cell_id_list))
            self.input_cell_name_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_lac_tac_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_cell_ci_cb.bind("<FocusIn>", self.bind_combobox)
            self.chosen_column_cell_identity.append(lac_list)
            self.chosen_column_cell_identity.append(cell_id_list)
            self.chosen_column_cell_identity.append(cell_name_list)

            for cb in self.cb_items:
                cb.configure(values=self.column_2gh)
                cb.bind("<FocusIn>", self.bind_combobox)
                print(self.column_2gd)
                self.check_date_column(self.column_2gh)
                self.chosen_column = self.column_2gh
            else:
                return self.n1
        elif rb_tech == 1 and rb_period == 2:
            lac_list, cell_id_list, cell_name_list = self.get_cell_identity(self.unique2)
            self.unique_result = self.unique2
            self.input_cell_name_cb.configure(values=list(cell_name_list))
            self.input_lac_tac_cb.configure(values=list(lac_list))
            self.input_cell_ci_cb.configure(values=list(cell_id_list))
            self.input_cell_name_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_lac_tac_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_cell_ci_cb.bind("<FocusIn>", self.bind_combobox)
            self.chosen_column_cell_identity.append(lac_list)
            self.chosen_column_cell_identity.append(cell_id_list)
            self.chosen_column_cell_identity.append(cell_name_list)
            for cb in self.cb_items:
                cb.configure(values=self.column_2gd)
                cb.bind("<FocusIn>", self.bind_combobox)
                self.check_date_column(self.column_2gd)
                self.chosen_column = self.column_2gd
            else:
                return self.n2
        elif rb_tech == 2 and rb_period == 1:
            lac_list, cell_id_list, cell_name_list = self.get_cell_identity(self.unique3)
            self.unique_result = self.unique3
            self.input_cell_name_cb.configure(values=list(cell_name_list))
            self.input_lac_tac_cb.configure(values=list(lac_list))
            self.input_cell_ci_cb.configure(values=list(cell_id_list))
            self.input_cell_name_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_lac_tac_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_cell_ci_cb.bind("<FocusIn>", self.bind_combobox)
            self.chosen_column_cell_identity.append(lac_list)
            self.chosen_column_cell_identity.append(cell_id_list)
            self.chosen_column_cell_identity.append(cell_name_list)
            for cb in self.cb_items:
                cb.configure(values=self.column_3gh)
                cb.bind("<FocusIn>", self.bind_combobox)
                self.check_date_column(self.column_3gh)
                self.chosen_column = self.column_3gh
            else:
                return self.n3
        elif rb_tech == 2 and rb_period == 2:
            lac_list, cell_id_list, cell_name_list = self.get_cell_identity(self.unique3)
            self.unique_result = self.unique3
            self.input_cell_name_cb.configure(values=list(cell_name_list))
            self.input_lac_tac_cb.configure(values=list(lac_list))
            self.input_cell_ci_cb.configure(values=list(cell_id_list))
            self.input_cell_name_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_lac_tac_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_cell_ci_cb.bind("<FocusIn>", self.bind_combobox)
            self.chosen_column_cell_identity.append(lac_list)
            self.chosen_column_cell_identity.append(cell_id_list)
            self.chosen_column_cell_identity.append(cell_name_list)
            for cb in self.cb_items:
                cb.configure(values=self.column_3gd)
                cb.bind("<FocusIn>", self.bind_combobox)
                self.check_date_column(self.column_3gd)
                self.chosen_column = self.column_3gd
            else:
                return self.n4
        elif rb_tech == 3 and rb_period == 1:
            lac_list, cell_id_list, cell_name_list = self.get_cell_identity(self.unique4)
            self.unique_result = self.unique4
            self.input_cell_name_cb.configure(values=list(cell_name_list))
            self.input_lac_tac_cb.configure(values=list(lac_list))
            self.input_cell_ci_cb.configure(values=list(cell_id_list))
            self.input_cell_name_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_lac_tac_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_cell_ci_cb.bind("<FocusIn>", self.bind_combobox)
            self.chosen_column_cell_identity.append(lac_list)
            self.chosen_column_cell_identity.append(cell_id_list)
            self.chosen_column_cell_identity.append(cell_name_list)
            for cb in self.cb_items:
                cb.configure(values=self.column_4gh)
                cb.bind("<FocusIn>", self.bind_combobox)
                self.check_date_column(self.column_4gh)
                self.chosen_column = self.column_4gh

            else:
                return self.n5
        elif rb_tech == 3 and rb_period == 2:
            lac_list, cell_id_list, cell_name_list = self.get_cell_identity(self.unique4)
            self.unique_result = self.unique4
            self.input_cell_name_cb.configure(values=list(cell_name_list))
            self.input_lac_tac_cb.configure(values=list(lac_list))
            self.input_cell_ci_cb.configure(values=list(cell_id_list))
            self.input_cell_name_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_lac_tac_cb.bind("<FocusIn>", self.bind_combobox)
            self.input_cell_ci_cb.bind("<FocusIn>", self.bind_combobox)
            self.chosen_column_cell_identity.append(lac_list)
            self.chosen_column_cell_identity.append(cell_id_list)
            self.chosen_column_cell_identity.append(cell_name_list)
            for cb in self.cb_items:
                cb.configure(values=self.column_4gd)
                cb.bind("<FocusIn>", self.bind_combobox)
                self.check_date_column(self.column_4gd)
                self.chosen_column = self.column_4gd

            else:
                return self.n6

    def set_date_start(self, event):
        start = self.cal_start_ent.get_date().strftime("%d-%b-%y")
        self.cal_start_chosen_date_var.set(start)


    def set_date_end(self, event):
        end = self.cal_end_ent.get_date().strftime("%d-%b-%y")
        self.cal_end_chosen_date_var.set(end)


    def get_cell_name_from_ent(self):
        return self.input_cell_name_cb.get()

    def get_ci(self):
        ci = self.input_cell_ci_cb.get()
        return ci

    def get_lac_tac(self):
        lac_tac = self.input_lac_tac_cb.get()
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

    def get_results_from_source(self, cell):
        kpi_item = Kpi(self.get_kpi_columns(), self.cal_start_chosen_date_var.get(), self.cal_end_chosen_date_var.get())
        n = self.get_name()



        result_for_graphic1 = self.kpi_data.get_data_for_graphic1(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic2 = self.kpi_data.get_data_for_graphic2(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic3 = self.kpi_data.get_data_for_graphic3(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic4 = self.kpi_data.get_data_for_graphic4(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic5 = self.kpi_data.get_data_for_graphic5(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic6 = self.kpi_data.get_data_for_graphic6(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic7 = self.kpi_data.get_data_for_graphic7(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic8 = self.kpi_data.get_data_for_graphic8(cell, kpi_item, n, self.date_column_name, self.hour_column_name)

        return result_for_graphic1,result_for_graphic2,result_for_graphic3,result_for_graphic4,result_for_graphic5,result_for_graphic6,result_for_graphic7,result_for_graphic8, n

    def update_plots(self,cell):
        res1,res2,res3,res4,res5,res6,res7,res8, n = self.get_results_from_source(cell)
        self.graphic.update_plot_graphik1(res1,n)
        self.graphic.update_plot_graphik2(res2,n)
        self.graphic.update_plot_graphik3(res3,n)
        self.graphic.update_plot_graphik4(res4,n)
        self.graphic.update_plot_graphik5(res5,n)
        self.graphic.update_plot_graphik6(res6,n)
        self.graphic.update_plot_graphik7(res7,n)
        self.graphic.update_plot_graphik8(res8,n)

    def get_data_for_graphics_by_cell_name(self):
        found_name = ''
        found_lac = ''
        found_ci = ''
        for _ in range(len(self.unique_result)):
            if None not in self.unique_result[_]:
                cn =  self.unique_result[_][2] + self.unique_result[_][3] + self.unique_result[_][4]
                if cn == self.get_cell_name_from_ent():
                    found_name = self.unique_result[_][2] + self.unique_result[_][3] + self.unique_result[_][4]
                    found_lac = str(self.unique_result[_][0])
                    found_ci =  str(self.unique_result[_][1])
                    found_controller = self.unique_result[_][5]

        cell = Cell(found_name, found_ci, found_lac, found_controller)

        #self.get_results_from_source(cell)
        self.update_plots(cell)

    def get_data_for_graphics_by_lac_ci(self):

        cell = Cell(self.get_cell_name_from_ent(), self.get_ci(), self.get_lac_tac())

        kpi_item = Kpi(self.get_kpi_columns(), self.cal_start_chosen_date_var.get(), self.cal_end_chosen_date_var.get())
        n = self.get_name()
        # SET BSC NUMBER


        result_for_graphic1 = self.kpi_data.get_data_for_graphic1(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic2 = self.kpi_data.get_data_for_graphic2(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic3 = self.kpi_data.get_data_for_graphic3(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic4 = self.kpi_data.get_data_for_graphic4(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic5 = self.kpi_data.get_data_for_graphic5(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic6 = self.kpi_data.get_data_for_graphic6(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic7 = self.kpi_data.get_data_for_graphic7(cell, kpi_item, n, self.date_column_name, self.hour_column_name)
        result_for_graphic8 = self.kpi_data.get_data_for_graphic8(cell, kpi_item, n, self.date_column_name, self.hour_column_name)

        self.graphic.update_plot_graphik1(result_for_graphic1, n)
        self.graphic.update_plot_graphik2(result_for_graphic2, n)
        self.graphic.update_plot_graphik3(result_for_graphic3, n)
        self.graphic.update_plot_graphik4(result_for_graphic4, n)
        self.graphic.update_plot_graphik5(result_for_graphic5, n)
        self.graphic.update_plot_graphik6(result_for_graphic6, n)
        self.graphic.update_plot_graphik7(result_for_graphic7, n)
        self.graphic.update_plot_graphik8(result_for_graphic8, n)
