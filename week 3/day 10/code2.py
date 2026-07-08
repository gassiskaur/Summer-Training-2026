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