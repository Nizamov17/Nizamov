class Good:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def calc(self):
        self.cost = self.price * self.weight

apple = Good('apple', 100, 1.5)
pear = Good('pear', 120, 0.8)

apple.calc()
pear.calc()

print("Стоимость яблок: ", apple.cost)
print("Стоимость груш: ", pear.cost)