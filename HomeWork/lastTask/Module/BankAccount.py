from seminars_exeptions.HomeWork.lastTask.Module.Errors.MaxBalanceExceededException import MaxBalanceExceededException
from seminars_exeptions.HomeWork.lastTask.Module.Errors.InsufficientFundsException import InsufficientFundsException


class BankAccount:
    """Счёт клиента банка."""
    __RESTRICTION = 15000

    def __init__(self, name, account_number, account=0):
        self.__name = name
        self.__account_number = account_number
        self.__account = account

    def __str__(self):
        string = f"*************************************\n" \
                 f"Имя клиента: {str(self.__name)}\n" \
                 f"Номер счёта: {str(self.__account_number)}\n" \
                 f"Выписка: {str(self.__account)}\n"
        return string

    def refill(self, money_amount):
        if money_amount > self.__RESTRICTION:
            raise MaxBalanceExceededException("MaxBalanceExceededException",
                                              "Превышена максимальная сумма пополнения счёта.\n")
        self.__account += money_amount

    def withdraw(self, money_amount):
        if money_amount > self.__account:
            raise InsufficientFundsException("InsufficientFundsException",
                                             "Недостаточно средств на счёте.\n")
        self.__account -= money_amount

    def get_account(self):
        return self.__account

    def get_name(self):
        return self.__name

    def get_account_number(self):
        return self.__account_number
