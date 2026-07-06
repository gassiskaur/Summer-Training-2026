# finding the max using recursion in a list 


data = [10,40,30,50,20]

def find_max(numbers, length):
    if length == 1:
        return numbers[0]
    else:
        previous = find_max(numbers, length - 1)
        current = numbers[length - 1]
    
        if current > previous:
            return current  
        else :
            return previous
    

result= (find_max(data, len(data)))
print("The maximum value in the list is:", result) 

