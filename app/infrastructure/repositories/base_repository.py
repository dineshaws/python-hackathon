import mysql.connector
from mysql.connector import errorcode
from app.infrastructure.config.db_connection import Database


class BaseRepository():
    def __init__(self, table = None) -> None:
        self.table = table

    def insert_one(self, statement, data):
        Database.connect()
        Database.cursor.execute(statement, data)
        last_row_id = Database.cursor.lastrowid
        Database.cnx.commit()
        Database.disconnect()
        return last_row_id

    def find_one(self, query):
        Database.connect()
        Database.cursor.execute(query)
        columns = Database.cursor.description
        value = Database.cursor.fetchone()
        result = {}
        for (index,column) in enumerate(value):
            result[columns[index][0]] = column
        Database.disconnect()
        return result

    def find_all(self, query):
        Database.connect()
        Database.cursor.execute(query)
        columns = Database.cursor.description
        values = Database.cursor.fetchall()
        result = []
        for value in values:
            tmp = {}
            for (index,column) in enumerate(value):
                tmp[columns[index][0]] = column
            result.append(tmp)
        Database.disconnect()
        return result
    
    def create_tables(self):
        TABLES = {}
        TABLES['accounts'] = (
            "CREATE TABLE `accounts` ("
                "`id` int(11) NOT NULL AUTO_INCREMENT,"
                "`account_number` int(11) NOT NULL,"
                "`name` varchar(45) NOT NULL,"
                "`description` varchar(45) DEFAULT NULL,"
                "PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;"
            )

        TABLES['transactions'] = (
            "CREATE TABLE `transactions` ("
                "`id` int(11) NOT NULL AUTO_INCREMENT,"
                "`transaction_number` int(11) NOT NULL,"
                "`amount` int(11) NOT NULL,"
                "`type` varchar(4) NOT NULL,"
                "PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;"
            )
        Database.connect()
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print('Creating table {}: '.format(table_name), end='')
                Database.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print('already exists.')
                else:
                    print(err.msg)
            else:
                print('OK')

        Database.disconnect()

    def drop_tables(self):
        TABLES = ['transactions', 'accounts']
        Database.connect()
        for table_name in TABLES:
            try:
                print('Dropping table {}: '.format(table_name), end='')
                Database.cursor.execute('DROP TABLE IF EXISTS {}'.format(table_name))
            except:
                print('Error in dropping table')
            else:
                print('OK')

        Database.disconnect()