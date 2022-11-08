# If/ Else conditions are used to decide to do something based on something being true or false

x = 70
y = 100

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
# Simple If / Else if and / Else
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested If
if x > 50:
    if x < 100:
        print(f'{x} is greater than 50 and less than 100')

# Logical operators (and, or, not) - Used to combine conditional statements
if x > 70 and x < 100:
    print(f'x is equal to {x}')

if x > 70 or x < 100:
    print(f'x = {x}')

if not (x == y):
    print(f'x which is {x}, is not equal to y')
else:
    print(f'x which is {x}, is equal to y')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
Numbers = [10, 30, 50, 70, 90]

if x in Numbers:
    print(x in Numbers)     # Return type : True or False
    print(f'{x} is in Numbers list')

if x not in Numbers:
    print(x not in Numbers)     # Return type : True or False
    print(f'{x} is not existed in Numbers list')

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is 70:
    print(x is 70)     # Return type : True or False
    print(f'{x} is equal to 70')

if x is not 70:
    print(x is not 70)     # Return type : True or False
    print(f'{x} is not equal to 70')
