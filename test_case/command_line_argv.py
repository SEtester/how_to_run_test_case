#encoding:utf8


import unittest
from sys import argv
if argv[-1] == None:
    print(argv[-1])
    URL = argv[-1]
else:
    URL = 'testing environment'
    print(URL)

class SkipExample(unittest.TestCase):

    @unittest.skip('用例 1 无条件跳过')
    def test_case_one(self):
        print('---用例 1 ---')


if __name__ == '__main__':
    unittest.main(verbosity=2)
