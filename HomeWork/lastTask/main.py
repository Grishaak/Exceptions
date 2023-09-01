from Module.Service import ServiceBank
from Module.Errors.InsufficientFundsException import InsufficientFundsException
from Module.Errors.MaxBalanceExceededException import MaxBalanceExceededException

if __name__ == '__main__':
    # try:
    bank_off = ServiceBank("Зенирoff")
    bank_off.add_account("Иванов Иван Иваныч", 1000)
    bank_off.add_account("Василий Вася Васильевич", 10000)
    print(bank_off)
    # bank_off.refill_account(0, 3000)
    # bank_off.refill_account(0, 1000)
    bank_off.withdraw_account(1, 3000)
    bank_off.withdraw_account(1, 3000)
    bank_off.withdraw_account(1, 3000)
    bank_off.withdraw_account(1, 3000)
    bank_off.withdraw_account(1, 3000)
    bank_off.refill_account(1, 100000)
    print(bank_off)
# except InsufficientFundsException:
#     print(InsufficientFundsException)
# except MaxBalanceExceededException:
#     print(MaxBalanceExceededException)
