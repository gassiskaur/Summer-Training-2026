def find_max(numbers):
    max = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] > max:
            max = numbers[index]

    print('max in', numbers, 'is:', max)


data = [10, 20, 50, 70, 30, 15]
scores = [27, 110, 35, 89, 20, 30]
prices = [1500, 3000, 5000, 1200, 4500]

#refrence copy operation:

find_max(numbers=data)

#simple way to call the function:

find_max(scores)

#inputing the data itself:

find_max([1500, 3000, 5000, 1200, 4500])


