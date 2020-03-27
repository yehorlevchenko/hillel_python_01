# https://api.darksky.net/forecast/4141b0f2514be7d396158a3628b6eb29/46.29,30.44?exclude=[hourly,daily,flags]

import requests
from json import loads, JSONDecodeError
import sqlite3
from time import sleep


class WeatherAPIWorker:

    def __init__(self, api_key, lat, lon):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.base_api_url = "https://api.darksky.net"
        self.api_endpoint = "forecast"
        self.excluded_blocks = "hourly, daily, flags"

    def _get_data(self):
        print("getting data")
        url = f"{self.base_api_url}/{self.api_endpoint}/{self.api_key}/{self.lat},{self.lon}?exclude=[{self.excluded_blocks}]&units=auto"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f'API response is {response.status_code}')
            return None

    def _process_data(self, raw_data):
        print("processing data")
        json_data = None
        try:
            json_data = loads(raw_data)
        except JSONDecodeError as e:
            print(e)
        except Exception as e:
            print(e)
        finally:
            return json_data

    def _save_data(self, data):
        print("saving data")
        with sqlite3.connect('weather_db.db') as db:
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO weather VALUES ('{data['currently']['time']}', '{data['currently']['summary']}', '{data['currently']['temperature']}')")
            db.commit()

    def work(self):
        while True:
            raw_data = self._get_data()
            if raw_data:
                data = self._process_data(raw_data)
                if data:
                    self._save_data(data)
            print("iteration is over, sleep")
            sleep(5)


def prepare_db():
    connection = sqlite3.connect('weather_db.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE weather (timestamp, summary, temperature)''')
    connection.commit()
    connection.close()


try:
    prepare_db()
except sqlite3.OperationalError:
    print("DB already exists")

key = "4141b0f2514be7d396158a3628b6eb29"
lat = 46.29
lon = 30.44

worker = WeatherAPIWorker(api_key=key, lat=lat, lon=lon)
worker.work()
