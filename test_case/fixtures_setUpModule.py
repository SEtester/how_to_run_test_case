# encoding:utf8

import unittest

def setUpModule():
    print('--- 模块运行开始时 ，运行一次 ---')

def tearDownModule():
    print('--- 模块运行结束时 ，运行一次 ---')

class TestCaseOne(unittest.TestCase):

    def test_case_one(self):
        print('--- 测试用例 1 ---')

    def test_case_two(self):
        print('--- 测试用例 2---')

class TestCaseTwo(unittest.TestCase):

    def test_case_three(self):
        print('--- 测试用例 3 ---')

    def test_case_four(self):
        print('--- 测试用例 4---')




if __name__ == '__main__':
    unittest.main(verbosity=2)
