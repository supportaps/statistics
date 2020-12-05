import cx_Oracle

from config.config import Config


class GetKpi:
    def __init__(self):
        self.config = Config()



    def db_conn(self):
        config_data = self.config.config_dsn()
        result_list = []
        dsn = cx_Oracle.makedsn(config_data[1], config_data[2], service_name=config_data[3])
        config_connection = self.config.config_connect()
        for i in range(len(config_connection)):
            connection = cx_Oracle.connect(config_connection[0], config_connection[1], dsn, encoding="UTF-8")
        cursor = connection.cursor()
        return cursor, result_list

    def get_columns_2g_h(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_2gh()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs",result_list)
        return result_set
        cursor.close()

    def get_columns_2g_d(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_2gd()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        return result_list
        cursor.close()

    def get_columns_3g_h(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_3gh()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        return result_set
        cursor.close()

    def get_columns_3g_d(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_3gd()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        return result_set
        cursor.close()

    def get_columns_4g_h(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_4gh()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        return result_set
        cursor.close()

    def get_columns_4g_d(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_4gd()
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        return result_set
        cursor.close()