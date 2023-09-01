from seminars_exeptions.SeminarTask.SubtractionException import SubtractionException
from seminars_exeptions.SeminarTask.CalculatorException import CalculatorException


class Calculator:
    # Метод для вычитания
    @staticmethod
    def subtract(a, b):
        if a < b:
            raise SubtractionException("subtraction", a, b, "Negative result not allowed")
        return a - b

    # Метод для сложения
    @staticmethod
    def add(a, b):
        if a > 2147483647 - b:
            raise CalculatorException("addition", "Integer overflow occurred")
        return a + b

    # Метод для деления
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise CalculatorException("division", "Division by zero is not allowed")
        return a // b
