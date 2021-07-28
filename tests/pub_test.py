import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer


class TestPub(unittest.TestCase):

    def setUp(self):
        self.drink_1 = Drink("Butter Beer", 2, 2)
        self.drink_2 = Drink("Fire Whiskey", 10, 8)
        self.drink_3 = Drink("Giggle Water", 3, 1)
        self.drink_4 = Drink("Wizards Brew", 8, 3)
        self.drink_5 = Drink("Daisyroot Draft", 4, 3)
        self.drink_6 = Drink("Lobe Blaster", 9, 11)
        self.drink_7 = Drink("Mulled Mead", 5, 6)
        self.drink_list = [self.drink_1, self.drink_2, self.drink_3,
                           self.drink_4, self.drink_5, self.drink_6, self.drink_7]
        # 500 sickles - 17 sickles in a galleon
        self.pub = Pub("The Leaky Cauldron", 500, self.drink_list)
        self.customer = Customer("Harry Potter", 200, 26)

    def test_pub_has_name(self):
        self.assertEqual("The Leaky Cauldron", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(500, self.pub.till)

    def test_add_drink(self):
        self.pub.add_drink(self.drink_3)
        self.assertEqual(8, self.pub.count_stock())

    def test_remove_drink(self):
        self.pub.add_drink(self.drink_3)
        self.pub.remove_drink(self.drink_3)
        self.assertEqual(7, self.pub.count_stock())

    def test_add_money(self):
        self.pub.add_money(self.drink_1.price)
        self.assertEqual(502, self.pub.till)

    def test_sell_drink(self):
        self.pub.sell_drink(self.customer, 'Butter Beer')
        self.assertEqual(198, self.customer.wallet)
        self.assertEqual(502, self.pub.till)
        self.assertEqual(6, self.pub.count_stock())
        self.assertEqual(1, len(self.customer.hands))
