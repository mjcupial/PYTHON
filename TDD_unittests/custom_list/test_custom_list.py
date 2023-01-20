import unittest
from mytest import *

class MyFirstTest(unittest.TestCase):
    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_customfunc_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)

if __name__ == '__main__':
    unittest.main()