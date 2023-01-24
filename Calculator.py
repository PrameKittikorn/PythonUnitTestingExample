class Calculator:
    def __init__(self):
        self.total = 0

    def add(self, a, b):
        self.total += a + b
        return self.total

    def subtract(self, a, b):
        self.total -= a + b
        return self.total

    def multiply(self, a, b):
        self.total *= a * b
        return self.total

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        self.total /= a / b
        return self.total
