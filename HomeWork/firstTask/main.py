from InvalidNumberException import InvalidNumberException
from inputValidNumber import inputPositiveNumber


def main():
    try:
        pos_number = inputPositiveNumber.positiveNumber()
        print(f"Число {pos_number} - положительное")
    except InvalidNumberException as e:
        print(e)
        print(f"Введеное число не явяется положительным")


main()
