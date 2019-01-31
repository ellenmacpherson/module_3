#-------------Data Validation------------

#-------------Task 1: User Input------------

print ("What's your age?") #Prints age on a new line
Age = input()

age = input("What's your age? ") #Prints input followed by a space for input.
print (age)

print (type(Age)) #String data type. Would need to be converted to int for most analysis
print (type(age)) #String data type. Would need to be converted to int for most analysis

#-------------Task 2: Casting into other data types------------

age = int(age)
print (type(age)) #Now an int data type

#More examples:

print ('What year were you born?')
year = int(input())

print (type(year))

phone = int(input("Please enter your phone number. "))

print (phone) #Note that ints do not register the 0 in front of phone numbers. Can deal with this by keeping it as a string or converting 0 to a country code

#-------------Task 3: String functions useful for storing data------------

option = input("Please input yes or no: ").lower() #If you input YES, this will print 'yes'

print(option)

#-------------Task 4: Validating string length------------

print ('What is your phone number?')
number = input()

while True:
    if len(number) == 11:
        continue
    else:
        print ('Please input a valid UK number. This should be 11 characters in length.')
    break
#


#-------------Task 5: Conditionals------------

def choices():

    if choice == 1:
        print ('Ms Macpherson')
    elif choice == 2:
        print ('26')
    elif choice == 3:
        print ('Sydney')
    elif choice <1 or choice >3:
        print ('Please enter a number between 1 and 3.')
        choices() #Runs function again to prompt second user input.

#-------------Task 5: Validating input and handling errors through while loops & Task 6: Where to break in while loops------------

#Note - infinite while loops are dangerous in code, but they're good for user input validation.

# Using Try and Exceptions
print ('Choice 1: Display my name')
print ('Choice 2: Display my age')
print ('Choice 3: Display my city')
choice = int(input('Please enter your choice: '))

while True:
    try:
        if choice == 1:
            print ('Ms Macpherson')
            break
        elif choice == 2:
            print ('26')
            break
        elif choice == 3:
            print ('Sydney')
            break
        while choice <1 or choice > 3:
            choice = int(input('Please enter your choice: '))
            break
    except ValueError:
        print ('Please enter a number.')

#------------Task 7: The assert statment-------------

class Spam(object):
    def __init__(self, description, value):
        if not description or value <=0:
            raise ValueError
        self.description = description
        self.value = value
s = Spam('s', 5)
print (s.value) #Prints 5

s = Spam('s', -1)
print (s.value) #Raises ValueError

class Spam(object):
    def __init__(self, description, value):
        assert description != "", "Description cannot be empty." #Assert statement is essentially shorthand for rasing a ValueError. will print statement after comma.
        assert value > 0, "Value must be greater than 0."
        self.description = description
        self.value = value


s = Spam('s', 5)
print (s.value) #Prints 5

s = Spam('', -1)
print (s.value) #Raises AssertionErrors
