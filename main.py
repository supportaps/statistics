import cx_Oracle

from config.config import config_dsn, config_connect, query
from gui.graphic_view import GraphicView
import datetime


def oracle_db_conn():
    config_data = config_dsn()
    for data in range(len(config_data)):
        cx_Oracle.init_oracle_client(
            lib_dir=rf"{config_data[0]}")

        dsn = cx_Oracle.makedsn(config_data[1], config_data[2], service_name=config_data[3])
        config_connection = config_connect()
        for i in range(len(config_connection)):
            connection = cx_Oracle.connect(config_connection[0], config_connection[1], dsn, encoding="UTF-8")
        cursor = connection.cursor()
        config_query = query()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list = []
        for row in result_set:
            result_list.append(row)
        print(result_list)
        return result_list
        cursor.close()
        break


if __name__ == '__main__':
    x = []
    y = []
    result = oracle_db_conn()
    for item in result:
        for d in item:
            if type(d) == datetime.datetime:
                x.append(d)
            elif type(d) == float or type(d) == int:
                y.append(d)
    print(x)
    print(y)

    graph = GraphicView(x, y)
