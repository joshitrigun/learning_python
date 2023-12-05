class Customer:
    def __init__(self, userid, name, bdno, bstreet, bcity, bcountry, bpin, sdno, sstreet, scity, scountry, spin):
        self.id = userid
        self.name = name
        self.baddress = self.Address(bdno, bstreet, bcity, bcountry, bpin)
        self.saddress = self.Address(sdno, sstreet, scity, scountry, spin)

    class Address:
        def __init__(self, dno, street, city, country, pin):
            self.dno = dno
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.dno)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)


c = Customer(1, 'Trigun', 101, 'abc', 'Richmond', 'Canada', 10001, 200, 'nor', 'van', 'USA', 4001)
c.saddress.display()