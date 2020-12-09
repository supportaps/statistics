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
        print("2ghquery", config_query)
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs2gh",result_list)
        return result_set
        cursor.close()

    def get_columns_2g_d(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_2gd()
        print("2gdquery", config_query)
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs2gd", result_list)
        return result_set
        cursor.close()

    def get_columns_3g_h(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_3gh()
        print("3ghquery",config_query)
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs3gh", result_list)
        return result_set
        cursor.close()

    def get_columns_3g_d(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_3gd()
        print("3gdquery", config_query)
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs3gd", result_list)
        return result_set
        cursor.close()

    def get_columns_4g_h(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_4gh()
        print("4ghquery", config_query)
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs4gh", result_list)
        return result_set
        cursor.close()

    def get_columns_4g_d(self):
        cursor, result_list = self.db_conn()
        config_query = self.config.query_head_4gd()
        print("4gdquery", config_query)
        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list.append(result_set)
        print("rs4gd", result_list)
        return result_set
        cursor.close()

    def get_n1(self):
        return self.config.n1()

    def get_n2(self):
        return self.config.n2()

    def get_n3(self):
        return self.config.n3()

    def get_n4(self):
        return self.config.n4()

    def get_n5(self):
        return self.config.n5()

    def get_n6(self):
        return self.config.n6()