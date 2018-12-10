# encoding:utf8

import unittest


class SkipExample(unittest.TestCase):

    @unittest.skip('用例 1 无条件跳过')
    def test_case_one(self):
        print('---用例 1 ---')

    @unittest.skipIf(2 > 1, '条件为True ，用例2 跳过')
    def test_case_two(self):
        print('---用例 2  ---')

    @unittest.skipUnless(2 < 1, '条件为False,用例3 跳过')
    def test_case_three(self):
        print('---用例 3  ---')


if __name__ == '__main__':
    unittest.main(verbosity=2)
