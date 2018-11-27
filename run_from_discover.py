# encoding:utf8

import unittest
import os
import sys

dir_how_to_run_test_case = os.path.dirname(os.path.abspath(__file__))
dir_test_case = dir_how_to_run_test_case + '/test_case'

discover = unittest.defaultTestLoader.discover(dir_test_case, pattern='test*.py')
# discover = unittest.TestLoader().discover(dir_test_case, pattern='test*.py')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(discover)
