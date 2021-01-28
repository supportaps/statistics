import tkinter


class Scroll:
    def __init__(self, canvas, container, fig):
        self.canvas = canvas
        self.container = container
        self.fig = fig


        self.scroll_y = tkinter.Scrollbar(self.container, orient="vertical")
        self.scroll_y.pack(side='right', fill='y')
        self.scroll_y.config(command=self.canvas.get_tk_widget().yview)

        self.scrollable_frame = tkinter.Frame(self.canvas.get_tk_widget())



        self.canvas.get_tk_widget().create_window((4, 4), window=self.scrollable_frame, anchor="nw")
        self.canvas.get_tk_widget().update_idletasks()

        self.canvas.get_tk_widget().config(yscrollcommand=self.scroll_y.set)
        self.canvas.get_tk_widget().bind("<Enter>", self.bind_mouse)
        self.canvas.get_tk_widget().bind("<Leave>", self.unbind_mouse)

        self.scrollable_frame.bind("<Configure>", self.frame_dimen)
        self.canvas.get_tk_widget().bind("<Configure>", self.canvas_dimen)






        self.canvas.mpl_connect('scroll_event', self.resize)

        #self.outer_attr = set(dir(tkinter.Widget))

    #def __getattr(self, item):
        #if item in self.outer_attr:
            #return getattr(self.outer, item)
        #else:
           # return getattr(self.inner, item)


    def resize(self, event):


        self.fig.tight_layout()
        self.fig.set_dpi(80)
        self.fig.set_size_inches(13, 40)
        fig_weight = self.fig.get_figwidth()
        fig_height = self.fig.get_figheight()
        dpi = self.fig.get_dpi()
        print(fig_weight,fig_height, dpi)
        #self.canvas1.get_tk_widget().config(width=fig_weight*dpi, height=fig_height*dpi)
        x1, y1, x2, y2 = self.canvas.get_tk_widget().bbox("all")
        print("SCROLL BBOX: ",x1, y1, x2, y2)
        print("SCROLL WINFO FRAME: ", self.scrollable_frame.winfo_geometry())


    def frame_dimen(self, event):
        self.canvas.get_tk_widget().config(scrollregion=self.canvas.get_tk_widget().bbox("all"))

    def canvas_dimen(self, event):
        canvas_width = event.width
        print("canvas_width: ",canvas_width)




    def bind_mouse(self, event=None):
        self.canvas.get_tk_widget().bind_all("<4>", self.on_mousewheel)
        self.canvas.get_tk_widget().bind_all("<5>", self.on_mousewheel)
        self.canvas.get_tk_widget().bind_all("<MouseWheel>", self.on_mousewheel)


    def unbind_mouse(self, event=None):
        self.canvas.get_tk_widget().unbind_all("<4>")
        self.canvas.get_tk_widget().unbind_all("<5>")
        self.canvas.get_tk_widget().unbind_all("<MouseWheel>")


    def on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.canvas.get_tk_widget().yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.get_tk_widget().yview_scroll(1, "units")
