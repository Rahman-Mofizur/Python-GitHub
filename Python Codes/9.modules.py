# A module is basically a file containing a set of functions to include in your application. There are [1]core python modules, [2]modules you can install using the pip package manager (including Django) as well as [3]custom modules.


# [1]core python modules


from validator import validate_email
from validator import validate_email2
import validator
import time
from datetime import date
import datetime            # Here datetime is a module/file
# Datetime is a module, date.today() is a method/function
today = datetime.date.today()
print(today)


today = date.today()
print(today)


timenow = time.time()   # Here, time is a module and time() is a method/ function
print(timenow)

# from time import time
# time1 = time()
# print(time1)


# Import Custom Module


email = 'mohammed@gamil.com'
if validate_email(email):
    print('Email is valid!')
else:
    print('Email is invalid! Please enter a valid email address')


email2 = 'mohammedeiman0177@gmail.com'                # Variable: email2
# Validate_email2(variable pass here)------- if true then print
if validate_email2(email2):
    print('Congratulation! Your email is valid.')
else:                                                 # if false then print sorry
    print('Sorry! Your email is invalid. Please, emnter a valid email address.')
