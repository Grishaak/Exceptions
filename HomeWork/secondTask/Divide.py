from DivisionByZeroException import DivisionByZeroException


class Divide:
    @staticmethod
    def division():
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе положительное число число: "))
        if b == 0:
            raise DivisionByZeroException("Деление на ноль", "DivisionByZeroException")
        return a / b
