#Q. WAP to copy content from 1 csv to another csv
print 'reading from csv and writing to a csv'
import csv
f=open('from.csv')
content = csv.reader(f) #reader() is a function of csv.py file/module used to read
l = list(content)

f_write = open('to.csv', 'wb')
wr = csv.writer(f_write) #writer is a function of csv to write into csv
for i in l:
	wr.writerow(i) #write into wr the values i
f_write.close()
