from seminars_exeptions.HomeWork.InternetShop.Model.Client.ClientDataBase import ClientDateBase
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.DateBaseErrors.CategoryNotFoundError import \
    CategoryNotFoundError
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.ClientErrors.ClientRefillRestrictionError import \
    ClientRefillRestrictionError
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.DateBaseErrors.DateBaseEmptyError import \
    DateBaseEmptyError
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.DateBaseErrors.ExceedDemandedQuantityError import \
    ExceedDemandedQuantityError
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.ClientErrors.NotClientFoundError import \
    NotClientFoundError
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.DateBaseErrors.ProductNotFoundError import \
    ProductNotFoundError
from seminars_exeptions.HomeWork.InternetShop.Model.Product.ManageDateBase import ManageProduct
from seminars_exeptions.HomeWork.InternetShop.Model.Exceptions.DateBaseErrors import InvalidEntityAppendError
from seminars_exeptions.HomeWork.InternetShop.View.Messages import *
from seminars_exeptions.HomeWork.InternetShop.Model.Product.Product import Product


class Presenter:

    def __init__(self):
        self.manage = ManageProduct()
        self.client_db = ClientDateBase()

    def add_category(self, category_name):
        try:
            self.manage.add_product_category(category_name)
            return True
        except InvalidEntityAppendError as e:
            print_text(e)

    def add_product(self, category_name, product_name, entity, price):
        try:
            product = Product(product_name, entity, price)
            self.manage.add_product(category_name, product)
            return True
        except CategoryNotFoundError as e:
            print_text(e)

    def del_category(self, category_name):
        try:
            self.manage.delete_category_product(category_name)
            return True
        except CategoryNotFoundError as e:
            print_text(e)

    def del_product(self, category_name, product_name):
        try:
            self.manage.delete_product(category_name, product_name)
            return True
        except CategoryNotFoundError as ce:
            print_text(ce)
        except ProductNotFoundError as pe:
            print_text(pe)

    def purchase_product(self, category_name, product_name, quantity, client_name):
        try:
            product = self.manage.purchase_product(category_name, product_name, quantity)
            price = product.get_price()
            client = self.client_db.get_client(client_name)
            end_price = price * quantity
            client.product_purchased(product, end_price)
            print_text("Все ок")
        except ExceedDemandedQuantityError as e:
            print_text(e)
        except ProductNotFoundError as e:
            print_text(e)
        except NotClientFoundError as e:
            print_text(e)
        except CategoryNotFoundError as e:
            print_text(e)
        except ClientRefillRestrictionError as e:
            print_text(e)
        except IOError as e:
            print_text(e)

    def show_products(self):
        try:
            result = str(self.manage.show_products())
            return result
        except DateBaseEmptyError as e:
            print_text(e)

    def create_client(self, client_name):
        self.client_db.add_client(client_name)

    def refill_for_client(self, amount, client_name):
        try:
            client = self.client_db.get_client(client_name)
            client.refill(amount)
        except NotClientFoundError as e:
            print_text(e)
        except ClientRefillRestrictionError as e:
            print_text(e)

    def show_client(self, client_name):
        try:
            return self.client_db.get_client(client_name)
        except NotClientFoundError as e:
            print_text(e)
