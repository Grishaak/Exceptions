class SubtractionException(Exception):
    def __init__(self, operation, operand1, operand2, error_message):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.error_message = error_message

    def __str__(self):
        return f"Error during {self.operation} operation:" \
               f" Operand 1: {self.operand1}," \
               f" Operand 2: {self.operand2} - {self.error_message}"
