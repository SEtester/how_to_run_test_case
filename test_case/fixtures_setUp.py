# encoding:utf8


import unittest


class TestCaseOne(unittest.TestCase):

    def setUp(self):
        print('---每个用例运行前执行---')

    def tearDown(self):
        print('---每个用例运行结束后执行---')

    def test_case_one(self):
        print('--- 测试用例 1 ---')

    def test_case_two(self):
        print('--- 测试用例 2---')


if __name__ == '__main__':
    unittest.main(verbosity=2)
