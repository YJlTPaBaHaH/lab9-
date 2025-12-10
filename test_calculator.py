import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # --- add ---
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 5), 4)
        self.assertEqual(self.calc.add(0, 0), 0)

    # --- subtract ---
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # --- multiply ---
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, 3), -9)

    # --- divide ---
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    # --- is_prime_number ---
    def test_is_prime_number(self):
        self.assertTrue(self.calc.is_prime_number(2))
        self.assertTrue(self.calc.is_prime_number(17))
        self.assertFalse(self.calc.is_prime_number(4))
        self.assertFalse(self.calc.is_prime_number(1))

if __name__ == '__main__':
    unittest.main()
