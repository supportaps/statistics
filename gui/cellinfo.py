import tkinter
from tkinter import ttk
class Cellinfo:
    def __init__(self, frame, cell):
        self.frame = frame
        self.cell = cell
        self.cell_data_tree = ttk.Treeview(self.frame, height=1, columns=('Item', 'Value'))
        self.cell_data_tree.pack(side="bottom")

    @property
    def cell(self):
        return self.__cell

    @cell.setter
    def cell(self, value):
        self.__cell = value



