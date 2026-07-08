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

class toll_plaza_queue:


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print('[toll_plaza_queue] [init] Object Constrcuted', self)

    
    def add(self, element):
        self.size += 1
        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.head.previous = element
            element.previous = self.tail
            element.next = self.head
            self.tail = element
        print('The following Vehicle added to queue.')
        print(element.show())




    def deduct_toll(self, element):
        print('deducting toll:')
        print('balance: ', element.fasttag.balance)
        if element.type == '4W':
            element.fasttag.balance = element.fasttag.balance - 100
        else:
            pass 

        print("toll deducted: new balance: ", element.fasttag.balance)
        self.delete()




    def delete(self,):
        self.size -= 1
        self.head= self.head.next
        print('vehicle removes from queue')



    def show(self, traverse=True):
        if traverse:
            element = self.head
            while True:
                element.show()
                element = element.next

                if element == self.head:
                    break

        else:
            element = self.tail

            while True:
                element.show()
                element = element.previous

                if element == self.tail:
                    break




def main():

    vehicle1= Vehicle(
        registration_number= 'PB10AL9743',
        type='4W',
        fasttag=FastTag(
            fasttag_id= 8920,
            bank='SBI', balance=1000
        )
    
    )

    vehicle2= Vehicle(
        registration_number= 'PB10AL3802',
        type='4W',
        fasttag=FastTag(
            fasttag_id= 1230,
            bank='ICIC',
            balance=50
        )
    
    )

    vehicle3= Vehicle(
        registration_number= 'HR10AL3742',
        type='2W',
        fasttag=FastTag(
            fasttag_id= 5730,
            bank='ICIC',
            balance=700
        )
    
    )

    vehicle4= Vehicle(
        registration_number= 'AP10MN9323',
        type='4W',
        fasttag=FastTag(
            fasttag_id= 2434,
            bank='KSI',
            balance=990
        )
    
    )

    vehicle5= Vehicle(
        registration_number= 'PB34BL9292',
        type='4W',
        fasttag=FastTag(
            fasttag_id= 1242,
            bank='ICIC',
            balance=860
        )
    
    )

    queue= toll_plaza_queue()
    queue.add(vehicle1)
    queue.add(vehicle2)
    queue.add(vehicle3)
    queue.add(vehicle4)
    queue.add(vehicle5)

    queue.show()



    queue.deduct_toll(vehicle1)
    queue.deduct_toll(vehicle2)
    queue.deduct_toll(vehicle3)
    queue.deduct_toll(vehicle4)
    queue.deduct_toll(vehicle5)

    print('size of queue: ', queue.size)


if __name__ == '__main__':
    main()


