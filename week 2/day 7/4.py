#bubble sort 

def sort(data):
    for i in range (len(data)):
        for j in range (len(data)-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]


numbers=[10, 30,20,5,15]
result= sort(numbers)
print("The sorted list is:", numbers)





