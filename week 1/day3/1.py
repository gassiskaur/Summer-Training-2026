a=10
b=a

print("ID of a: ", id(a))
print("ID of b: ", id(b))

b=100
print("b: ", b, id(b))
print("a: ",a, id(a))

data=[10,20,30,40,50]
numbers=data

print("id of data: ", id(data))
print("id of numbers: ", id(numbers))

data[1]=1000
print('data[1]: ', data[1])
print('numbers[1]: ', numbers[1])
print("id of a: ", id(a))
print("id of b: ", id(b))


numbers[3]=4000
print('numbers[3]: ',numbers[3] )
print('data[3]: ',data[3] )