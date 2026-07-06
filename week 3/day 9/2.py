class Song:
    def __init__(self,title,artist,duration, next_song, previous_song ):
        self.title= title 
        self.artist= artist 
        self.duration= duration
        self.next_song= None 
        self.previous_song = None 

    
    #make a function to display songs 
    def show_song(self):
        print('~~~~~')
        print('title: ', self.title)
        print('artists: ', self.artist)
        print('duration: ', self.duration)
        print('next song: ', self.next_song)
        print('previous song: ', self.previous_song)
        print('~~~~~')



#make 5 objects i.e. songs 

song1= Song(title= '1. is it a crime', 
            artist= 'Sade',
            duration= 4.0,
            previous_song=None,
            next_song=None)

song2= Song(title= '2. 7 seconds', 
            artist= 'neneh cherry',
            duration= 5.0,
            previous_song=None,
            next_song=None)

song3= Song(title= '3. no ordinary love', 
            artist= 'Sade',
            duration= 4.5,
            previous_song=None,
            next_song=None)

song4= Song(title= '4. paradise', 
            artist= 'Sade',
            duration= 6.0,
            previous_song=None,
            next_song=None)

song5= Song(title= '5. wicked game', 
            artist= 'chris isaak',
            duration= 5.0,
            previous_song=None,
            next_song=None)

#code the next and previous songs 

song1.next_song=song2
song2.next_song=song3
song3.next_song=song4
song4.next_song=song5
song5.next_song=song1

song1.previous_song=song5
song2.previous_song=song1
song3.previous_song=song2
song4.previous_song=song3
song5.previous_song=song4


#print the songs dynamically 


print('FORWARD TRAVERSING:')
song = song1

while True:
    song.show_song()
    song = song.next_song

    if song == song1:
        break


print('BACKWARD TRAVERSING:')
song = song5

while True:
    song.show_song()
    song = song.previous_song

    if song == song5:
        break


