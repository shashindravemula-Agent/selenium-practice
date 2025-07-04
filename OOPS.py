class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num

obj = Calculator(2, 3)
print(obj.ummation())