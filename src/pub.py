class Pub:
    def __init__(self,name, till, initial_stock):
        self.name = name
        self.till = till
        self.drinks = initial_stock     #list
        self.max_drunkenness = 50

    def add_drink(self,drink):
        self.drinks.append(drink)

    def count_stock(self):
        return len(self.drinks)

    def add_money(self, amount): # TODO add drink.price
        self.till += amount

    def remove_drink(self,drink):
        self.drinks.remove(drink)

    def check_stock(self, order):
        for drink in self.drinks:
            if drink.name == order:
                return drink
        return False

    def sell_drink(self, customer, order):
        drink = self.check_stock(order)
        if drink and customer.can_afford(drink) and customer.age >= 18 and customer.drunkenness <= self.max_drunkenness:
            self.remove_drink(drink)
            customer.add_drink(drink)
            self.add_money(drink.price)
            customer.reduce_money(drink.price)
    


