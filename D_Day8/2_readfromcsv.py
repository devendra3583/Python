import csv


exampleFile = open('abcd.csv')
exampleReader = csv.reader(exampleFile)

print exampleReader.next()
ex = list(exampleReader)
#print ex
exampleFile.close()






 


