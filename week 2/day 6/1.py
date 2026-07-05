#understanding debugging in python


for i in range(7):
    print(i)
    if i == 3:
        break

#using logs 


for i in range(7):
    print('i = ', i)
    if i == 3:
        print("Breaking the loop at i =", i)
        break
