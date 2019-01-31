from wordcount import wordcount
import unittest

class TestUnit(unittest.TestCase):
    def test_wordcount(self):
        self.assertDictEqual({'foo': 2, 'bar': 1}, wordcount('foo bar foo'))






if __name__ == '__main__':
    unittest.main()
