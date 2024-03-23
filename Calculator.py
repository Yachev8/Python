import unittest


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divice(self, x, y):
        return x / y


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtrach(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calculator.multiply(5, 5)
        self.assertEqual(result, 25)

    def test_devide(self):
        result = self.calculator.divice(10, 2)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
