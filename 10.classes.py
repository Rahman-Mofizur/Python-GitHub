# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class user:
    # Constructor
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa

    # Method/Function to pass the value of self object- person1 or person2 or person3 or etc...

    def greeting(self):
        return f'My name is {self.name} and my id is {self.id}'


# Initialize user object
person1 = user('Mohammed Mofizur Rhaman', '19-40120-1', '3.66')
print(type(person1))
print(person1.name, person1.id, person1.cgpa,)
print(f"I am " + person1.name + ". My id is " + person1.id +
      " and my cgpa is " + person1.cgpa+".")
print(person1.greeting())


# Overridding/Extending user class to customer class
class customer(user):
    # Constructor
    def __init__(self, name, id, cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
        self.balance = 0
        # self.starting_date = '10 Oct, 2022'

    def set_balance(self, balance):
        self.balance = balance


person55 = customer('Eiman', '19-40120-1', '3.66')
person55.set_balance("$5000")   # Update balance

print(person55.name, person55.id, person55.cgpa, person55.balance)

print(person55.greeting())
