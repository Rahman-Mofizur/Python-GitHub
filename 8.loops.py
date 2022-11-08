# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['Mofiz', 'Mahjabin', 'Farzana', 'Abdullah', 'Tasnim']

# Simple for loop
for person in people:
    # print(f'Current person: {person}')
    if person == 'Abdullah':
        # break      # Stops where Abdullah found
        continue     # Skip Abdullah then continue to the next index
    print(f'People : {person}')

print(len(people))


# Range
family = ['Ilias', 'Beby', 'Mofiz', 'Farzana', 'Abdullah', 'Tasnim']
for person in range(len(family)):
    print(family[person])
    print(f'Current person: {family[person]}')


# Range Numbers
for i in range(0, 10):   # for(i=0; i>10; i++)
    print(i)
    print(f'Numbers: {i}')


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print(count)
    count += 1
