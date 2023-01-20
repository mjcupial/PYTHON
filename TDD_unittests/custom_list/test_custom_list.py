import unittest
from mytest import *

class MyFirstTest(unittest.TestCase):
    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_customfunc_x(self):
        self.assertEqual(custom_func_x(3,2,3), 54)

    def test_custom_func_x(self):
        self.assertEqual(custom_non_lin_list(5,2,3)[2], 16)
        self.assertEqual(custom_non_lin_list(5, 3, 2)[4], 48)

if __name__ == '__main__':
    unittest.main()