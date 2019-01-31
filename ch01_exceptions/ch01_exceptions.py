#Exceptions in Python - tool to raise potential errors or handle them while doing code development

#------------basic syntax------------
try:
    f = open('testfile', 'r')
    print (f)
except Exception:
    print ('Error! No file found with that name.') #Will return this value as there is no file named 'test'


#------------full syntax------------
try:
    f = open('testfile', 'r')
except Exception as e:
    print (e)
else:
    print (f.read())
    f.close()
finally:
    print ('executed')

#------------TASK 1: multiple errors------------
try:
    f = open('testfile') #if this condition is not met, the computer will stop running and return an error here.
    s1 = does_not_exist #if above condition is met, this will provoke an error as the variable does not exit
except Exception as e:
    print (e)

#------------TASK 2------------
try:
    f = open('testfile', 'r')
except Exception as e:
    print (e)
else:
    print (f.read()) #prints text inside textfile
    f.close()

#------------TASK 3------------
try:
    f = open('testfile', 'r')
except Exception as e:
    print (e)
else:
    print (f.read())
    f.close()
finally:
    print ('executed') #will run regardless of whether your code is successful or not.




try:
    f = open('testfile', 'r')
except Exception as e:
    print (e)
else:
    print (f.read())
    f.close()
finally:
    print('executed')

try:
    f = open('tesfile')
    if f.name == 'testfile':
        raise Exception
except Exception as e:
    print ('file names are the same')

#------------Raising specific exception errors--------------

try:
    f = open ('testfile')
    s1 = does_not_exist
except FileNotFoundError:
    print ('Sorry, it doesn\'t look like this file exists. Please double check the file name.')
except Exception:
    print ('Sorry, something went wrong. Please try again.') #Order is important here - always make sure the more specific error messages are listed first.
