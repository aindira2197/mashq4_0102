class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  # private

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price


banana = Fruit("Banan", 8000)
print(banana.get_price())
banana.set_price(9000)
print(banana.get_price())
