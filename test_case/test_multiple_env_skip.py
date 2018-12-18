# encoding:utf8

from selenium import webdriver
from sys import argv
import unittest
from time import sleep

URL = argv[-1]
print('argv[-1] : ', URL)


class TestEnv(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    @unittest.skipIf(URL != 'https://www.baidu.com', '不是百度首页的URL，跳过用例test_load_page')
    def test_load_page(self):
        self.driver.get(URL)
        sleep(10)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestEnv('test_load_page'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suit)
