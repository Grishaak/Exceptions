class Bank:
    """Банк для содержания клиентских счётов."""
    __list_accounts = {}
    __account_count = 0

    def __init__(self, bank_name):
        self.bank_name = bank_name



    # def __add_account(self, name, account=0):
    #     new_account = BankAccount(name, self.__account_count, account)
    #     self.__list_accounts[self.__account_count] = new_account

    # def refill_account(self, account_number, money_amount):
    #     bank_account = self.get_account(account_number)
    #     bank_account.BankAccount.refill_account(money_amount)
    #
    # def get_account(self, account_number):
    #     if account_number not in self.__list_accounts.keys():
    #         return None
    #     return self.__list_accounts.get(account_number)
