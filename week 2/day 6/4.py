#understanding parameters and arguments in python

def add_numbers(a, b):
    print('a =', a)
    print('b =', b)
    print('sum =', a + b)

def multiply_numbers(x, y=1):
    print('x =', x)
    print('y =', y)
    print('product =', x * y)

add_numbers(10, 20)
multiply_numbers(10)


