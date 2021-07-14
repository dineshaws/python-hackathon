import mysql.connector
from mysql.connector import errorcode

from app.infrastructure.config.config_factory import ConfigFactory

config = ConfigFactory().create()

class Database():
    cursor = None

    @staticmethod
    def connect():
        try:
            cnx = mysql.connector.connect(
                user=config.DB_USER, 
                password=config.DB_PASS,
                host=config.DB_HOST,
                database=config.DB_NAME
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            Database.cursor = cnx.cursor(buffered=True)
            Database.cnx = cnx

    def disconnect():
        Database.cursor.close()
        Database.cnx.close()
        