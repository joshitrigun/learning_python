Students = {}

for i in range(3):
    name = input('Enter name?: ')
    roll = int(input('Enter roll no.? '))
    dept_name = input('Enter dept name? ')

    Students[name] = {
        'Roll': roll,
        'Name': name,
        'Dept': dept_name
    }

print(Students)