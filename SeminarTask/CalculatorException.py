class CalculatorException(Exception):
    def __init__(self, operation, error_message):
        self.operation = operation
        self.error_message = error_message

    def __str__(self):
        return f"Error during {self.operation}" \
               f" operation: {self.error_message}"
