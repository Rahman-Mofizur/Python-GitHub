# A variable is a container for a value, which can be of various types

'''
This is a
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
x = 1
y = 2.5
y = int(y)  # Casting y as an Integer.
z = float(y)
name = 'Mohammed Mofizur Rahman'
is_cool = True
a = x + y
p, q, city = (5, 7.5, 'Dhaka')  # Input multiples

# z will be 2.0 cz y turns to integer so that 2.5 -> 2 then, z = 2.0
print(type(x), y, name, is_cool, a, p, q, city, z)
