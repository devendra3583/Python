#Q. WAP to take input of 3 people's name, surname and location and store it into a file?
import csv


def csv_writer(data,path):
	fo = open(path,'wb')#writing b also bec 1. csv and 2. python 2.7.x
	writer = csv.writer(fo)
	for i in data:
		writer.writerow(i)
	fo.close()


if __name__ == "__main__":
	data1 = [
			['Vin','Kumar','Delhi'],
			['Dev','Kumar','Jhansi'],
			['Faheem', 'Mohd', 'Kanpur']
		]
	path = "file.csv"
	csv_writer(data1,path)
	

	#Input
	data2 = []
	for i in range(3):
		print 'First Person'		
		a=raw_input('Enter name: ')
		b=raw_input('Enter surname: ')
		c=raw_input('Enter location: ')
		l = []
		l.append(a)
		l.append(b)
		l.append(c)
		data2.append(l)
	csv_writer(data2,'file1.csv')
