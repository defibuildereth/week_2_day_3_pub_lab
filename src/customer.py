class Customer:
    def __init__(self, name, wallet, age, drunkenness=0):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.hands = []     # Max 2
        self.drunkenness = drunkenness

    def reduce_money(self, amount):
        self.wallet -= amount

    def add_drink(self, drink): 
        if len(self.hands) <= 2:
            self.hands.append(drink)

    def can_afford(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            return False

    def drink(self):
        self.drunkenness += self.hands[0].alcohol_level
        self.hands.pop(0)


    

