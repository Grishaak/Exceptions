from Messages import scaner, print_text, error_text, general_menu, menu_admin, menu_client
from seminars_exeptions.HomeWork.InternetShop.Presenter.Presenter import Presenter


def start():
    match_general()


def match_general():
    presenter = Presenter()
    while True:
        print_text(general_menu)
        choice = input("\nВведите цифру действия: ")
        if choice == "1":
            match_admin(presenter)
        elif choice == "2":
            match_client(presenter)
        elif choice == "3":
            return


def match_admin(presenter):
    while True:
        print_text(menu_admin)
        choice = scaner()
        match choice:
            case "1":
                category = input("Введите категорию которую хотите добавить: ")
                flag = presenter.add_category(category)
                if flag:
                    print_text("Категория добавлена.")
            case "2":
                category = input("Введите категорию товара : ")
                product_name = input("Введите товар который хотите добавить: ")
                quantity = int(input("Введите кол-во товара: "))
                price = int(input("Введите цену товара за штуку: "))
                flag = presenter.add_product(category, product_name, quantity, price)
                if flag:
                    print_text("Товар успешно добавлен.")
            case "3":
                x = presenter.show_products()
                if x is not None:
                    print_text(x)
            case "4":
                category = input("Введите категорию товара : ")
                flag = presenter.del_category(category)
                if flag:
                    print_text("Категория удалена.")
            case "5":
                category = input("Введите категорию товара : ")
                product_name = input("Введите название товара : ")
                flag = presenter.del_product(category, product_name)
                if flag:
                    print_text("Категория удалена.")
            case "6":
                return
            case _:
                print_text(error_text)


def match_client(presenter):
    while True:
        print_text(menu_client)
        choice = scaner()
        match choice:
            case "1":
                client_name = input("Введите имя новго клиента: ")
                presenter.create_client(client_name)
            case "2":
                category = input("Введите категорию товара : ")
                product_name = input("Введите название товара : ")
                quantity = int(input("Введите кол-во товара который хотите приобрести : "))
                client_name = input("Введите имя клиента: ")
                flag = presenter.purchase_product(category, product_name, quantity, client_name)
                if flag:
                    print_text("Покупка успешно произведена.")
            case "3":
                x = presenter.show_products()
                if x is not None:
                    print_text(x)
            case "4":
                client_name = input("Введите имя клиента: ")
                refill_amount = int(input("Введите сумму пополнения: "))
                presenter.refill_for_client(refill_amount, client_name)
            case "5":
                client_name = input("Введите имя клиента: ")
                client = presenter.show_client(client_name)
                print_text(client)
            case "6":
                return
            case _:
                print_text(error_text)