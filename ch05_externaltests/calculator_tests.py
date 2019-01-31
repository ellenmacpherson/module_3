import unittest
from calculator import Calculator


class calculator_testing(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test__add(self):
        result = self.calc.add(2, 2)
        self.assertEqual(result, 4)

    def test__subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_type_subtract(self):
        self.assertRaises(ValueError, self.calc.subtract('seven', 'two'))

    def test_multiply(self):
        result = self.calc.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_type_add(self):
        self.assertRaises(ValueError, self.calc.add('two', 'four'))

if __name__ == '__main__':
    unittest.main()
