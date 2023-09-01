from NumberOutOfRangeException import NumberOutOfRangeException
from NumberSumException import NumberSumException
from DivisionByZeroException import DivisionByZeroException


class Operation:
    @staticmethod
    def test(a, b, c):
        try:
            Operation.testOutOfRangeFirst(a)
            Operation.testOutOfRangeSecond(b)
            Operation.testSum(a, b)
            Operation.testDivisionZero(c)
        except DivisionByZeroException as e:
            print(e)
            return "Не все числа валидны. Проверка провалена."
        except NumberOutOfRangeException as e:
            print(e)
            return "Не все числа валидны. Проверка провалена."
        except NumberSumException as e:
            print(e)
            return "Не все числа валидны. Проверка провалена."

        return "Проверка пройдена успешно. Все чила валидны."

    @staticmethod
    def testOutOfRangeFirst(n):
        if n > 100:
            raise NumberOutOfRangeException("Первое число вне допустимого диапазона", "NumberOutOfRangeException")
        # print(f"Первое число {n} валидно")

    @staticmethod
    def testOutOfRangeSecond(n):
        if n < 0:
            raise NumberOutOfRangeException("Второе число вне допустимого диапазона", "NumberOutOfRangeException")
        # print(f"Второе число {n} валидно")

    @staticmethod
    def testSum(a, b):
        if (a + b) < 10:
            raise NumberSumException("Сумма первого и второго чисел слишком мала", "NumberSumException")
        # print(f"Сумма чисел {a} и {b} валидна")

    @staticmethod
    def testDivisionZero(c):
        if not c:
            raise DivisionByZeroException("Деление на ноль недопустимо", "DivisionByZeroException")
        # print(f"Число {c} не равно нулю.")
