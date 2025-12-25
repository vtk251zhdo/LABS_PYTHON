import unittest
from shop import Shop, Discount

class TestShop(unittest.TestCase):

    def setUp(self):
        self.shop = Shop("MegaStore", "electronics")
    
    def test_shop_attributes(self):
        self.assertEqual(self.shop.shop_name, "MegaStore")
        self.assertEqual(self.shop.store_type, "electronics")
        self.assertEqual(self.shop.number_of_units, 0)

    def test_set_number_of_units(self):
        self.shop.set_number_of_units(10)
        self.assertEqual(self.shop.number_of_units, 10)

    def test_set_invalid_units(self):
        with self.assertRaises(ValueError):
            self.shop.set_number_of_units(-5)

class TestDiscount(unittest.TestCase):

    def test_discount_products(self):
        discount = Discount(
            "SaleShop",
            "tech",
            ["laptop", "smartphone", "tablet"]
        )
        self.assertIn("laptop", discount.discount_products)
        self.assertEqual(len(discount.discount_products), 3)

if __name__ == '__main__':
    unittest.main()