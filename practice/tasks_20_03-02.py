"""
Нужно реализовать класс-адаптер, который будет:
1. Раз в 1 минуту получать цену на Bitcoin от
https://www.quandl.com/api/v3/datasets/BCHARTS/BITSTAMPUSD
2. Распаковывать нужные данные
3. Сохранять их во внешний словарь вида {"2020-03-19": 5340}

Импорты:
from time import sleep
import requests
"""

import requests
from datetime import date
from time import sleep

historical_data = dict()


class BTCPriceWorker:
    def __init__(self):
        self.api_url = "https://www.quandl.com/api/v3/datasets/BCHARTS/BITSTAMPUSD"

    def get_raw_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            print(response)
            return response
        else:
            print(f"Response status code: {response.status_code}")
            return None

    def process_data(self, raw_data):
        return raw_data["dataset"]["data"][0][4]

    def save_data(self, clean_data):
        key = str(date.today())
        historical_data[key] = clean_data
        print(historical_data)

    def work(self):
        while True:
            raw_data = self.get_raw_data()
            if raw_data:
                clean_data = self.process_data(raw_data)
                if clean_data:
                    self.save_data(clean_data)
            sleep(10)


worker = BTCPriceWorker()
worker.work()
