import tkinter
import datetime



from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
from tkcalendar import DateEntry, Calendar


class GraphicView:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.main_window = tkinter.Tk()
        self.main_window.wm_title("Statistics")

        self.input_data_fr = tkinter.Frame(self.main_window,relief='raised', borderwidth=1, background="misty rose")
        self.input_cell_name_lb = tkinter.Label(self.input_data_fr,text='CellName:')
        self.input_cell_name_ent = tkinter.Entry(self.input_data_fr, width='22')
        self.input_cell_ci_lb = tkinter.Label(self.input_data_fr, text='CellId:')
        self.input_cell_ci_ent = tkinter.Entry(self.input_data_fr, width='22')

        self.cal_start_lab = tkinter.Label(self.input_data_fr, text='Choose date').pack(side = 'top',padx=10, pady=10)
        self.cal_start_ent = DateEntry(self.input_data_fr, width=12, background='red',
                        foreground='white', borderwidth=2, year=2020,calendar_cursor="hand1",selectmode='day')
        self.cal_start_ent.pack(padx=10, pady=10)
        self.cal_end_ent = DateEntry(self.input_data_fr, width=12, background='red',
                                       foreground='white', borderwidth=2, year=2020, calendar_cursor="hand1",
                                       selectmode='day')
        self.cal_end_ent.pack(padx=10, pady=10)





        self.input_cell_ci_lb.pack(side='top')
        self.input_cell_ci_ent.pack(side='top', padx=5, pady=5)
        self.input_cell_name_lb.pack(side='top')
        self.input_cell_name_ent.pack(side='top',padx=5, pady=5)
        self.input_data_fr.pack(side='left',fill='y')


        f = Figure(figsize=(8, 2), dpi=100)
        a = f.add_subplot(111)
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self.main_window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
        tkinter.mainloop()

    def draw_plot(self):
        pass
