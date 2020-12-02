import cx_Oracle

from config.config import config_dsn, config_connect, query


def get_columns():
        config_data = config_dsn()
        dsn = cx_Oracle.makedsn(config_data[1], config_data[2], service_name=config_data[3])
        config_connection = config_connect()
        for i in range(len(config_connection)):
            connection = cx_Oracle.connect(config_connection[0], config_connection[1], dsn, encoding="UTF-8")
        cursor = connection.cursor()
        config_query = query()
        for q in range(len(config_query)):
            cursor.execute(config_query[1])
        result_set = cursor.fetchall()
        result_list = []
        for row in result_set:
            result_list.append(row)
        return result_list
        cursor.close()

