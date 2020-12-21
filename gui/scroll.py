import tkinter


class Scroll:
    def __init__(self, canvas, frame):
        self.canvas = canvas
        self.frame = frame

        self.scroll_y = tkinter.Scrollbar(self.frame, orient="vertical")
        self.scroll_y.pack(side='right', fill='y', expand=1)

        self.canvas.get_tk_widget().config(yscrollcommand=self.scroll_y.set)
        self.canvas.get_tk_widget().bind("<Enter>", self.bind_mouse)
        self.canvas.get_tk_widget().bind("<Leave>", self.unbind_mouse)

        self.scroll_y.config(command=self.canvas.get_tk_widget().yview)

        self.canvas_frame = tkinter.Frame(self.canvas.get_tk_widget())
        self.canvas.get_tk_widget().create_window(4, 4, window=self.canvas_frame, anchor='nw')
        self.canvas_frame.bind("<Configure>", self.frame_dimen)

        self.outer_attr = set(dir(tkinter.Widget))

    def __getattr(self, item):
        if item in self.outer_attr:
            return getattr(self.outer, item)
        else:
            return getattr(self.inner, item)

    def frame_dimen(self, event=None):
        x1, y1, x2, y2 = self.canvas.get_tk_widget().bbox("all")
        height = self.canvas.get_tk_widget().winfo_height()
        self.canvas.get_tk_widget().config(scrollregion=(0, 0, x2, max(y2, height)))

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