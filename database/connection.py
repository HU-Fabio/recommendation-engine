import mysql.connector


class Database:

    @staticmethod
    def Mysql():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="recommendation_engine"
        )
        return mydb
