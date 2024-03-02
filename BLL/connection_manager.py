import mysql.connector
class ConnectionManager:
    __connection_config = {
        "host": "localhost",
        "database": "bootcamp",
        "user": "root"
    }

    __mydb = mysql.connector.connect(**__connection_config)

    def open_connection(self):

        self.__mydb = mysql.connector.connect(**self.__connection_config)

    def close_connection(self):
        self.__mydb.close()

    def get_connection(self):
        return self.__mydb