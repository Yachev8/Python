import unittest

class FirstTest(unittest.TestCase):
    def test_1(self):
        num1 = 5
        num2 = 10
        result = num1+num2
        assert result == 15

    def test_2(self):
        num1 = 10
        num2 = 50
        result = num1*num2
        self.assertEqual(result,500)


if __name__ == '__main__':
    unittest.main()
