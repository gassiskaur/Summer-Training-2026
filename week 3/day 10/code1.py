class FastTag:
    def __init__(self, fasttag_id, bank, balance):
        self.fasttag_id = fasttag_id ,
        self.balance = balance ,
        self.bank = bank

    def show(self):
        print('FAST TAG')
        print(self.fasttag_id, self.bank, self.balance)

class Vehicle :
    def __init__(self,registration_number,type,fasttag):
        self.registration_number= registration_number,
        self.type= type,
        self.fasttag=fasttag

    def show(self):
        print('VEHICLE')
        print(self.registration_number, self.fasttag, self.type)

        self.fasttag.show()
        print('end of vehicle')


