import requests
import json
import urllib2
import psycopg2


class weatherUtilities():
    def __init__(self):
        pass

    def getCount(self):
        url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1&offset=1&sortfield=id&sortorder=asc'
        headers = {'Token': 'yourtoken'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)

            recordsCount = int((data['metadata'])['resultset'].get('count'))
            IterationsCount = (recordsCount / 1000) + 1
            return IterationsCount

    def getLocations(self, iterations):
        locations = []
        print "Process Started"
        constring = "dbname='weatherdb' user='hari' password='Esrigis01' host=your_rds_host' port=5432"

        conn = psycopg2.connect(constring)
        cur = conn.cursor()

        for i in range(0, int(iterations)):
            baseurl = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?' \
                      'limit=1000&sortfield=name&sortorder=asc'

            if i > 0:
                offset = (1000 * i) + 1
                url = baseurl + "&offset=" + str(offset)
            else:
                url = baseurl

            headers = {'Token': 'your token'}
            r = requests.get(url, headers=headers)

            if r.status_code == 200:
                data = json.loads(r.text)
                results = data["results"]
                for item in results:
                    datacoverage = str(item.get('datacoverage'))
                    id = item.get('id')
                    maxdate = item.get('maxdate')
                    mindate = item.get('mindate')
                    name = item.get('name').replace("'", "")

                    strSql = "INSERT INTO public.locations(datacoverage, id, maxdate, mindate, name)VALUES (" + \
                             datacoverage + ",'" + id + "','" + maxdate + "','" + mindate + "','" + name + "');"

                    cur.execute(strSql)
                    conn.commit()

        cur.close()
        conn.close()

                # locations.append(item)

        # jsonData = {"Records": locations}
        # with open('LocationsData.json', 'w') as f:
        #     json.dump(jsonData, f)

        print "Process Completed for locations data"


if __name__ == '__main__':
    wutilities = weatherUtilities()
    iterations = wutilities.getCount()
    print iterations
    # wutilities.getWeatherStationLocations(iterations)

    wutilities.getLocations(iterations)
