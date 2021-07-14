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
                "`id` bigint NOT NULL AUTO_INCREMENT,"
                "`account_number` varchar(255) NOT NULL,"
                "`account_balance` decimal(19,2) NOT NULL,"
                "`description` varchar(255) DEFAULT NULL,"
                "`account_name` varchar(255) NOT NULL,"
                "`version` bigint NOT NULL,"
                "PRIMARY KEY (`id`),"
                "UNIQUE KEY `UK_6kplolsdtr3slnvx97xsy2kc8` (`account_number`)"
            ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
        )

        TABLES['account_transactions'] = (
            "CREATE TABLE `account_transactions` ("
                "`id` bigint NOT NULL AUTO_INCREMENT,"
                "`accounts_id` bigint NOT NULL,"
                "`txn_type` varchar(255) NOT NULL,"
                "`amount` decimal(19,2) NOT NULL,"
                "`txn_number` varchar(255) NOT NULL,"
                "`created_on` varchar(255) NOT NULL,"
                "`version` bigint NOT NULL,"
                "PRIMARY KEY (`id`),"
                "KEY `FKdsg8ptc8qfbq0aejfppd8j6b2` (`accounts_id`),"
                "CONSTRAINT `FKdsg8ptc8qfbq0aejfppd8j6b2` FOREIGN KEY (`accounts_id`) REFERENCES `accounts` (`id`)"
            ") ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;"
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
        TABLES = ['account_transactions', 'accounts'] # dropping account_transactions first as its have foreign key on accounts table
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