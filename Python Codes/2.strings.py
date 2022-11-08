# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


Name = 'Mohammed Mofizur Rahman'
age = 22
# 1 Concatination
# print('Hello! My name is ' + Name + 'My age is ' + str(age))

# 2 String Formatting
# Formatting: Arguments by position
# print('My name is {myname} and I am {myage} years old.'.format(
#     myname=Name, myage=age))


# 3 Print string Using F-string
print(f'Hello! My name is {Name} and I am {age} years old.')


# 4 String Methods
a = 'hello World'

print(a.capitalize())

print(a.upper())

print(a.lower())

print(a.swapcase())

# Length of string
print(len(a))

# Replace
print(a.replace('World', 'Everyone'))
