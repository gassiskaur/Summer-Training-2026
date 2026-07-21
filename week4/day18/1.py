#built in functions of python multivalue containers 
'''
sequences are those data types that work on indexing: (not arrays as they have fixed size)
(dynamic arrays)
list
tuple
string 

other multivalue containers:
set (hashing)
dictionary (key value pair where keys are hashed)

'''


#INDEXING : 


my_data=[10,20,30,40,50]
print(my_data[0])
print(my_data[-1])
print(my_data[-5])
#print(my_data[7])    #run time error, [List index out of range]

# note: there is no compile time errors in pyhton and javascript etc they are interpreted 
# after one run time error is detected, after that whatever code is written is not execcuted 
# this is usually said in the softwares as 'your application has stopped working'
# the error "Application took too long to respond" is a different error because of long running processes in the main thread 

#hand=ling the run time errors in this way, so that code doesnot crash 
try: 
    print(my_data[7])
except:
    print('Something went wrong')

print('Last statement')


#is SERVER a hardware or a software, it is a software, it is above the operating system, applications run on server softwares 
#apachi toncap is an example for the server 

print('indexing on tuple:')

my_tuple= (10,20,30,40)
print(my_tuple[0])


print('Indexing on string: ')

my_string= 'Apple Banana'
print(my_string[-3])