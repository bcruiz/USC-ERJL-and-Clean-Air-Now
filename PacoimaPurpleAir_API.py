from purpleair import PurpleAir
import datetime
import json
import pprint
import sqlite3
from pandas.io.json import json_normalize

p = PurpleAir('XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX')
# API required key from PurpleAir website
# Have to email them (contact@purpleair.com) a request stating how frequent you would be pulling data from their API source

con = sqlite3.connect('DelAmo_PurpleAir.db')
# initializes sqlite DB to store all data pull, sqlite can be stored on your local device and compresses the files so that the files don't take up muuch space
# you can import the data to csv files but would take longer and more saved space
# https://www.sqlite.org/index.html

cur = con.cursor()

date_range = []
i = 1609488000 #Date and time (your time zone): Friday, January 1, 2021 12:00:00 AM GMT-08:00
# datetime is in epoch; I use this website to convert dates back and forth
# https://www.epochconverter.com/

# a list of a date range; was used to pull 2 years worth of purple air monitor data
while i < 1672559999:
    j = i + 259200
    tup = (i, j)
    date_range.append(tup)
    i = j + 600

sensor_list = [56207, 37551, 91055, 56119, 55503, 56141, 55923, 56073, 98643, 56087, 99139, 99345, 56053, 54631, 56153, 56077, 55467, 55405, 55515]
# would have to specify which purple air monitor you wish to pull, can be selected through purple air website

cur.execute('''DROP TABLE IF EXISTS Pacoima_PurpleAir''')
# python driver stating sql code
# will drop table each time line is ran, if updating tables comment this line out

cur.execute('''CREATE TABLE Pacoima_PurpleAir (Monitor TEXT, Timestamp TEXT, Value INT)''')
# creates new table, stating table name and columns with variable type

## a for loop that iterates through each purple air monitor through each date range in our date_range list
for sensor in sensor_list:
    print('Sensor: ' + str(sensor))
    for date in date_range:
        r = p.get_sensor_history(sensor_index=sensor, start_timestamp=date[0], end_timestamp=date[1], fields=('pm2.5_alt', ))
        # function calling same parameters from https://api.purpleair.com/
        # I recommend exploring this site once you have access to an API key
        print("Daterange: " + str(date))
        ## once in date range iterates through each row of data, can be as small as 10 minute intervals
        for i in range(len(r['data'])):
            Monitor = sensor
            Timestamp = r['data'][i][0]
            Value = r['data'][i][1]

            tup = (Monitor, Timestamp, Value)
            cur.executemany('INSERT INTO Pacoima_PurpleAir VALUES(?, ?, ?)', [tup])
            # tuple to store as a list to be inseted into sqlite DB

            con.commit()
            # for each line of data read is inputed and saved into sqlite DB
            # very important

    # cur.execute('SELECT * FROM DelAmo_PurpleAir LIMIT 5')
    # can even check to see what is actually being inputted into the DB

con.close()
# cannot stress how important it is to close DB after each script run