import psycopg2  # define database connection parameters
import config

class dbHelper():
    def __init__(self, hostname, username, password, dbname, portno):
        self.host = hostname
        self.user = username
        self.password = password
        self.database = dbname
        self.port = portno

    def selectInfo(self, strsql):
        con = psycopg2.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               port=self.port)
        # define cursor
        cur = con.cursor()
        # define sql query to read data
        # sql = "select * from public.weather_daily_info limit 100;"
        # excute sql statement
        cur.execute(strsql)
        # collect results
        rows = cur.fetchall()

        for row in rows:
            print tuple(row)

        cur.close()
        con.close()

    def insertInfo(self,firstname,middlename,lastname,age):
        con = psycopg2.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               port=self.port)
        # define cursor
        cur = con.cursor()
        # define sql query to read data
        sql = "INSERT INTO public.studentinfo(fname, mname, lname, age)VALUES ('" + firstname +  "', '" + middlename + "', '" + lastname + "'," + str(age) + ");"

        print sql
        # excute sql statement
        cur.execute(sql)

        #commit  = we are saving inserted records
        con.commit()

        # first close cursor then close connection
        cur.close()
        con.close()

    def updateInfo(self):
        pass

    def deleteInfo(self,id):
        con = psycopg2.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               port=self.port)
        # define cursor
        cur = con.cursor()
        # define sql query to read data
        sql = "delete from studentinfo where id = " + str(id) + ";"
        # excute sql statement
        cur.execute(sql)

        # commit  = we are saving inserted records
        con.commit()

        # first close cursor then close connection
        cur.close()
        con.close()


if __name__ == '__main__':

    condetails = config.dbdetails

    helper = dbHelper(condetails["host"],
                      condetails["username"],
                      condetails["password"],
                      condetails["database"],
                      condetails["portno"])

    #helper.insertInfo("Test","","test1",50)

    #helper.deleteInfo(9)

    helper.selectInfo("select fn_get_film_details();")

