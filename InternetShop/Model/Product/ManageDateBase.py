from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.CategoryNotFoundError import \
    CategoryNotFoundError
from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.DateBaseEmptyError import \
    DateBaseEmptyError
from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.ExceedDemandedQuantityError import \
    ExceedDemandedQuantityError
from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.InvalidEntityAppendError import \
    InvalidEntityAppendError
from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.ProductNotFoundError import \
    ProductNotFoundError
from seminars_exeptions.InternetShop.Model.Product.ProductListCategory import ProductListCategory


class ManageProduct:
    """Сервис для просмотра и управления базой данных."""

    def __init__(self):
        self.__date_base_product = dict()

    def add_product_category(self, category_name):
        if category_name not in self.__date_base_product.keys():
            new_prod_list = ProductListCategory(category_name)
            self.__date_base_product[category_name] = new_prod_list
        else:
            raise InvalidEntityAppendError("InvalidEntityAppendError",
                                           "Попытка повторного создания уже существующей категории.")

    def add_product(self, category_name, product):
        if category_name not in self.__date_base_product.keys():
            raise CategoryNotFoundError("CategoryNotFoundError", "Отсутствие товарной категории.")
        product_list = self.__date_base_product.get(category_name)
        product_list.add_product(product)
        self.__date_base_product[category_name] = product_list

    def delete_category_product(self, category_name):
        if category_name not in self.__date_base_product.keys():
            raise CategoryNotFoundError("CategoryNotFoundError", "Отсутствие товарной категории.")
        self.__date_base_product.pop(category_name)

    def delete_product(self, category_name, product_name):
        if category_name not in self.__date_base_product.keys():
            raise CategoryNotFoundError("CategoryNotFoundError", "Отсутствие товарной категории.")
        try:
            product_list = self.__date_base_product.get(category_name)
            product_list.del_product(product_name)
            self.__date_base_product[category_name] = product_list
        except ProductNotFoundError:
            raise ProductNotFoundError("ProductNotFoundError", "Товар не найден.")

    def purchase_product(self, category_name, product_name, quantity):
        if category_name not in self.__date_base_product.keys():
            raise CategoryNotFoundError("CategoryNotFoundError", "Отсутствие товарной категории.")
        try:
            product_list = self.__date_base_product.get(category_name)
            product = product_list.get_product(product_name, quantity)
            return product
        except ExceedDemandedQuantityError:
            raise ExceedDemandedQuantityError("ExceedDemandedQuantityError", "Превышение лимита запрашиваемого товара.")
        except ProductNotFoundError:
            raise ProductNotFoundError("ProductNotFoundError", "Отсутствие товара")

    def __str__(self):
        if not self.__date_base_product.values():
            raise DateBaseEmptyError("DateBaseEmptyError", "База данных пуста.")
        else:
            result = ""
            for product in self.__date_base_product.values():
                result += product.show_list()
            return result

    def show_products(self):
        return str(self.__str__())
