class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"\nТовар : {self.name}" \
               f"\nКоличество товара на складе(х): {self.quantity}" \
               f"\nЦена за еденицу товара: {self.price}"

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

    # @property
    # def name(self):
    #     return self.name
    #
    # @name.setter
    # def name(self, new_name: str):
    #     # if name != "":
    #     self.name = new_name
    #
    # @property
    # def quantity(self):
    #     return self.quantity
    #
    # @quantity.setter
    # def quantity(self, quantity: int):
    #     if quantity > 0:
    #         self.quantity = quantity
    #
    # @property
    # def price(self):
    #     return self.price
    #
    # @price.setter
    # def price(self, price: int):
    #     if price > 0:
    #         self.price = price
