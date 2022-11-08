# JSON is commonly used with data APIs. Here how we can parse JSON into a Python dictionary

import json

# Simple JSON
Mofiz_person_1 = '{"first_name": "Mohammed","last_name": "Eiman","age": "22","cgpa": "3.66"}'

# Print the properties of Mofiz_person_1 object through loading the jason dictionary using json.loads
print(json.loads(Mofiz_person_1))

# Or create an object named user and pass the loads of json into the user object/instance
# This is a system to find the dictionary from the JSON format
Elias = json.loads(Mofiz_person_1)
print(Elias)

# Make JSON format from a dictionary
car_Mofiz = {'made by': 'Toyota', 'Model': 'Corolla', 'Year': '2022'}
print(json.dumps(car_Mofiz))

Corolla2022 = json.dumps(car_Mofiz)
print(Corolla2022)
