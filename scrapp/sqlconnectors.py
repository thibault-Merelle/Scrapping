import mysql.connector
from scrapp import scrapp_VR

class mototravel_conn:

    def __init__(self):
        self.connection = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            passwd=os.environ['MYSQL_ROOT_PASSWORD'],
            auth_plugin=os.environ['MYSQL_AUTH_PLUGIN'],
            database=os.environ['MYSQL_DATABASE']
            )
        self.c = self.connection.cursor()
        self.myclass = scrapp_VR()


    def create_tables(self):
        self.c.execute("DROP TABLE IF EXISTS vintage_ride;")
        self.c.execute("CREATE TABLE IF NOT EXISTS vintage_ride \
                        (\
                        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,\
                        title VARCHAR(200),\
                        destination VARCHAR(200),\
                        departure_date VARCHAR(200),\
                        end_date VARCHAR(200),\
                        year INT,\
                        level VARCHAR(200)\
                        )\
                        ;")
        self.connection.commit()


    def insert_tables(self, data):
        sql = "INSERT INTO vintage_ride (title, destination, departure_date, end_date, year, level) VALUES "
        for ii, i in enumerate(data):
            if ii == 75:
                val = tuple(i.values())
                sql = sql + str(val)  + ";"
            else:
                val = tuple(i.values())
                sql = sql + str(val) + ", "
        self.c.execute("use mototravel;")
        self.c.execute(sql)
        self.connection.commit()
