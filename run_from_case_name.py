# encoding:utf8

import unittest
import os
import sys
dir_run_test_case = os.path.dirname(os.path.abspath(__file__))
dir_test_case = dir_run_test_case + '/test_case'
sys.path.insert(0,dir_test_case)

# loadTestsFromName 这个方法是从sys.path的目录下寻找匹配的测试用例
# cases= unittest.TestLoader().loadTestsFromName('test_add.AddCase.test_add_1')
'''
test_add   是 Module （文件名）
AddCase    是 unittest.TestCase的测试类  （类名）
test_add_1 是 unittest.TestCase 下的测试用例   （测试用例的名字）
'''
cases= unittest.TestLoader().loadTestsFromName('test_add.AddCase.test_add_1')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(cases)
