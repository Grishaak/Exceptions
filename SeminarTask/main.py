from seminars_exeptions.SeminarTask.Calculator import Calculator
from seminars_exeptions.SeminarTask.CalculatorException import CalculatorException

from seminars_exeptions.SeminarTask.SubtractionException import SubtractionException

if __name__ == "__main__":
    try:
        result1 = Calculator.add(1231232131313, 20)
        print(f"Addition result: {result1}")

        result2 = Calculator.divide(50, 0)
        print(f"Division result: {result2}")
    except CalculatorException as e:
        print(f"Calculator Exception: {e}")

    try:
        result3 = Calculator.subtract(50, 20)
        print(f"Subtraction result: {result3}")

        result4 = Calculator.subtract(10, 30)
        print(f"Subtraction result: {result4}")
    except SubtractionException as e:
        print(f"Subtraction Exception: {e}")
