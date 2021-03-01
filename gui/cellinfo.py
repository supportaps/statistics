import tkinter
from tkinter import ttk
class Cellinfo:
    def __init__(self, frame):
        self.frame = frame

        self.cell_data_tree = ttk.Treeview(self.frame, height=1, columns=('Item', 'Value'))
        self.cell_data_tree.pack(side="bottom")

