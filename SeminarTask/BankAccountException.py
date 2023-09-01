class BankAccountException(Exception):
    def __init__(self, account_number, operation, error_message):
        self.account_number = account_number
        self.operation = operation
        self.error_message = error_message

    def __str__(self):
        return f"Error for account {self.account_number}" \
               f" during {self.operation} operation: {self.error_message}"
