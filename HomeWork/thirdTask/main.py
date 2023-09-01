# Напишите программу, которая запрашивает у пользователя три числа и выполняет следующие проверки:
#
# Если первое число больше 100, выбросить исключение NumberOutOfRangeException с сообщением "Первое число вне допустимого диапазона".
# Если второе число меньше 0, выбросить исключение NumberOutOfRangeException с сообщением "Второе число вне допустимого диапазона".
# Если сумма первого и второго чисел меньше 10, выбросить исключение NumberSumException с сообщением "Сумма первого и второго чисел слишком мала".
# Если третье число равно 0, выбросить исключение DivisionByZeroException с сообщением "Деление на ноль недопустимо".
# В противном случае, программа должна выводить сообщение "Проверка пройдена успешно".
# - необходимо создать 3 класса собвстенных исключений

from operation import Operation
from DivisionByZeroException import DivisionByZeroException
from NumberOutOfRangeException import NumberOutOfRangeException
from NumberSumException import NumberSumException

#
if __name__ == "__main__":
    test = Operation.test(30, 20, 40)
    print(test)

    test1 = Operation.test(120, 20, 40)
    print(test1)

    test2 = Operation.test(23, -10, 40)
    print(test2)

    test3 = Operation.test(3, 3, 10)
    print(test2)

    test4 = Operation.test(23, 10, 0)
    print(test4)

    test5 = Operation.test(200, -100, 0)
    print(test5)
