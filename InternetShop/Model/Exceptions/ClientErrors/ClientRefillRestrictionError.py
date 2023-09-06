class ClientRefillRestrictionError(Exception):
    def __init__(self, error, message):
        self.error = error
        self.message = message

    def __str__(self):
        return f"Ошибка: {self.error}\n" \
               f"{self.message}"
