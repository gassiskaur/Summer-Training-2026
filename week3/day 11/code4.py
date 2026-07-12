file = open('quotes.txt','w')

quote= input('enter a quote: ')

file.write(quote)
file.close()

print('quote saved! ')

