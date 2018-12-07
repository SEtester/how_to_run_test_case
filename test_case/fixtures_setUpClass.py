# encoding:utf8

import unittest

class TestCaseOne(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('---每个测试类开始前运行一次---')

    @classmethod
    def tearDownClass(cls):
        print('---每个测试类结束时运行一次---')

    def test_case_one(self):
        print('--- 测试用例 1 ---')

    def test_case_two(self):
        print('--- 测试用例 2---')


if __name__ == '__main__':
    unittest.main(verbosity=2)
