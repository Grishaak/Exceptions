from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.ExceedDemandedQuantityError import \
    ExceedDemandedQuantityError
from seminars_exeptions.InternetShop.Model.Exceptions.DateBaseErrors.ProductNotFoundError import \
    ProductNotFoundError
from seminars_exeptions.InternetShop.Model.Product.Product import Product


class ProductListCategory:
    """Управление товарами одной категории."""

    def __init__(self, category_name):
        self.category_name = category_name
        self.product_list = []

    def add_product(self, product: Product):
        self.product_list.append(product)
        return True

    def del_product(self, name_product):
        flag = True
        for product in self.product_list:
            if product.name == name_product:
                self.product_list.remove(product)
                return flag
        if flag:
            raise ProductNotFoundError("ProductNotFoundError", "Товар не найден.")

    def get_product(self, product_name, quantity):
        flag = True
        for product in self.product_list:
            if product.name == product_name:
                if product.quantity >= quantity:
                    return product
                else:
                    raise ExceedDemandedQuantityError("ExceedDemandedQuantityError",
                                                      "Превышение запрашиваемого количества доступного товара.")
        if flag:
            raise ProductNotFoundError("ProductNotFoundError", "Товар не найден.")

    def __str__(self):
        string = ""
        string += f"\nКатегория: {str(self.category_name)}\n"
        for product in self.product_list:
            string += "*********************"
            string += str(product) + "\n"
        string += "*********************\n"
        return string

    def show_list(self):
        return str(self.__str__())
