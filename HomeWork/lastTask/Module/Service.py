# from Bank import Bank
from threading import Thread

from seminars_exeptions.HomeWork.lastTask.Module.Bank import Bank
from seminars_exeptions.HomeWork.lastTask.Module.BankAccount import BankAccount
from seminars_exeptions.HomeWork.lastTask.Module.Errors.InsufficientFundsException import InsufficientFundsException
from seminars_exeptions.HomeWork.lastTask.Module.Errors.MaxBalanceExceededException import MaxBalanceExceededException


class ServiceBank:
    """Кластер управления банком и банковскими аккаунтами."""
    __list_accounts = {}
    __account_number = 0

    def __init__(self, name):
        bank = Bank(name)
        self.bank = bank

    def add_account(self, name, account=0):
        new_account = BankAccount(name, self.__account_number, account)
        self.__list_accounts[self.__account_number] = new_account
        self.__account_number += 1

    def __refill_account(self, account_number, money_amount):
        bank_account = self.get_account(account_number)
        if bank_account:
            try:
                bank_account.refill(money_amount)
            except MaxBalanceExceededException as e:
                print(e)
            return "Опреация прошла успешно."

    def __withdraw_account(self, account_number, money_amount):
        bank_account = self.get_account(account_number)
        if bank_account:
            try:
                bank_account.withdraw(money_amount)
            except InsufficientFundsException as e:
                print(e)
            return "Опреация прошла успешно."

    def withdraw_account(self, account_number, money_amount):
        thread = Thread(target=self.__withdraw_account, args=(account_number, money_amount,))
        thread.start()
        thread.join(5)

    def refill_account(self, account_number, money_amount):
        try:
            thread = Thread(target=self.__refill_account, args=(account_number, money_amount,))
            thread.start()
            thread.join(5)
        except MaxBalanceExceededException:
            return "Опреация прервалась."
        return "Опреация прошла успешно."

    def get_account(self, account_number):
        if account_number not in self.__list_accounts.keys():
            return None
        return self.__list_accounts.get(account_number)

    def __str__(self):
        string = ""
        for account in self.__list_accounts.values():
            string += str(account)
        return string
