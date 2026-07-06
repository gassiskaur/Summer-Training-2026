#function re defination in python 

'''def add_numbers(a,b):
    return a+b

def add_numbers(a,b,c):      #the last copy of function will be used in python
    return a+b+c


print('sum is', add_numbers(10,20,30)) #calling the function using 3 parameters'''

#preventing deletion of original function by using refrence copy operation

def add_numbers(a,b):
    return a+b

add=add_numbers #refrence copy operation

def add_numbers(a,b,c):      
    return a+b+c

print('sum is', add(10,20))
print('sum is', add_numbers(10,20,30))

