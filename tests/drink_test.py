import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self): 
        self.drink_1 = Drink("Butter Beer", 2, 2) 
        self.drink_2 = Drink("Fire Whiskey", 5, 8) 

    def test_drink_has_name(self): 
        self.assertEqual("Butter Beer", self.drink_1.name) 

    def test_drink_has_price(self): 
        self.assertEqual(5, self.drink_2.price) 
