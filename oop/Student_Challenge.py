class Employee:
    employee_count = 101

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.eid = 'e' + str(Employee.employee_count)
        Employee.employee_count += 1

    def show_details(self):
        print('Name: ', self.name)
        print('Salary: ', self.salary)
        print('Designation: ', self.designation)
        print('Employee id: ', self.eid)

    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101


e1 = Employee('Sagun', 500000, 'DS')
e2 = Employee('Zaha', 500000, 'Manager')
print(e1.show_details())
print(e2.show_details())

print(e2.total_emp())
