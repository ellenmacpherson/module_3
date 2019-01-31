import unittest
from primes import is_prime

class PrimesTestCase(unittest.TestCase):
    #Tests for primes.py
    def test_is_prime(self):        #For these tests to run, the function name must start with 'test'
        #Is five successfully evaluated as a prime?
        self.assertTrue(is_prime(5))

    # def test_four(self):
    #     #Is four correctly evaluated as non-prime?
    #     self.assertTrue(is_prime(4), msg = "Four is not prime!") #Failing a test as expected

    def test_zero(self):
        #Is zero correctly evaluated as non-prime?
        self.assertFalse(is_prime(0))

    def test_negative_number(self):
        #Is a negative number correctly evaluated as non-prime?
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))

if __name__ == '__main__':
    unittest.main()
