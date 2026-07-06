# Variable Arguments in Python
def add_numbers(*args):
    print(args)  
    print(type(args))
    print(sum(args))


add_numbers(10, 20, 30, 40, 50)
add_numbers(10, 20, 30)
add_numbers(-10, -20, -30)


# Keyword Arguments -> KeyWord Variable Arguments
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))


fun(a=10, b=20, c=30, d='john')
fun(name='john', email='john@example.com', phone='+919876543210')


#using both variable and keyword variable arguments in a single function

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(10, 'john', 30, a=10, b=20, c=30)

