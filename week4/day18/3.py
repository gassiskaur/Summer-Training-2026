#inbuilt list functions:
#range 


data=list(range(10,101,10))
print(data)


#SLICING:                           #wont work on set and dictionary as they have hashing and not indexing 
print('data[2:5]',data[2:5])        #here 2 is inclusive but 5 is not inclusive [standard], this is sequential indexing 
print('data[:5]',data[:5])
print('data[5:]',data[5:])
print('data[:-5]',data[:-5])
print('data[-5:-2]',data[-5:-2])


#CONCATINATION:                     #wont work on set and dictionary 
data1= [10,20,30]
data2= [40,50,60]

data3= data1+data2
print('data3 : ',data3)

#doesnot work on dictionary 
'''dict1={
    1:'apple'
}
dict2 = {
    2:'banana'
}

dict3= dict1+dict2
print(dict3)'''

#MULTIPLICITY 

data4=[10,20,30]
data5= data4 * 3
print('data5: ',data5)


#MEMBERSHIP TESTING 

print(10 in data4)
print(100 in data4)
print(100 not in data4)


#membership testing works for all i.e. inclusing set and dictionary 

#on set 
data6={10,20,30}
print(30 in data6)

#on dictionary 
my_dictionary={
    1:'apple',
    2:'banana'
}
print(1 in my_dictionary)
print('apple' in my_dictionary)  #membership testing doesnot work on values but only keys of a dictionary 