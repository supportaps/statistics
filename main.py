import datetime


from controller.backend import GetKpi
from gui.gui import Gui





if __name__ == '__main__':

    getkpi = GetKpi()

    getkpi.conn_driver()

    gui = Gui()
