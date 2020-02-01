import csv


exampleFile = open('abcd.csv')
exampleReader = csv.reader(exampleFile)

#print exampleReader.next()
ex = list(exampleReader)
print ex
exampleFile.close()

r=raw_input('enter city: ')
for i in ex:
	if r in i:
		print i





 


