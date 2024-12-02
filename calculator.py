# calculator.py

class Calculator:
    def abs_add(self, a, b): # pragma: no cover
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b