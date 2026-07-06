from class_cdll import CircularDoublyLinkedList
from class_Song import Song 

song_list= CircularDoublyLinkedList()

song_list.add(element= Song(title= '1. is it a crime',
                            artist= 'Sade',
                            duration= 4.0,
                            previous_song = None,
                            next_song=None))

song_list.add(element=Song(title= '2. 7 seconds', 
            artist= 'neneh cherry',
            duration= 5.0,
            previous_song=None,
            next_song=None))

song_list.add(element=Song(title= '3. no ordinary love', 
            artist= 'Sade',
            duration= 4.5,
            previous_song=None,
            next_song=None))

song_list.add(element=Song(title= '4. paradise', 
            artist= 'Sade',
            duration= 6.0,
            previous_song=None,
            next_song=None))

song_list.add(element=Song(title= '5. wicked game', 
            artist= 'chris isaak',
            duration= 5.0,
            previous_song=None,
            next_song=None))



print(vars(song_list))

song_list.show()