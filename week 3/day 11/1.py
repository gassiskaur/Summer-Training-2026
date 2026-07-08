"""file = open('code3.py', 'r')
data = file.read()
print(data)
"""


file= open('code3.py', 'r')

lines= file.readlines()
print(lines)

#to get output line by line , we use:
for line in lines:
    print(line)




    