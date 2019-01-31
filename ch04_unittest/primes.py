def is_prime(number):
    if number <= 1:
        return False

    for num in range(2, number):
        if number % num == 0:
            return False
    return True

def print_next_prime(number):
    #Print the closest prime number larger than number
    index = number
    while True:
        index += 1
        if is_prime(index):
            print (index)



#Sample result below:

# Ellens-MacBook-Pro:ch04_unittest ellenmacpherson$ python test.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
# Ellens-MacBook-Pro:ch04_unittest ellenmacpherson$
