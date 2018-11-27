# encoding:utf8

import unittest
import pytest


class AddCase(unittest.TestCase):

    @pytest.mark.bvt
    def test_add_1(self):
        '''加法冒烟测试'''
        ret = self.add_fun(1, 2)
        self.assertEqual(3, ret)

    def add_fun(self, a, b):
        return a + b

    def test_add_2(self):
        ret = self.add_fun(1, 2)
        self.assertEqual(6, ret)


if __name__ == '__main__':
    unittest.main(verbosity=2)
