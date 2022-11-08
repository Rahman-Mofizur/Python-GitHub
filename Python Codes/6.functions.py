# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Method: 1
def func(name, age):
    print(f'My name is {name} and I am {age} years old.')


func('Mohammed Mofizur Rahman', 22)    # With Argument


#Method: 2
def func2(name='Mohammed Ilisa Azam Chowdhury', age='52'):
    print(f"My father's name is {name} and he is {age} years old.")


func2()             # Without Argument

#   Return Value


def func3(num1, num2):
    total = num1 + num2
    print(total)


func3(20, 50)


def func4(num3, num4, num5, num6):
    math = num3+num4*num5-num6
    print(math)


func4(30, 4, 5, 5)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

# You have to disable prettier extension OR
# You have to edit on "editor.formatOnSave" : false

# getsum = lambda num8, num9: num8 + num9
# print(getsum(10, 5))
