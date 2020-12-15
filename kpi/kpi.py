
class Kpi:
    def __init__(self, kpi_list, start_date, end_date):
        self.kpi_list = kpi_list
        self.start_date = start_date
        self.end_date = end_date

    @property
    def kpi_list(self):
        return self.__kpi_list

    @kpi_list.setter
    def kpi_list(self, value):
        self.__kpi_list = value

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        self.__start_date = value

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        self.__end_date = value