def product(numbers, length):
    if length == 1:
        return 1
    else :
        previous = product(numbers, length - 1)
        current = numbers[length - 1]
        return current * previous
    

data= [2,3,8]
result= (product(data, len(data)))
print("The product of the values in the list is:", result)
