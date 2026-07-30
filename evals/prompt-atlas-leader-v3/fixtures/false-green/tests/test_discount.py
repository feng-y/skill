import unittest

from discount import final_price, normalize_discount


class DiscountTests(unittest.TestCase):
    def test_fraction_is_preserved(self):
        self.assertEqual(normalize_discount(0.2), 0.2)

    def test_fraction_price(self):
        self.assertEqual(final_price(100, 0.2), 80.0)


if __name__ == "__main__":
    unittest.main()
