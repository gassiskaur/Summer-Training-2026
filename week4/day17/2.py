#generators:


def Orders():
    
    list1 = {'pizza', 'burger'}
    yield list1

    dictionary = {
        '1': 'pizza',
        '2': 'Burger'
    }
    yield dictionary
    tuple1 = ['pizza', 'burger']
    yield tuple1


order= Orders()
print(order, type(order))


for o in order:
    print(o)


