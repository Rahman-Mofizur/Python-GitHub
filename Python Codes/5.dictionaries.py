# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# Create dictionary
person = {
    'first_name': 'Mohammed Mofizur',
    'last_name': 'Rahman',
    'age': 22,
    'gender': 'Male'
}

# Create dictionary using Constructor
person2 = dict(first_name='Sara', last_name='Hafiza')
print(person2, type(person2))

# Get value
# 1
print(person['gender'])
# 2
print(person.get('first_name'), person.get('age'))


# Add a member to the dictionary
person['phone'] = '+8801779746565'

# Get Keys
print(person.keys())

# Get Items
print(person.items())

# Copy dictionary
person2 = person.copy()
person2['city'] = 'Chittagong'
print(person2)

# Removing an item/member
del (person['age'])
person.pop('last_name')
print(person)

# Clear the dictionary
person.clear()  # delete does NOT work for dictionary, so use clear
print(person)

# List of dictionary
person3 = [
    {'name': 'Maria', 'age': 20},
    {'name': 'Maruf', 'age': 22}
]
print(person3, type(person3))

# A person's name print
print(person3[1]['age'], person3[0]['name'])

print(person)
