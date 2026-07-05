#refrence copy operations on functions 

def add_numbers(a, b):
    print('a =', a)
    print('b =', b)
    print('sum =', a + b)

add=add_numbers #refrence copy operation

add(10, 20) #calling the function using refrence copy

add_numbers(30, 40) #calling the function using original name


