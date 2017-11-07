import requests
import json
import psycopg2


# weather class
class weatherinfo():
    def __init__(self,
                 token="tourtoken",
                 url="https://www.ncdc.noaa.gov/cdo-web/api/v2/"):
        self.token = token
        self.baseurl = url

    def gettotalnoofrecords(self, endpoint="stations?limit=1&sortfield=name&sortorder=asc"):
        # https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?limit=1000&sortfield=name&sortorder=asc
        url = self.baseurl + endpoint
        r = requests.get(url, headers={'Token': self.token})

        if (r.status_code == 200):
            data = r.json()
            metadata = data.get("metadata")
            # print metadata
            totalstations = (metadata.get("resultset")).get("count")
            return totalstations

    def getnoofiterations(self, totalnoofstations):
        i = (totalnoofstations / 1000)
        return (i + 1)

    def getweatherstations(self, iterations, endpoint="stations?limit=1000&sortfield=name&sortorder=asc"):
        offset = 0

        '''
        for i in range(0,int(iterations)):

            if i == 0:
                offset = 0
            else:
                offset = (i * 1000) + 1
        '''

        # https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?limit=1000&sortfield=name&sortorder=asc
        url = self.baseurl + endpoint + "&offset=" + str(offset)
        r = requests.get(url, headers={'Token': self.token})

        if (r.status_code == 200):
            con = psycopg2.connect(host="localhost",
                                   user="postgres",
                                   password="Esrigis01",
                                   database="noaa_weather_daily_info",
                                   port="5432")
        # define cursor
        cur = con.cursor()
        data = r.json()
        results = data.get("results")
        for obj in results:
            elevation = obj.get('elevation')
        stationid = obj.get('id')
        stationname = obj.get('name')
        max_date = obj.get('maxdate')
        min_date = obj.get('mindate')
        longitude = str(obj.get('longitude'))
        latitude = str(obj.get('latitude'))
        elevation_unit = obj.get('elevationUnit')

        # define sql query to read data
        sql = "INSERT INTO public.weatherstation_locations(stationid, \
                stationname, min_date, max_date, latitude, longitude, elevation, \
                elevation_unit)VALUES('" + stationid + "','" + stationname + "','" \
              + min_date + "','" + max_date + "'," + latitude + "," + longitude + "," + \
              elevation + ",'" + elevation_unit + "');"

        # excute sql statement
        cur.execute(sql)

        # commit  = we are saving inserted records
        con.commit()

        # first close cursor then close connection
        cur.close()
        con.close()


class dbHelper():
    def __init__(self, hostname, username, password, dbname, portno):
        self.host = hostname
        self.user = username
        self.password = password
        self.database = dbname
        self.port = portno

    def insertInfo(self, stationid, stationname, min_date, max_date, latitude, longitude,
                   elevation, elevation_unit):
        con = psycopg2.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               port=self.port)
        # define cursor
        cur = con.cursor()
        # define sql query to read data
        sql = "INSERT INTO public.weatherstation_locations(stationid, \
        stationname, min_date, max_date, latitude, longitude, elevation, \
        elevation_unit)VALUES('" + stationid + "','" + stationname + "','" \
              + min_date + "','" + max_date + "'," + latitude + "," + longitude + "," + \
              elevation + ",'" + elevation_unit + "');"

        # excute sql statement
        cur.execute(sql)

        # commit  = we are saving inserted records
        con.commit()

        # first close cursor then close connection
        cur.close()
        con.close()


if __name__ == '__main__':
    winfo = weatherinfo()
    totalstations = winfo.gettotalnoofrecords()

    print totalstations
    iterationscount = winfo.getnoofiterations(totalstations)
    print

    #i = winfo.getweatherstations(iterationscount)
    #winfo.getweatherstations(i)
