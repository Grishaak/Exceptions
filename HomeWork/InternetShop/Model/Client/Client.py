from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.ClientErrors.ClientRefillRestrictionError import \
    ClientRefillRestrictionError
from seminars_exeptions.HomeWork.InternetShop.Model.Product.Product import Product


class Client:
    log_list = "log_client.txt"

    def __init__(self, name):
        self.name = name
        self.money_value = 0

    def __str__(self):
        return f"Имя клиента: {self.name}\n" \
               f"Счёт клиента: {self.money_value}"

    def refill(self, refill_amount):
        if refill_amount > 150000:
            raise ClientRefillRestrictionError("ClientRefillRestrictionError", "Превышение лимита по внесению средств.")
        self.money_value += refill_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.money_value:
            raise ClientRefillRestrictionError("ClientRefillRestrictionError", "Недостаточно средств.")
        self.money_value -= withdraw_amount

    def product_purchased(self, product: Product, amount):
        try:
            self.withdraw(amount)
            with open(self.log_list, "w") as file:
                file.write(self.name)
                file.write("Приобретенные товары: ")
                file.write(str(product))
                return True
        except IOError:
            raise IOError
        except ClientRefillRestrictionError:
            raise ClientRefillRestrictionError("ClientRefillRestrictionError", "Недостаточно средств.")
