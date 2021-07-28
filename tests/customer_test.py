import unittest
from src.customer import Customer
from src.drink import Drink



class TestCustomer(unittest.TestCase):

    def setUp(self): 
        self.customer = Customer("Harry Potter", 200, 26)
        self.drink_1 = Drink("Butter Beer", 2, 2)
        self.drink_2 = Drink("Fire Whiskey", 10, 8)


    
    def test_customer_has_name(self): 
        self.assertEqual("Harry Potter", self.customer.name) 

    
    def test_customer_has_wallet(self): 
        self.assertEqual(200, self.customer.wallet) 

    
    def test_customer_has_age(self): 
        self.assertEqual(26, self.customer.age) 

    def test_drink(self):
        self.customer.add_drink(self.drink_1)
        self.customer.add_drink(self.drink_2)
        self.customer.drink()
        self.assertEqual()
        self.assertEqual()




