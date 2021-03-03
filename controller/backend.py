import cx_Oracle
import pymssql
import pymysql

from config.config import Config



class GetKpi:
    def __init__(self):
        self.config = Config()
        self.q_2_3 = self.config.query_graphic_2g_3g_daily()
        self.q4 = self.config.query_graphic_4g_daily()
        self.q4_h = self.config.query_graphic_4g_hourly()
        self.q_2_3_h = self.config.query_graphic_2g_3g_hourly()
        self.net_data_2g_hua = self.config.query_2g_net_data_hua()
        self.net_data_2g_nsn = self.config.query_2g_net_data_nsn()
        self.net_data_2g_zte = self.config.query_2g_net_data_zte()

    def conn_driver(self):
        config = Config()
        config_data = config.config_dsn()
        for data in range(len(config_data)):
            cx_Oracle.init_oracle_client(
                lib_dir=rf"{config_data[0]}")
            break

    def oracle_db_conn(self):
        config = Config()
        config_data = config.config_dsn()

        dsn = cx_Oracle.makedsn(config_data[1], config_data[2], service_name=config_data[3])
        config_connection = config.config_connect()
        for i in range(len(config_connection)):
            connection = cx_Oracle.connect(config_connection[0], config_connection[1], dsn, encoding="UTF-8")
        cursor = connection.cursor()
        config_query = config.query_graphic()

        cursor.execute(config_query)
        result_set = cursor.fetchall()
        result_list = []
        for row in result_set:
            result_list.append(row)
        print(result_list)
        return result_list
        cursor.close()

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


    def get_data_for_graphic1(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[0] + self.q4[40:46] + n + self.q4[47:60] + "'" + cell.lac + "'" + self.q4[70:86] + "'" + cell.cell_id[0:length-2] + "'" + self.q4[100:114]+ "'" + cell.cell_id[-2:] + "'" + self.q4[128:133] + date_column_name + self.q4[149:158] + "'" + kpi.start_date + "'" + self.q4[174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[0] + self.q4_h[44:50] + n + self.q4_h[51:64] + "'" + cell.lac + "'" + self.q4_h[74:90] + "'" + cell.cell_id[0:length-2] + "'" + self.q4_h[104:118]+ "'" + cell.cell_id[-2:] + "'" + self.q4_h[132:137] + date_column_name + self.q4_h[153:162] + "'" + kpi.start_date + "'" + self.q4_h[178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[0] + self.q_2_3_h[44:50] + n + self.q_2_3_h[51:64] + "'" + cell.lac + "'" + self.q_2_3_h[74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[98:103] + date_column_name + self.q_2_3_h[119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[0] + self.q_2_3_h[44:50] + n + self.q_2_3_h[51:64] + "'" + cell.lac + "'" + self.q_2_3_h[74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[98:103] + date_column_name + self.q_2_3_h[119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[0] + self.q_2_3[40:46] + n + self.q_2_3[47:60] + "'" + cell.lac + "'" + self.q_2_3[70:80] + "'" + cell.cell_id + "'" + self.q_2_3[94:99] + date_column_name + self.q_2_3[115:124] + "'" + kpi.start_date + "'" + self.q_2_3[140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[0] + self.q_2_3[40:46] + n + self.q_2_3[47:60] + "'" + cell.lac + "'" + self.q_2_3[70:80] + "'" + cell.cell_id + "'" + self.q_2_3[94:99] + date_column_name + self.q_2_3[115:124] + "'" + kpi.start_date + "'" + self.q_2_3[140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY1", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()

    def get_data_for_graphic2(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[1] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                                   70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[1] + self.q4_h[
                                                                                           44:50] + n + self.q4_h[
                                                                                                        51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                        74:90] + "'" + cell.cell_id[
                                                                                                                                                       0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                             104:118] + "'" + cell.cell_id[
                                                                                                                                                                                              -2:] + "'" + self.q4_h[
                                                                                                                                                                                                           132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                         153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                 178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[1] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[1] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[1] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[1] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY1", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_data_for_graphic3(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[2] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                                   70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[2] + self.q4_h[44:50] + n + self.q4_h[
                                                                                                                  51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                                  74:90] + "'" + cell.cell_id[
                                                                                                                                                                 0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                                       104:118] + "'" + cell.cell_id[
                                                                                                                                                                                                        -2:] + "'" + self.q4_h[
                                                                                                                                                                                                                     132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                                   153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                           178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[2] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[2] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[2] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[2] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY1", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_data_for_graphic4(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[3] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                                   70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[3] + self.q4_h[44:50] + n + self.q4_h[
                                                                                                                  51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                                  74:90] + "'" + cell.cell_id[
                                                                                                                                                                 0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                                       104:118] + "'" + cell.cell_id[
                                                                                                                                                                                                        -2:] + "'" + self.q4_h[
                                                                                                                                                                                                                     132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                                   153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                           178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[3] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[3] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[3] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[3] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY1", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_data_for_graphic5(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[4] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                                   70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[4] + self.q4_h[44:50] + n + self.q4_h[
                                                                                                                  51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                                  74:90] + "'" + cell.cell_id[
                                                                                                                                                                 0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                                       104:118] + "'" + cell.cell_id[
                                                                                                                                                                                                        -2:] + "'" + self.q4_h[
                                                                                                                                                                                                                     132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                                   153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                           178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[4] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[4] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[4] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[4] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY1", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_data_for_graphic6(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[5] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                                   70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[5] + self.q4_h[44:50] + n + self.q4_h[
                                                                                                                  51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                                  74:90] + "'" + cell.cell_id[
                                                                                                                                                                 0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                                       104:118] + "'" + cell.cell_id[
                                                                                                                                                                                                        -2:] + "'" + self.q4_h[
                                                                                                                                                                                                                     132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                                   153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                           178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[5] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[5] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[5] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[5] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY6", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_data_for_graphic7(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[6] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                               70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[6] + self.q4_h[44:50] + n + self.q4_h[
                                                                                                                  51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                                  74:90] + "'" + cell.cell_id[
                                                                                                                                                                 0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                                       104:118] + "'" + cell.cell_id[
                                                                                                                                                                                                        -2:] + "'" + self.q4_h[
                                                                                                                                                                                                                     132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                                   153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                           178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[6] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[6] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[6] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[6] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY7", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_data_for_graphic8(self, cell, kpi, n, date_column_name, h):
        cursor, result_list = self.db_conn()
        query = ''
        length = len(cell.cell_id)

        if "lte" in n:
            query = self.q4[:7] + date_column_name + ', ' + kpi.kpi_list[7] + self.q4[40:46] + n + self.q4[
                                                                                                   47:60] + "'" + cell.lac + "'" + self.q4[
                                                                                                                                   70:86] + "'" + cell.cell_id[
                                                                                                                                                  0:length - 2] + "'" + self.q4[
                                                                                                                                                                        100:114] + "'" + cell.cell_id[
                                                                                                                                                                                         -2:] + "'" + self.q4[
                                                                                                                                                                                                      128:133] + date_column_name + self.q4[
                                                                                                                                                                                                                                    149:158] + "'" + kpi.start_date + "'" + self.q4[
                                                                                                                                                                                                                                                                            174:179] + "'" + kpi.end_date + "'"
        elif "4g" in n and "hourly" in n:
            query = self.q4_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[7] + self.q4_h[44:50] + n + self.q4_h[
                                                                                                                  51:64] + "'" + cell.lac + "'" + self.q4_h[
                                                                                                                                                  74:90] + "'" + cell.cell_id[
                                                                                                                                                                 0:length - 2] + "'" + self.q4_h[
                                                                                                                                                                                       104:118] + "'" + cell.cell_id[
                                                                                                                                                                                                        -2:] + "'" + self.q4_h[
                                                                                                                                                                                                                     132:137] + date_column_name + self.q4_h[
                                                                                                                                                                                                                                                   153:162] + "'" + kpi.start_date + "'" + self.q4_h[
                                                                                                                                                                                                                                                                                           178:183] + "'" + kpi.end_date + "'"
        elif "2g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[7] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "3g" in n and "hourly" in n:
            query = self.q_2_3_h[:7] + date_column_name + ', ' + h + ', ' + kpi.kpi_list[7] + self.q_2_3_h[
                                                                                              44:50] + n + self.q_2_3_h[
                                                                                                           51:64] + "'" + cell.lac + "'" + self.q_2_3_h[
                                                                                                                                           74:84] + "'" + cell.cell_id + "'" + self.q_2_3_h[
                                                                                                                                                                               98:103] + date_column_name + self.q_2_3_h[
                                                                                                                                                                                                            119:128] + "'" + kpi.start_date + "'" + self.q_2_3_h[
                                                                                                                                                                                                                                                    144:149] + "'" + kpi.end_date + "'"
        elif "2g" in n and "daily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[7] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        elif "udaily" in n:
            query = self.q_2_3[:7] + date_column_name + ', ' + kpi.kpi_list[7] + self.q_2_3[40:46] + n + self.q_2_3[
                                                                                                         47:60] + "'" + cell.lac + "'" + self.q_2_3[
                                                                                                                                         70:80] + "'" + cell.cell_id + "'" + self.q_2_3[
                                                                                                                                                                             94:99] + date_column_name + self.q_2_3[
                                                                                                                                                                                                         115:124] + "'" + kpi.start_date + "'" + self.q_2_3[
                                                                                                                                                                                                                                                 140:145] + "'" + kpi.end_date + "'"
        print("DB_QUERY8", query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        return result_set
        cursor.close()


    def get_parameters_for_cell(self,n, cell):

        config_data = self.config.config_net_data()
        conn_db = pymysql.connect(host=rf"{config_data[0]}", user=rf"{config_data[1]}", password=rf"{config_data[2]}",
                                  db=rf"{config_data[3]}")
        cursor = conn_db.cursor()
        if "2g" in n:
            query = self.net_data_2g_hua[:73] + cell.lac + self.net_data_2g_hua[78:86] + cell.cell_id
            cursor.execute(query)
            result_set = cursor.fetchall()
            if result_set:
                return result_set
            else:
                query = self.net_data_2g_nsn[:141] + cell.lac + self.net_data_2g_nsn[146:158] + cell.cell_id
                cursor.execute(query)
                result_set = cursor.fetchall()
                if result_set:
                    return result_set
                else:
                    query = self.net_data_2g_zte[:109] + cell.controller + self.net_data_2g_zte[114:132] + cell.cell_id
                    cursor.execute(query)
                    result_set = cursor.fetchall()
                    if result_set:
                        return result_set

    def get_unique2(self):
            cursor, result_list = self.db_conn()
            query = self.config.un2()
            cursor.execute(query)
            result_set = cursor.fetchall()
            return result_set
            cursor.close()

    def get_unique3(self):
            cursor, result_list = self.db_conn()
            query = self.config.un3()
            cursor.execute(query)
            result_set = cursor.fetchall()
            return result_set
            cursor.close()

    def get_unique4(self):
            cursor, result_list = self.db_conn()
            query = self.config.un4()
            cursor.execute(query)
            result_set = cursor.fetchall()
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

    def get_c1(self):
        return self.config.c1()

    def get_c2(self):
        return self.config.c2()

    def get_c3(self):
        return self.config.c3()
