#THER CAN BE DIMENSIONS TO LIST, THIS IS A 2D LIST:
#real world application: bookmyshow etc 

numbers = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

print(len(numbers))
print(len(numbers[0]))
print((numbers[1][0]))



#This is a 3D list:
#real world application: population of the world world-contries-states

large_data = [
    [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ],
    [
        [32,23,34],
        [40,50,53],
        [34,43,54]
    ]
]

print(len(large_data))
print(large_data[-1][-1][-2])