# encoding:utf8

from selenium import webdriver
from sys import argv
import unittest
from time import sleep


class TestEnv(unittest.TestCase):

    def setUp(self):
        self.url = argv[-1]
        print(self.url)
        self.driver = webdriver.Chrome()

    def test_load_page(self):
        self.driver.get(self.url)
        sleep(10)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestEnv('test_load_page'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
