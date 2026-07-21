numbers=list(range(10,101,10))


#append finction adds data at the end of the container 
numbers.append(101)


#insert can insert element at any index 
numbers.insert(3, 33)

#some built in functions that work on all data types (there may be exeptions)

#sum function - dictionary cannot be added 
print(sum(numbers))

#min
print(min(numbers))

#max
print(max(numbers))

#len
print(len(numbers))

#average- no direct function in python (not on dictionary )
print(sum(numbers)/len(numbers))

# data = tuple(numbers)
# data = set(numbers)
# data = str(numbers)
# data = dict(numbers) : error
# print('data:', data, type(data))

reverse_numbers = list(reversed(numbers))
print('reverse_numbers:', reverse_numbers)

# Python - reverse with slicing technique
print(numbers[::-1])

# numbers.sort(reverse=True)
numbers.sort()
print(numbers)

index = numbers.index(101)
print('index of 101:', index)

numbers.remove(99)
del numbers[6]
numbers.clear()
# del numbers

data = [10, 20, 30, 40, 50]
print('before data:', data)
# data.append(70)
data.pop()
print('after data:', data)


#we can convert a list into following data types anytime: 
# data = tuple(numbers)
# data = set(numbers)
# data = str(numbers)
# data = dict(numbers) : error
# print('data:', data, type(data))

reverse_numbers = list(reversed(numbers))
print('reverse_numbers:', reverse_numbers)

# Python - reverse with slicing technique
print(numbers[::-1])

# numbers.sort(reverse=True)  we can also sort in descending order 
numbers.sort()
print(numbers)

#we can find index of any element 
index = numbers.index(101)  
print('index of 101:', index)

#we can remove any element 
numbers.remove(99)

#we can delete an element using its index 
del numbers[6]

#we can empty our container/list 
numbers.clear()

#we can completely delete our list from the memory 
# del numbers

data = [10, 20, 30, 40, 50]
print('before data:', data)
# data.append(70)
data.pop()
print('after data:', data)


print('Numbers: ', numbers)