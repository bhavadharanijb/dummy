import unittest
import calc

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2,3), 5)
    def test_sub(self):
        self.assertEqual(calc.add(2,3), -1)


if __name__ == '__main__':
    unittest.main()
