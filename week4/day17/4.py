#decorator as design pattern 
#(Implementing decorators in oops)

class FreePlan:
    def __init__(self, name, price):
        self.name = name
        self.price = price 

    def show (self):
        print('Name: ',self.name,' Price: ',self.price)


class UpgradePlan:

    def __init__(self, freeplan):
        self.freeplan= freeplan 
        self.freeplan.name = 'PAID PLAN'
        self.freeplan.price +=200

    def show(self):
        print('PLAN: ', self.freeplan.name, 'PRICE: ',self.freeplan.price)


freeplan= FreePlan(name='FREE Plan', price= 0)

upgrade = UpgradePlan(freeplan=freeplan)

upgrade.show()