import unittest
import Questionaire

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("ENTJ", Questionaire.result())


if __name__ == '__main__':
    unittest.main()
