# append mode to write into file 

file = open('quotes.txt', 'a') 
quote = input('Enter a Quote: ')
file.write(quote+'\n')
file.close()
print('Quote Saved...')


