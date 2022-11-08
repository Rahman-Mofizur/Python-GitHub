# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuples with duplicate member/item
# Tuples allow duplicate items
fruits = ('Apples', 'Oranges', 'Grapes', 'Oranges')

# Single parameter
# fruits2 = ('Apple')
# print(type(fruits2))      # Considers as a String

# Using Constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
# print(fruits, fruits2)

# print(type(fruits))     # Considers as a Tuple

# Delete Tuple
# del fruits

# Length of tuple
print(len(fruits))

# Check if the item is in the set
# print('Apples' in fruits)

# Checking index
# print(fruits[0])      # It works

# Tuple can not be clreared   -> Tuples do not have clear attribute

print(fruits)


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Creat Set
# A set does NOT allow duplicate items/members
fruits_set = {'Jackfruits', 'Jackfruits',
              'Watermalons', 'Pears', 'Blackberries', 'Pears'}

# Check if the item is in the set
# print('Apples' in fruits_set)

# Adding an item
fruits_set.add('Banana')

# Does NOT add an item twice
fruits_set.add('Jackfruits')

# Removing an item
# fruits_set.remove('Pears')

# Clearing the set
# fruits_set.clear()

# Delete set
# del fruits_set

print(fruits_set)
