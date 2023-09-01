class DivisionByZeroException(Exception):
    def __init__(self, message, exception):
        self.message = message
        self.exception = exception

    def __str__(self):
        return f"Ошибка : {self.exception}\n" \
               f"{self.message}"
