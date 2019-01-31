import unittest
import sys
from prime import is_prime


#This is a class so you can test for a number of different things in the class
class Prime_test(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertIsInstance(5.1, int)

    # def test_int(self):
    #     self.assertIsInstance(3, int)

# if __name__ == '__main__':
#     unittest.main()
