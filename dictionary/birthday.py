
birthdays = {
        'Sachin': '03/14/2003',
        'Carl': '01/17/2001',
        'Khan': '12/10/2006',
        'Donald': '06/14/2010',
        'Rohan': '01/6/2005'}


name = input("Enter name: ").title()

if name in birthdays:
    print(name, birthdays[name])
else:
    print('No names found')