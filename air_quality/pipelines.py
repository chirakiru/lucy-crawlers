# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime
import psycopg2
import os


class AirQualityPipeline(object):
    def __init__(self):
        # Connect to an existing database
        self.conn = psycopg2.connect(database=os.environ.get("LCDATABASE"),
            user=os.environ.get("LCUSER"),
            password=os.environ.get("LCPASSWORD"),
            host=os.environ.get("LCHOST"),
            port=os.environ.get("LCPORT"))

    def process_item(self, item, spider):
        def cast_as_float(text):
            if text == 'ND':
                return None
            else:
                return float(text)

        # Full datetime
        today         = datetime.datetime.today()
        hour, minute  = map(int, item.get('HOUR').split(':'))
        timestamp     = datetime.datetime(today.year, today.month, today.day, hour, minute)
        item['HOUR'] = timestamp

        item['PM10']    = cast_as_float(item['PM10'])
        item['O3']      = cast_as_float(item['O3'])
        item['NO2']     = cast_as_float(item['NO2'])
        item['SO2']     = cast_as_float(item['SO2'])
        item['CO']      = cast_as_float(item['CO'])
        item['PM25']    = cast_as_float(item['PM25'])

        cur = self.conn.cursor()
        cur.execute("insert into pollutants(hour, station, pm10, \"O3\", \"nO2\", \"sO2\", \"CO\", pm25, created_at, updated_at) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (timestamp, item['STATION'], item['PM10'], item['O3'], item['NO2'], item['SO2'], item['CO'], item['PM25'], today, today) )
        self.conn.commit()

        return item
