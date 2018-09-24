import pandas as pd
import os
import sys
import collections
import mysql.connector

#Data export script
#Takes the Dateline Entries CSV as a input and migrates it to the database


def export_entries(csvfile):

    dtype = { 'date': 'str', 'headline': 'str', source: 'str', blurb: 'str', category: 'str', blank: 'str', date1: 'str', zero: 'str', date2: 'str', blank2: 'str', id: 'int', locale: 'str', mediaType: 'str', date3: 'str' }
    df = pd.read_csv(csvfile, dtype=dtype, parse_dates=['date'])

    cnx = mysql.connector.connect(user='nicole', password='password',
                              host='127.0.0.1',
                              database='DatelineRiceStorage')
    df.to_sql("MediaMentions", cnx, if_exists='replace')
    cnx.close()



def main():
    export_entries(sys.argv[1])


if __name__== "__main__":
    main()


