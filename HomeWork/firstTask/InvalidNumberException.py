# Задача 1:
# Напишите программу, которая запрашивает у
# пользователя число и проверяет, является ли оно положительным.
# Если число отрицательное или равно нулю, программа должна
# выбрасывать исключение InvalidNumberException с сообщением
# "Некорректное число". В противном случае, программа должна
# выводить сообщение "Число корректно".


class InvalidNumberException(Exception):
    def __init__(self, message, exception):
        self.message = message
        self.exception = exception

    def __str__(self):
        return f"Ошибка : {self.exception}\n" \
               f"{self.message}"
