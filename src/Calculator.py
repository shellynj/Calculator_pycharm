import math


def addition(a, b):
    a = int(a)
    b = int(b)
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return c


def division(a, b):
  a = float(a)
  b = float(b)
  return round((b/a),9)


def square(a):
  a = int(a)
  b = a ** 2
  return b


def square_root(a):
  a = float(a)
  b = float(math.sqrt(a))
  return b


class Calculator:
    result = 0

    def __init__(self):
        pass


    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result


    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result


    def divide(self, a, b):
        self.result = division(a, b)
        return self.result


    def squ(self,a):
        self.result = square(a)
        return self.result


    def squ_root(self,a):
        self.result = square_root(a)
        return self.result

