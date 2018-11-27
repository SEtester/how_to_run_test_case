# encoding:utf8

import unittest
from test_case import test_add

cases = unittest.TestLoader().loadTestsFromModule(test_add)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(cases)
