import sqlite3
import requests
from time import sleep

from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, url):
        self.url = url
        self.raw_html = None
        self.bulk_data = list()
        self.is_active = False

    def work(self):
        data = None
        if self.get_html():
            data = self.parse_html()
        return self.bulk_data


    def get_html(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.raw_html = response.text
                return True
            else:
                print(f"Failed to get HTML, code {response.status_code}:\n{response.text}")
                return False
        except Exception as e:
            print(f"Failed to get HTML: {e}")
            return False

    def parse_html(self):
        raise NotImplementedError("Use parse_html method from child")


class NVParser(BaseParser):
    def __init__(self, url):
        super().__init__(url)

    def parse_html(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')
        one_results = soup.find_all('div', attrs={'class': 'one_result'})

        for result in one_results:
            record = dict()
            raw_headline = result.find('span', attrs={'class': 'search__article_title'})
            record['headline'] = raw_headline.get_text().encode('iso-8859-1').decode('utf8').strip()

            raw_tag = result.find('div', attrs={'class': 'atom__additional_category'})
            record['tag'] = raw_tag.get_text().encode('iso-8859-1').decode('utf8')

            raw_date = result.find('div', attrs={'class': 'atom__additional_pubDate'})
            record['date'] = raw_date.get_text().encode('iso-8859-1').decode('utf8')

            self.bulk_data.append(record)
