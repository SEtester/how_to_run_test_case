# encoding:utf8

import unittest


class SubCase(unittest.TestCase):

    def add_fun(self, a, b):
        return a - b

    def test_sub_1(self):
        '''减法冒烟测试'''
        ret = self.add_fun(1, 2)
        self.assertEqual(-1, ret)

    def test_sub_2(self):
        ret = self.add_fun(1, 2)
        self.assertEqual(6, ret)


if __name__ == '__main__':
    unittest.main(verbosity=2)
