##using with keyword


with open('quotes.txt') as file:
    lines = file.readlines()
    for line in lines:
        print(line)

file.close()
print('Program Finished')