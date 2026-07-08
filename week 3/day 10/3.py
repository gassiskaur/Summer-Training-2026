from code1 import FastTag, Vehicle 
from code2 import *
    


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



