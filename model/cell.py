
class Cell:
    def __init__(self, name, cell_id, lac, controller):
        self.name = name
        self.cell_id = cell_id
        self.lac = lac
        self.controller = controller

    @property
    def lac(self):
        return self.__lac

    @lac.setter
    def lac(self, value):
        self.__lac = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cell_id(self):
        return self.__cell_id

    @cell_id.setter
    def cell_id(self, value):
        self.__cell_id = value

    @property
    def controller(self):
        return self.__controller

    @controller.setter
    def controller(self, value):
        self.__controller = value


    def __str__(self):
        return f"{self.__name}, {self.__cell_id}, {self.__lac}, {self.__controller}"