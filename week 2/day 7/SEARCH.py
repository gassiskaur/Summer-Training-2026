flight1={
    'code': 'AA123',
    'carrier': 'Indigo',
    'source': 'delhi',
    'destination': 'bangluru',
    'fare': 5000,
    'duration': 2.5
}

flight2={
    'code': 'AI456',   
    'carrier': 'Air India',
    'source': 'bangluru',
    'destination': 'delhi',
    'fare': 6000,
    'duration': 3                  
}

flight3={
    'code': 'SG789',
    'carrier': 'SpiceJet',
    'source': 'delhi',  
    'destination': 'mumbai',
    'fare': 4000,
    'duration': 2
}

flight4={
    'code': 'GJ101',
    'carrier': 'GoAir',
    'source': 'mumbai',
    'destination': 'delhi',
    'fare': 4500,
    'duration': 2.5
}

flight5={
    'code': 'VJ202',
    'carrier': 'Vistara',
    'source': 'delhi',
    'destination': 'chennai',
    'fare': 5500,
    'duration': 3
}

#list of dictionaries 
flights = [flight1, flight2]

#1.search code 
#2.sort fare,duration 
#3.filter carrier, price, duration 

# search 
def search (flights, code):
    for flight in flights:
        if flight['code'] == code:
            print(flight)
            break
    else:
        print("Flight not found")


def main():

    (search(flights, 'AA123'))  


