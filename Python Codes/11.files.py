# Python has functions for creating, reading, updating, and deleting files.

# Create a file named Eiman.txt and put the file on myfile instance/object
myfile = open('Eiman.txt', 'w')  # Mode = Write(w)


# Get some information
print('Name: ', myfile.name)
print('Is closed: ', myfile.closed)
print('Opening mode: ', myfile.mode)


# Write into the file
myfile.write('I love Python ')
myfile.write('and I am learning Python.')
myfile.write(' I also like JavaScript.')
myfile.close()

# Append/Add into the file
myfile = open('Eiman.txt', 'a')
myfile.write(' This is an append text.')
myfile.close()


# Read from a file
myfile = open('Eiman.txt', 'r+')
readTheText = myfile.read(500)
print(readTheText)
