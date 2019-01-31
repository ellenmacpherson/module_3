#Mainains the sanctity of the code

#A way to validate data input. THe most common way code fails is through invalid input.

#Your code is only as good as the test you write

#More useful in the development process - because it's modular, it does not cause ripple effects and you can pinpoint exactly where the bugs are very quickly.

"""Syntax for unit tests:
- assertEqual (a, b) - tests a and b are equal
- assertNotEqual (a, b) - tests a and b are not equal
- assertIn (a, b) - checks that a is in the item b
- assertFalse (a) - checks that the value of a is false
- assertTrue (a) - checks that the value of a is true
- assertIsInstance (a, TYPE)


"""

def is_prime(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True
