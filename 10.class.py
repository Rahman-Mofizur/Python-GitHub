class class_7:
    def __init__(self, name, id, age, cgpa):
        self.name = name
        self.id = id
        self.age = age
        self.cgpa = cgpa


Roll_53 = class_7('Afia Tasnim', '530722', '12', '3.5')
Roll_06 = class_7('Ipshita Alam Piyasha', '060722', '12', '3.6')
Roll_25 = class_7('Nafeesa Tabassum Dipu', '250722', '13', '3.45')

print(Roll_53.name, Roll_53.id, Roll_53.age, Roll_53.cgpa)
print(Roll_06.name, Roll_06.id, Roll_06.age, Roll_06.cgpa)
print(Roll_25.name, Roll_25.id, Roll_25.age, Roll_25.cgpa)

print(f'My name is ' + Roll_53.name + ' and my id is ' +
      Roll_53.id + '. I am ' + Roll_53.age + ' years old.')
