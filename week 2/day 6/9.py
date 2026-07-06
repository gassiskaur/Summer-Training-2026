#basics of recursion:

def print_number(number):
    if number <=10:
        print(number)
        print_number(number+1) # execute the same function again from itself
    
    # return


print_number(5)

