#list 
#orders = ['Pizza', 'Burger', 'Ramen', 'Coke']

#tuple 
#orders = ('Pizza', 'Burger', 'Ramen', 'Coke')

#set 
#orders = {'Pizza', 'Burger', 'Ramen', 'Coke'}

#string 
orders = 'Pizza'

#dictionary 
orders={
    1 : 'Pizza',
    2 : 'Burger',
    3 : 'Ramen',
    4 : 'Coke'
}

orders_iterator= iter(orders)
'''print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))'''

#to print both key and value in a dictionary 
key= next(orders_iterator)
print(key, orders[key])