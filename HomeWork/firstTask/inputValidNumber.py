from InvalidNumberException import InvalidNumberException


class inputPositiveNumber:

    @staticmethod
    def positiveNumber():
        pos_number = int(input("Введите положительное число: "))
        if pos_number <= 0:
            raise InvalidNumberException("Некорректное число", "inputPositiveNumber")
        return pos_number
