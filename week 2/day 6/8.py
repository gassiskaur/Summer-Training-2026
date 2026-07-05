def square_of_numbers(numbers):
    print('[square_of_number] start')
    print('[square_of_number] Before', numbers, id(numbers))
    
    for index in range(len(numbers)):
        numbers[index] = numbers[index] * numbers[index]

    print('[square_of_number] After', numbers, id(numbers))
    print('[square_of_number] end')
    # return

#IN THIS CASE, the original list is modified because lists are mutable objects in Python. 
#When you pass a list to a function, you are passing a reference to that list, not a copy of it. 
#Therefore, any changes made to the list inside the function will affect the original list outside the function.



#HOW TO PREVENT THIS SITUATION?



def square_of_numbers(numbers):
    print('[square_of_number] start')
    print('[square_of_number] Before', numbers, id(numbers))
    
    #using a new variable that points to a seperate memory location 
    my_numbers = []
    for index in range(len(numbers)):
       my_numbers.append(numbers[index])

    print('[square_of_number] Before', my_numbers, id(my_numbers))

    for index in range(len(my_numbers)):
        my_numbers[index] = my_numbers[index] * my_numbers[index]

    print('[square_of_number] After', my_numbers, id(my_numbers))
    print('[square_of_number] After', numbers, id(numbers))
    print('[square_of_number] end')
    # return




data=[10, 20, 30, 40, 50]
square_of_numbers(numbers=data)

print('After calling the function', data, id(data))



