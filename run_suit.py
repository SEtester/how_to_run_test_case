#encoding:utf8

import unittest
from test_case.test_add import AddCase
from test_case.test_sub import SubCase

cases = unittest.TestSuite()
cases.addTest(SubCase("test_sub_2"))
cases.addTest(AddCase("test_add_2"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(cases)

