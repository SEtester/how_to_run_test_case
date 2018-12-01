# encoding:utf8

import unittest
from test_case.test_add import AddCase

cases = unittest.TestLoader().loadTestsFromTestCase(AddCase)
runner = unittest.TextTestRunner(verbosity=2)
runner.run(cases)
