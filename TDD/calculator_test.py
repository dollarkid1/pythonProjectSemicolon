import unittest
import calculator


class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = calculator.add(3, 7)
        self.assertEqual(10, result)

    def test_subtract(self):
        result = calculator.subtract(9, 8)
        self.assertEqual(1, result)

    def test_multiply(self):
        result = calculator.multiply(8, 3)
        self.assertEqual(24, result)

    def test_divide(self):
        result = calculator.divide(4,2)
        self.assertEqual(2,result)
        self.ass


if __name__ == '__main__':
    unittest.main()
