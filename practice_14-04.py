import unittest
from time import sleep
from unittest.mock import MagicMock
from my1404 import BaseParser, NVParser


class TestBaseParser(unittest.TestCase):
    def setUp(self):
        self.parser = MagicMock(BaseParser)

    def test_work(self):
        self.parser.get_html.return_value = True
        self.parser.get_html.side_effect = print("test get_html")
        self.parser.work()

        assert self.parser.get_html.call_count == 1
        assert self.parser.parse_html.call_count == 1

    def test_work_non_200(self):
        self.parser.get_html.return_value = False
        self.parser.work()

        assert self.parser.get_html.call_count == 1
        assert self.parser.parse_html.call_count == 0


    def test_get_html(self):
        pass

    def test_save_data(self):
        pass


class TestNVParser(unittest.TestCase):
    pass


if __name__ == '__main__':
    uniitest.main()
