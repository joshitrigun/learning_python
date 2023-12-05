class NegativeAgeException(Exception):
    pass

def stage(age):

    try:
        if age < 0:
            raise NegativeAgeException('Age should be greater than zero')
        elif 0 <= age < 13:
            print('Kid')
        elif 13 <= age < 19:
            print('Teen')
        elif 19 <= age <= 50:
            print('Young')
        else:
            print('Old')

age = int(input('Enter age'))

try:
    stage(age)
except NegativeAgeException as e:
    print(e)