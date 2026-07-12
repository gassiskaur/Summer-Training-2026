# class SongList:
class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print('[CircularDoublyLinkedList] [init] Object Constrcuted', self)


    def add(self, element):
        
        self.size += 1

        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next_song = element
            self.head.previous_song = element
            element.previous_song = self.tail
            element.next_song = self.head
            self.tail = element

    def show(self, traverse=True):

        if traverse:
            element = self.head
            while True:
                element.show_song()
                element = element.next_song

                if element == self.head:
                    break

        else:
            element = self.tail

            while True:
                element.show_song()
                element = element.previous_song

                if element == self.tail:
                    break





