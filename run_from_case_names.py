# encoding:utf8

import unittest
import sys
import os

dir_run_test_case = os.path.dirname(os.path.abspath(__file__))
dir_test_case = dir_run_test_case + '/test_case'
sys.path.insert(0, dir_test_case)

cases = ['test_sub.SubCase.test_sub_1','test_add.AddCase.test_add_1']
suite = unittest.TestLoader().loadTestsFromNames(cases)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
