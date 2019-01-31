class Calculator():

    def __init__self(self):
        pass

    def add(self, x, y):
        number_types = (int, float, complex)
        try:
            if isinstance(x, number_types) and isinstance(y, number_types):
                return x + y
        except ValueError:
            return ValueError

    def subtract(self, x, y):
        number_types = (int, float, complex)
        try:
            if isinstance(x, number_types) and isinstance(y, number_types):
                return x - y
        except ValueError:
            return ValueError


    def multiply(self, x, y):
        number_types = (int, float, complex)
        try:
            if isinstance(x, number_types) and isinstance(y, number_types):
                return x * y
        except ValueError:
            return ValueError

    def divide(self, x, y):
        number_types = (int, float, complex)
        try:
            if isinstance(x, number_types) and isinstance(y, number_types):
                return x / y
        except ValueError:
            return ValueError
